from PySide6.QtWidgets import QDialog, QWidget, QVBoxLayout, QSpinBox, QHBoxLayout, QPushButton

from base.skill import Skill
from qt import ComboBox, LabelRow


class SkillEditorDialog(QDialog):
    skill: Skill = None

    def __init__(self, items: list = None, value: Skill = None, parent: QWidget = None):
        super().__init__(parent)
        self.setWindowTitle("Edit Skill")
        layout = QVBoxLayout(self)

        self.id_combo = ComboBox()
        self.level_combo = ComboBox()
        self.count_spin = QSpinBox(minimum=1, value=1)
        self.count_row = LabelRow("Count:", self.count_spin)

        layout.addWidget(LabelRow("ID:", self.id_combo))
        layout.addWidget(LabelRow("Level:", self.level_combo))
        layout.addWidget(self.count_row)

        layout.addLayout((btn_layout := QHBoxLayout()))
        btn_layout.addWidget((ok_button := QPushButton("OK")))
        btn_layout.addWidget((cancel_button := QPushButton("Cancel")))

        ok_button.clicked.connect(self.accept)
        cancel_button.clicked.connect(self.reject)
        self.id_combo.currentTextChanged.connect(self.select_id)
        self.level_combo.currentTextChanged.connect(self.select_level)
        self.count_spin.valueChanged.connect(self.select_count)

        if items:
            self.id_combo.set_items(items, -1)
            self.id_combo.setCurrentIndex(-1)
        if value:
            self.id_combo.setCurrentText(str(value.id))
            self.level_combo.setCurrentText(str(value.level))
            self.count_spin.setValue(value.count)

    def select_id(self, skill_id: str):
        if not skill_id:
            return
        self.skill = Skill(int(skill_id))
        self.level_combo.set_items([str(level + 1) for level in range(self.skill.max_level)])

    def select_level(self, level: str):
        if not self.skill or not level:
            return
        self.skill.level = int(level)

    def select_count(self, count: int):
        if not self.skill:
            return
        self.skill.count = count