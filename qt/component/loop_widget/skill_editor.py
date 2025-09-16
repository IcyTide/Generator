from PySide6.QtWidgets import QDialog, QHBoxLayout, QLabel, QPushButton, QSpinBox, QVBoxLayout, QWidget

from base.skill import Skill
from qt import ComboBox, LabelRow


class SkillEditorDialog(QDialog):
    skills: dict[str, dict[int, dict[int, dict]]] = {}
    skill: Skill = None

    def __init__(self, skills: dict = None, skill: Skill = None, parent: QWidget = None):
        super().__init__(parent)
        self.setWindowTitle("Edit Skill")
        layout = QVBoxLayout(self)

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
