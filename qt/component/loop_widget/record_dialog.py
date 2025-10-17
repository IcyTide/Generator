from PySide6.QtWidgets import QDialog, QDoubleSpinBox, QHBoxLayout, QLineEdit, QPushButton, QSpinBox, \
    QVBoxLayout, QWidget

from qt import LabelRow
from qt.classes.attribute import Attribute
from qt.classes.damage import Damage
from qt.classes.record import Record
from qt.component.loop_widget.damage_dialog import DamagesDialog, add_buffs_to_attributes
from qt.utils import evaluate_dot, evaluate_skill


class RecordEditorDialog(QDialog):
    record: Record = None

    def __init__(self, value: Record = None, parent: QWidget = None):
        super().__init__(parent)
        self.setWindowTitle("Edit Record")
        layout = QVBoxLayout(self)

        if value:
            self.record = Record(value.name, value.count, value.duration, value.buffs, value.skills, value.dots)
        else:
            self.record = Record()
        self.name_edit = QLineEdit(self.record.name)
        self.count_spin = QSpinBox(minimum=1, value=self.record.count)
        self.duration_spin = QDoubleSpinBox(minimum=0, value=self.record.duration, maximum=1000)

        layout.addWidget(LabelRow("Name:", self.name_edit))
        layout.addWidget(LabelRow("Count:", self.count_spin))
        layout.addWidget(LabelRow("Duration:", self.duration_spin))

        layout.addLayout((btn_layout := QHBoxLayout()))
        btn_layout.addWidget((ok_button := QPushButton("OK")))
        btn_layout.addWidget((cancel_button := QPushButton("Cancel")))

        ok_button.clicked.connect(self.accept)
        cancel_button.clicked.connect(self.reject)
        self.name_edit.textChanged.connect(self.edit_name)
        self.count_spin.valueChanged.connect(self.select_count)
        self.duration_spin.valueChanged.connect(self.select_duration)

    def edit_name(self, name: str):
        if name := name.strip():
            self.record.name = name

    def select_count(self, count: int):
        self.record.count = count

    def select_duration(self, duration: float):
        self.record.duration = duration


class RecordDamageDialog(DamagesDialog):
    def __init__(
            self, record: Record, current: Attribute, snapshot: Attribute, parent: QWidget = None
    ):
        add_buffs_to_attributes(record.buffs, current, snapshot)
        variables = {**current.current, **current.snapshot}
        self.damages, self.duration = {}, record.duration
        for skill in record.skills:
            count = skill.count
            if skill.name in self.damages:
                damage = self.damages[skill.name]
            else:
                damage = self.damages[skill.name] = Damage(skill.name)
            _, _, _, expected_damage = evaluate_skill(skill, variables)
            damage.formula += expected_damage * count
            damage.count += count
        variables = {**current.current, **snapshot.snapshot}
        for dot in record.dots:
            count = dot.count
            if dot.name in self.damages:
                damage = self.damages[dot.name]
            else:
                damage = self.damages[dot.name] = Damage(dot.name)
            _, _, _, expected_damage = evaluate_dot(dot, variables)
            damage.formula += expected_damage * count
            damage.count += count
        super().__init__(record.name, record.count, parent)
