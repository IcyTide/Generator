from PySide6.QtWidgets import QDialog, QDoubleSpinBox, QHBoxLayout, QLabel, QPushButton, QVBoxLayout, QWidget

from base.constant import LEVEL_VARIABLES, SHIELD_BASE_MAP
from qt import ComboBox, LabelRow
from qt.classes.attribute import Attribute
from qt.classes.skill import Skill
from qt.component.loop_widget.widget import LoopWidget
from qt.utils import evaluate_skill


class SkillEditorDialog(QDialog):
    skills: dict[str, dict[int, dict[int, dict]]] = {}
    skill: Skill = None

    def __init__(self, skills: dict = None, skill: Skill = None, parent: LoopWidget = None):
        super().__init__(parent)
        self.setWindowTitle("编辑技能伤害")
        layout = QVBoxLayout(self)
        self.skills = skills
        self.belong_combo = ComboBox()
        self.id_combo = ComboBox()
        self.level_combo = ComboBox()
        self.count_spin = QDoubleSpinBox(minimum=0.01, value=1, singleStep=1)
        self.count_row = LabelRow("数量:", self.count_spin)

        layout.addWidget(LabelRow("类别:", self.belong_combo))
        layout.addWidget(LabelRow("ID:", self.id_combo))
        layout.addWidget(LabelRow("等级:", self.level_combo))
        layout.addWidget(self.count_row)

        self.name_label = QLabel("")
        self.comment_label = QLabel("")
        layout.addWidget(LabelRow("名称:", self.name_label))
        layout.addWidget(LabelRow("注释:", self.comment_label))

        layout.addLayout((btn_layout := QHBoxLayout()))
        btn_layout.addWidget((ok_button := QPushButton("确定")))
        btn_layout.addWidget((cancel_button := QPushButton("取消")))

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
        count = self.count_spin.value()
        count = int(count) if int(count) == count else count
        self.skill = Skill(belong, skill_id, skill_level, count, **self.skills[belong][skill_id][skill_level])

        self.name_label.setText(self.skill.name)
        self.comment_label.setText(self.skill.comment)

    def select_count(self, count: float):
        if not self.skill:
            return
        count = int(count) if int(count) == count else count
        self.skill.count = count


class SkillDamageDialog(QDialog):

    def __init__(
            self, skill: Skill, attribute: Attribute, parent: QWidget = None
    ):
        super().__init__(parent)
        self.setWindowTitle("技能伤害细节")

        layout = QVBoxLayout(self)

        variables = {**attribute.current, **attribute.snapshot}
        self.damage, self.critical_strike, self.critical_damage, self.expected_damage = evaluate_skill(skill, variables)

        layout.addWidget(LabelRow("名称:", QLabel(skill.name)))
        layout.addWidget(LabelRow("ID:", QLabel(str(skill.skill_id))))
        layout.addWidget(LabelRow("等级:", QLabel(str(skill.skill_level))))
        layout.addWidget(LabelRow("数量:", QLabel(str(skill.count))))
        self.target_level = ComboBox()
        layout.addWidget(LabelRow("目标等级:", self.target_level))
        self.critical_strike_label = QLabel("")
        layout.addWidget(LabelRow("期望会心:", self.critical_strike_label))
        self.damage_label = QLabel("")
        layout.addWidget(LabelRow("命中伤害:", self.damage_label))
        self.critical_damage_label = QLabel("")
        layout.addWidget(LabelRow("会心伤害:", self.critical_damage_label))
        self.expected_damage_label = QLabel("")
        layout.addWidget(LabelRow("期望伤害:", self.expected_damage_label))

        self.target_level.currentTextChanged.connect(self.select_target_level)
        self.target_level.set_items(SHIELD_BASE_MAP)

    def select_target_level(self, level):
        if not level:
            return
        level = int(level)
        variables = LEVEL_VARIABLES(level)
        critical_strike = self.critical_strike.evaluate(variables)
        self.critical_strike_label.setText(f"{round(critical_strike * 100, 2)}%")
        damage = int(self.damage.evaluate(variables))
        self.damage_label.setText(str(damage))
        critical_damage = int(self.critical_damage.evaluate(variables))
        self.critical_damage_label.setText(str(critical_damage))
        expected_damage = int(self.expected_damage.evaluate(variables))
        self.expected_damage_label.setText(str(expected_damage))
