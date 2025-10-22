from PySide6.QtWidgets import QDialog, QDoubleSpinBox, QHBoxLayout, QLineEdit, QPushButton, QSpinBox, QVBoxLayout, \
    QWidget

from qt import LabelRow
from qt.classes.attribute import Attribute
from qt.classes.damage import Damage
from qt.classes.section import Section, Sections
from qt.component.loop_widget.damage_dialog import DamagesDialog, add_buffs_to_attributes, sub_buffs_to_attributes
from qt.utils import evaluate_dot, evaluate_skill


class SectionEditorDialog(QDialog):
    section: Section = None

    def __init__(self, value: Section = None, parent: QWidget = None):
        super().__init__(parent)
        self.setWindowTitle("编辑小节")
        layout = QVBoxLayout(self)

        if value:
            self.section = Section(value.name, value.count, value.duration, value.records)
        else:
            self.section = Section()
        self.name_edit = QLineEdit(self.section.name)
        self.count_spin = QSpinBox(minimum=1, value=self.section.count)
        self.duration_spin = QDoubleSpinBox(minimum=0, value=self.section.duration, maximum=1000)

        layout.addWidget(LabelRow("名称:", self.name_edit))
        layout.addWidget(LabelRow("数量:", self.count_spin))
        layout.addWidget(LabelRow("时长:", self.duration_spin))

        layout.addLayout((btn_layout := QHBoxLayout()))
        btn_layout.addWidget((ok_button := QPushButton("确定")))
        btn_layout.addWidget((cancel_button := QPushButton("取消")))

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


class SectionDamageDialog(DamagesDialog):
    def __init__(self, section: Section, current: Attribute, snapshot: Attribute, parent: QWidget = None):
        self.damages, self.duration = {}, section.duration
        for record in section.records:
            add_buffs_to_attributes(record.buffs, current, snapshot)
            variables = {**current.current, **current.snapshot}
            for skill in record.skills:
                count = record.count * skill.count
                if skill.name in self.damages:
                    damage = self.damages[skill.name]
                else:
                    damage = self.damages[skill.name] = Damage(skill.name)
                _, _, _, expected_damage = evaluate_skill(skill, variables)
                damage.formula += expected_damage * count
                damage.count += count
            variables = {**current.current, **snapshot.snapshot}
            for dot in record.dots:
                count = record.count * dot.count
                if dot.name in self.damages:
                    damage = self.damages[dot.name]
                else:
                    damage = self.damages[dot.name] = Damage(dot.name)
                _, _, _, expected_damage = evaluate_dot(dot, variables)
                damage.formula += expected_damage * count
                damage.count += count
            sub_buffs_to_attributes(record.buffs, current, snapshot)
        super().__init__(section.name, section.count, parent)


class AllDamageDialog(DamagesDialog):
    def __init__(self, sections: Sections, current: Attribute, snapshot: Attribute, parent: QWidget = None):
        self.damages, self.duration = {}, 0
        for section in sections:
            self.duration += section.duration * section.count
            for record in section.records:
                add_buffs_to_attributes(record.buffs, current, snapshot)
                variables = {**current.current, **current.snapshot}
                for skill in record.skills:
                    count = section.count * record.count * skill.count
                    if skill.name in self.damages:
                        damage = self.damages[skill.name]
                    else:
                        damage = self.damages[skill.name] = Damage(skill.name)
                    _, _, _, expected_damage = evaluate_skill(skill, variables)
                    damage.formula += expected_damage * count
                    damage.count += count
                variables = {**current.current, **snapshot.snapshot}
                for dot in record.dots:
                    count = section.count * record.count * dot.count
                    if dot.name in self.damages:
                        damage = self.damages[dot.name]
                    else:
                        damage = self.damages[dot.name] = Damage(dot.name)
                    _, _, _, expected_damage = evaluate_dot(dot, variables)
                    damage.formula += expected_damage * count
                    damage.count += count
                sub_buffs_to_attributes(record.buffs, current, snapshot)
        super().__init__("总计", 1, parent)
