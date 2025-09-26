from PySide6.QtWidgets import QDialog, QHBoxLayout, QLineEdit, QPushButton, QSpinBox, QVBoxLayout, QWidget

from qt.classes.section import Section
from qt import LabelRow


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
