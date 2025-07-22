from PySide6.QtWidgets import QDialog, QWidget, QVBoxLayout, QPushButton, QSpinBox, QHBoxLayout

from base.dot import Dot
from base.skill import Skill
from qt import ComboBox, LabelRow
from qt.component.skill_editor import SkillEditorDialog


class SourceSkillEditorDialog(SkillEditorDialog):
    def __init__(self, max_stack: int, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.count_row.set_label("Stack:")
        self.count_spin.setMaximum(max_stack)


class ConsumeSkillEditorDialog(SkillEditorDialog):
    def __init__(self, max_tick: int, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.count_row.set_label("Tick:")
        self.count_spin.setMaximum(max_tick)


class DotEditorDialog(QDialog):
    dot: Dot = None

    def __init__(self, items: list = None, value: Dot = None, parent: QWidget = None):
        super().__init__(parent)
        self.setWindowTitle("Edit Dot")
        layout = QVBoxLayout(self)

        self.id_combo = ComboBox()
        self.level_combo = ComboBox()
        self.source_button = QPushButton("")
        self.consume_button = QPushButton("")
        self.count_spin = QSpinBox(minimum=1, value=1)

        layout.addWidget(LabelRow("ID:", self.id_combo))
        layout.addWidget(LabelRow("Level:", self.level_combo))
        layout.addWidget(LabelRow("Source:", self.source_button))
        self.consume_row = LabelRow("Consume:", self.consume_button)
        layout.addWidget(self.consume_row)
        layout.addWidget(LabelRow("Count:", self.count_spin))

        layout.addLayout((btn_layout := QHBoxLayout()))
        btn_layout.addWidget((ok_button := QPushButton("OK")))
        btn_layout.addWidget((cancel_button := QPushButton("Cancel")))

        ok_button.clicked.connect(self.accept)
        cancel_button.clicked.connect(self.reject)
        self.id_combo.currentTextChanged.connect(self.select_id)
        self.level_combo.currentTextChanged.connect(self.select_level)
        self.source_button.clicked.connect(self.select_source)
        self.consume_button.clicked.connect(self.select_consume)
        self.count_spin.valueChanged.connect(self.select_count)

        if items:
            self.id_combo.set_items(items, -1)
        if value:
            self.id_combo.setCurrentText(str(value.id))
            self.level_combo.setCurrentText(str(value.level))
            self.dot.source = Skill(value.source.id, value.source.level, value.source.count)
            self.source_button.setText(str(self.dot.source))
            self.dot.consume = Skill(value.consume.id, value.consume.level, value.consume.count)
            self.consume_button.setText(str(self.dot.consume))
            self.count_spin.setValue(value.count)

    def select_id(self, dot_id: str):
        if not dot_id:
            return
        self.dot = Dot(int(dot_id))
        self.level_combo.set_items([str(level + 1) for level in range(self.dot.max_level)])
        self.source_button.setText("Select")
        if self.dot.consume_list:
            self.consume_row.show()
            self.consume_button.setText("Select")
        else:
            self.consume_row.hide()

    def select_level(self, level: str):
        if not self.dot or not level:
            return
        self.dot.level = int(level)

    def select_source(self):
        if not self.dot:
            return
        dialog = SourceSkillEditorDialog(max_stack=3, items=self.dot.source_list, parent=self)
        if dialog.exec() == QDialog.DialogCode.Accepted and (skill := dialog.skill):
            self.dot.source = skill
            self.source_button.setText(str(skill))

    def select_consume(self):
        if not self.dot:
            return
        dialog = ConsumeSkillEditorDialog(max_tick=5, items=self.dot.consume_list, parent=self)
        if dialog.exec() == QDialog.DialogCode.Accepted and (skill := dialog.skill):
            self.dot.consume = skill
            self.consume_button.setText(str(skill))

    def select_count(self, count: int):
        if not self.dot:
            return
        self.dot.count = count
