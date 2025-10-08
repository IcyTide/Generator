from PySide6.QtWidgets import QDialog, QHBoxLayout, QLineEdit, QPushButton, QSpinBox, QVBoxLayout, QWidget, QLabel

from base.constant import SHIELD_BASE_MAP
from base.expression import Constant
from qt.classes.attribute import Attribute
from qt.classes.buff import BuffType
from qt.classes.section import Section, Sections
from qt import LabelRow, ComboBox


class SectionEditorDialog(QDialog):
    section: Section = None

    def __init__(self, value: Section = None, parent: QWidget = None):
        super().__init__(parent)
        self.setWindowTitle("Edit Section")
        layout = QVBoxLayout(self)

        if value:
            self.section = Section(value.name, value.count)
        else:
            self.section = Section()
        self.name_edit = QLineEdit(self.section.name)
        self.name_row = LabelRow("Name:", self.name_edit)
        self.count_spin = QSpinBox(minimum=1, value=self.section.count)
        self.count_row = LabelRow("Count:", self.count_spin)

        layout.addWidget(self.name_row)
        layout.addWidget(self.count_row)

        layout.addLayout((btn_layout := QHBoxLayout()))
        btn_layout.addWidget((ok_button := QPushButton("OK")))
        btn_layout.addWidget((cancel_button := QPushButton("Cancel")))

        ok_button.clicked.connect(self.accept)
        cancel_button.clicked.connect(self.reject)
        self.name_edit.textChanged.connect(self.edit_name)
        self.count_spin.valueChanged.connect(self.select_count)

    def edit_name(self, name: str):
        if name := name.strip():
            self.section.name = name

    def select_count(self, count: int):
        self.section.count = count


class SectionDamageDialog(QDialog):
    def __init__(
            self, section: Section, current: Attribute, snapshot: Attribute, parent: QWidget = None
    ):
        super().__init__(parent)
        self.setWindowTitle("Damage Detail")

        layout = QVBoxLayout(self)

        self.expected_damage = Constant(0)
        for record in section.records:
            record_damage = Constant(0)
            for buff in record.buffs:
                if buff.buff_type == BuffType.Current:
                    current.add_buff(buff)
                elif buff.buff_type == BuffType.Snapshot:
                    snapshot.add_buff(buff)
            variables = {**current.current, **current.snapshot}
            for skill in record.skills:
                damage = skill.damage.evaluate(variables) * skill.count
                critical_strike = skill.critical_strike.evaluate(variables)
                record_damage += damage * (1 - critical_strike)
                critical_damage = skill.critical_damage.evaluate({**variables, "damage": damage})
                record_damage += critical_damage * critical_strike
            variables = {**current.current, **snapshot.snapshot}
            for dot in record.dots:
                damage = dot.source.damage.evaluate({**variables, "tick": dot.tick}) * dot.stack * dot.count
                critical_strike = dot.source.critical_strike.evaluate(variables)
                record_damage += damage * (1 - critical_strike)
                critical_damage = dot.source.critical_damage.evaluate({**variables, "damage": damage})
                record_damage += critical_damage * critical_strike
            for buff in record.buffs:
                if buff.buff_type == BuffType.Current:
                    current.sub_buff(buff)
                elif buff.buff_type == BuffType.Snapshot:
                    snapshot.sub_buff(buff)
            self.expected_damage += record_damage * record.count
        self.expected_damage *= section.count

        layout.addWidget(LabelRow("Name:", QLabel(section.name)))
        layout.addWidget(LabelRow("Count:", QLabel(str(section.count))))
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


class AllDamageDialog(QDialog):
    def __init__(
            self, sections: Sections, current: Attribute, snapshot: Attribute, parent: QWidget = None
    ):
        super().__init__(parent)
        self.setWindowTitle("Damage Detail")

        layout = QVBoxLayout(self)

        self.expected_damage = Constant(0)
        for section in sections:
            section_damage = Constant(0)
            for record in section.records:
                record_damage = Constant(0)
                for buff in record.buffs:
                    if buff.buff_type == BuffType.Current:
                        current.add_buff(buff)
                    elif buff.buff_type == BuffType.Snapshot:
                        snapshot.add_buff(buff)
                variables = {**current.current, **current.snapshot}
                for skill in record.skills:
                    damage = skill.damage.evaluate(variables) * skill.count
                    critical_strike = skill.critical_strike.evaluate(variables)
                    record_damage += damage * (1 - critical_strike)
                    critical_damage = skill.critical_damage.evaluate({**variables, "damage": damage})
                    record_damage += critical_damage * critical_strike
                variables = {**current.current, **snapshot.snapshot}
                for dot in record.dots:
                    damage = dot.source.damage.evaluate({**variables, "tick": dot.tick}) * dot.stack * dot.count
                    critical_strike = dot.source.critical_strike.evaluate(variables)
                    record_damage += damage * (1 - critical_strike)
                    critical_damage = dot.source.critical_damage.evaluate({**variables, "damage": damage})
                    record_damage += critical_damage * critical_strike
                for buff in record.buffs:
                    if buff.buff_type == BuffType.Current:
                        current.sub_buff(buff)
                    elif buff.buff_type == BuffType.Snapshot:
                        snapshot.sub_buff(buff)
                section_damage += record_damage * record.count
            self.expected_damage += section_damage * section.count

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