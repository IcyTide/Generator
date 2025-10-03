from PySide6.QtWidgets import QDialog, QHBoxLayout, QLabel, QPushButton, QSpinBox, QVBoxLayout, QWidget

from base.constant import SHIELD_BASE_MAP
from base.expression import Variable
from qt import ComboBox, LabelRow
from qt.classes.attribute import Attribute
from qt.classes.skill import Skill
from qt.component.loop_widget.widget import LoopWidget


class SkillEditorDialog(QDialog):
    skills: dict[str, dict[int, dict[int, dict]]] = {}
    skill: Skill = None

    def __init__(self, skills: dict = None, skill: Skill = None, parent: LoopWidget = None):
        super().__init__(parent)
        self.setWindowTitle("Edit Skill")
        layout = QVBoxLayout(self)
        self.kungfu = parent.kungfu
        self.skills = skills
        self.belong_combo = ComboBox()
        self.id_combo = ComboBox()
        self.level_combo = ComboBox()
        self.count_spin = QSpinBox(minimum=1, value=1)
        self.count_row = LabelRow("Count:", self.count_spin)

        layout.addWidget(LabelRow("Belong:", self.belong_combo))
        layout.addWidget(LabelRow("ID:", self.id_combo))
        layout.addWidget(LabelRow("Level:", self.level_combo))
        layout.addWidget(self.count_row)

        self.name_label = QLabel("")
        self.comment_label = QLabel("")
        layout.addWidget(LabelRow("Name:", self.name_label))
        layout.addWidget(LabelRow("Comment:", self.comment_label))

        layout.addLayout((btn_layout := QHBoxLayout()))
        btn_layout.addWidget((ok_button := QPushButton("OK")))
        btn_layout.addWidget((cancel_button := QPushButton("Cancel")))

        ok_button.clicked.connect(self.accept)
        cancel_button.clicked.connect(self.reject)
        self.belong_combo.currentTextChanged.connect(self.select_belong)
        self.id_combo.currentTextChanged.connect(self.select_id)
        self.level_combo.currentTextChanged.connect(self.select_level)
        self.count_spin.valueChanged.connect(self.select_count)

        if skills:
            self.belong_combo.set_items(list(skills))
        if skill:
            self.belong_combo.setCurrentText(skill.belong)
            self.id_combo.setCurrentText(str(skill.skill_id))
            self.level_combo.setCurrentText(str(skill.skill_level))
            self.count_spin.setValue(skill.count)

    def select_belong(self, belong: str):
        if belong not in self.skills:
            return
        self.id_combo.set_items([str(skill_id) for skill_id in self.skills[belong]])

    def select_id(self, skill_id: str):
        if not skill_id:
            return
        belong = self.belong_combo.currentText()
        skill_id = int(skill_id)
        self.level_combo.set_items([str(level) for level in self.skills[belong][skill_id]])

    def select_level(self, skill_level: str):
        if not skill_level:
            return
        belong = self.belong_combo.currentText()
        skill_id = int(self.id_combo.currentText())
        skill_level = int(skill_level)
        self.skill = Skill(belong, skill_id, skill_level, **self.skills[belong][skill_id][skill_level])

        self.name_label.setText(self.skill.name)
        self.comment_label.setText(self.skill.comment)

    def select_count(self, count: int):
        if not self.skill:
            return
        self.skill.count = count


class SkillDamageDialog(QDialog):

    def __init__(
            self, skill: Skill, attribute: Attribute, parent: QWidget = None
    ):
        super().__init__(parent)
        self.setWindowTitle("Damage Detail")

        layout = QVBoxLayout(self)

        variables = {
            "rand": 0.5, "damage": Variable("damage"), **attribute.current, **attribute.snapshot
        }
        self.damage = skill.damage.evaluate(variables) * skill.count
        self.critical_damage = skill.critical_damage.evaluate(variables)
        self.critical_strike = skill.critical_strike.evaluate(variables)

        layout.addWidget(LabelRow("Name:", QLabel(skill.name)))
        layout.addWidget(LabelRow("Skill ID:", QLabel(str(skill.skill_id))))
        layout.addWidget(LabelRow("Skill Level:", QLabel(str(skill.skill_level))))
        layout.addWidget(LabelRow("Count:", QLabel(str(skill.count))))
        self.target_level = ComboBox()
        layout.addWidget(LabelRow("Target Level:", self.target_level))
        layout.addWidget(LabelRow("Critical Strike:", QLabel(f"{round(self.critical_strike * 100, 2)}%")))
        self.damage_label = QLabel("")
        layout.addWidget(LabelRow("Hit Damage:", self.damage_label))
        self.critical_damage_label = QLabel("")
        layout.addWidget(LabelRow("Critical Damage:", self.critical_damage_label))
        self.expected_damage_label = QLabel("")
        layout.addWidget(LabelRow("Expected Damage:", self.expected_damage_label))

        self.target_level.currentTextChanged.connect(self.select_target_level)
        self.target_level.set_items(SHIELD_BASE_MAP)

    def select_target_level(self, level):
        if not level:
            return
        level = int(level)
        damage = int(self.damage.evaluate({"target_level": level, "shield_base": SHIELD_BASE_MAP[level]}))
        self.damage_label.setText(str(damage))
        critical_damage = int(self.critical_damage.evaluate({"damage": damage}))
        self.critical_damage_label.setText(str(critical_damage))
        expected_damage = int(damage * (1 - self.critical_strike) + critical_damage * self.critical_strike)
        self.expected_damage_label.setText(str(expected_damage))
