from PySide6.QtWidgets import QDialog, QHBoxLayout, QLineEdit, QPushButton, QSpinBox, QVBoxLayout, QWidget, QLabel

from base.constant import SHIELD_BASE_MAP
from base.expression import Constant
from qt.classes.attribute import Attribute
from qt.classes.buff import BuffType
from qt.classes.record import Record
from qt import LabelRow, ComboBox


class RecordEditorDialog(QDialog):
    record: Record = None

    def __init__(self, value: Record = None, parent: QWidget = None):
        super().__init__(parent)
        self.setWindowTitle("Edit Record")
        layout = QVBoxLayout(self)

        if value:
            self.record = Record(value.name, value.count)
        else:
            self.record = Record()
        self.name_edit = QLineEdit(self.record.name)
        self.count_spin = QSpinBox(minimum=1, value=self.record.count)

        layout.addWidget(LabelRow("Name:", self.name_edit))
        layout.addWidget(LabelRow("Count:", self.count_spin))

        layout.addLayout((btn_layout := QHBoxLayout()))
        btn_layout.addWidget((ok_button := QPushButton("OK")))
        btn_layout.addWidget((cancel_button := QPushButton("Cancel")))

        ok_button.clicked.connect(self.accept)
        cancel_button.clicked.connect(self.reject)
        self.name_edit.textChanged.connect(self.edit_name)
        self.count_spin.valueChanged.connect(self.select_count)

    def edit_name(self, name: str):
        if name := name.strip():
            self.record.name = name

    def select_count(self, count: int):
        self.record.count = count


class RecordDamageDialog(QDialog):
    def __init__(
            self, record: Record, current: Attribute, snapshot: Attribute, parent: QWidget = None
    ):
        super().__init__(parent)
        self.setWindowTitle("Damage Detail")

        layout = QVBoxLayout(self)

        self.expected_damage = Constant(0)
        for buff in record.buffs:
            if buff.buff_type == BuffType.Current:
                current.add_buff(buff)
            elif buff.buff_type == BuffType.Snapshot:
                snapshot.add_buff(buff)
        variables = {**current.current, **current.snapshot}
        for skill in record.skills:
            damage = skill.damage.evaluate(variables) * skill.count
            critical_strike = skill.critical_strike.evaluate(variables)
            self.expected_damage += damage * (1 - critical_strike)
            critical_damage = skill.critical_damage.evaluate({**variables, "damage": damage})
            self.expected_damage += critical_damage * critical_strike
        variables = {**current.current, **snapshot.snapshot}
        for dot in record.dots:
            damage = dot.source.damage.evaluate({**variables, "tick": dot.tick}) * dot.stack * dot.count
            critical_strike = dot.source.critical_strike.evaluate(variables)
            self.expected_damage += damage * (1 - critical_strike)
            critical_damage = dot.source.critical_damage.evaluate({**variables, "damage": damage})
            self.expected_damage += critical_damage * critical_strike
        self.expected_damage *= record.count

        layout.addWidget(LabelRow("Name:", QLabel(record.name)))
        layout.addWidget(LabelRow("Count:", QLabel(str(record.count))))
        self.target_level = ComboBox()
        layout.addWidget(LabelRow("Target Level:", self.target_level))
        self.expected_damage_label = QLabel("")
        layout.addWidget(LabelRow("Expected Damage:", self.expected_damage_label))

        self.target_level.currentTextChanged.connect(self.select_target_level)
        self.target_level.set_items(SHIELD_BASE_MAP)

    def select_target_level(self, level):
        if not level:
            return
        level = int(level)
        expected_damage = int(self.expected_damage.evaluate(
            {"target_level": level, "shield_base": SHIELD_BASE_MAP[level]}
        ))
        self.expected_damage_label.setText(str(expected_damage))
