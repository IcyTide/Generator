from PySide6.QtWidgets import QDialog, QDoubleSpinBox, QHBoxLayout, QLineEdit, QPushButton, QSpinBox, QVBoxLayout, \
    QWidget

from qt import LabelRow
from qt.classes.attribute import Attribute
from qt.classes.buff import BuffType
from qt.classes.section import Section, Sections
from qt.component.loop_widget.damage_dialog import DamageDialog
from qt.utils import evaluate_dot, evaluate_skill


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
        self.count_spin = QSpinBox(minimum=1, value=self.section.count)
        self.duration_spin = QDoubleSpinBox(minimum=0, value=0, maximum=1000)

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
            self.section.name = name

    def select_count(self, count: int):
        self.section.count = count

    def select_duration(self, duration: float):
        self.section.duration = duration


class SectionDamageDialog(DamageDialog):
    def __init__(self, section: Section, current: Attribute, snapshot: Attribute, parent: QWidget = None):
        self.damages, self.duration = {}, section.duration
        for record in section.records:
            count = section.count * record.count
            for buff in record.buffs:
                if buff.buff_type == BuffType.Current:
                    current.add_buff(buff)
                elif buff.buff_type == BuffType.Snapshot:
                    snapshot.add_buff(buff)
            variables = {**current.current, **current.snapshot}
            for skill in record.skills:
                if skill.name not in self.damages:
                    self.damages[skill.name] = 0
                _, _, _, expected_damage = evaluate_skill(skill, variables)
                self.damages[skill.name] += expected_damage * count
            variables = {**current.current, **snapshot.snapshot}
            for dot in record.dots:
                _, _, _, expected_damage = evaluate_dot(dot, variables)
                if dot.name not in self.damages:
                    self.damages[dot.name] = 0
                self.damages[f"{dot.name}"] += expected_damage * count
            for buff in record.buffs:
                if buff.buff_type == BuffType.Current:
                    current.sub_buff(buff)
                elif buff.buff_type == BuffType.Snapshot:
                    snapshot.sub_buff(buff)
        super().__init__(section.name, section.count, parent)


class AllDamageDialog(DamageDialog):
    def __init__(self, sections: Sections, current: Attribute, snapshot: Attribute, parent: QWidget = None):
        self.damages, self.duration = {}, 0
        for section in sections:
            self.duration += section.duration
            for record in section.records:
                count = section.count * record.count
                for buff in record.buffs:
                    if buff.buff_type == BuffType.Current:
                        current.add_buff(buff)
                    elif buff.buff_type == BuffType.Snapshot:
                        snapshot.add_buff(buff)
                variables = {**current.current, **current.snapshot}
                for skill in record.skills:
                    if skill.name not in self.damages:
                        self.damages[skill.name] = 0
                    _, _, _, expected_damage = evaluate_skill(skill, variables)
                    self.damages[skill.name] += expected_damage * count
                variables = {**current.current, **snapshot.snapshot}
                for dot in record.dots:
                    _, _, _, expected_damage = evaluate_dot(dot, variables)
                    if dot.name not in self.damages:
                        self.damages[dot.name] = 0
                    self.damages[f"{dot.name}"] += expected_damage * count
                for buff in record.buffs:
                    if buff.buff_type == BuffType.Current:
                        current.sub_buff(buff)
                    elif buff.buff_type == BuffType.Snapshot:
                        snapshot.sub_buff(buff)
        super().__init__("All", 1, parent)
