from PySide6.QtWidgets import QDialog, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QSpinBox, QLineEdit

from base.record import Record
from qt import LabelRow


class RecordEditorDialog(QDialog):
    record: Record = None

    def __init__(self, value: Record = None, parent: QWidget = None):
        super().__init__(parent)
        self.setWindowTitle("Edit Record")
        layout = QVBoxLayout(self)

        if value:
            self.record = Record(value.name, value.count)
        else:
            self.record = Record()
        self.name_edit = QLineEdit(self.record.name)
        self.count_spin = QSpinBox(minimum=1, value=self.record.count)

        layout.addWidget(LabelRow("Name:", self.name_edit))
        layout.addWidget(LabelRow("Count:", self.count_spin))

        layout.addLayout((btn_layout := QHBoxLayout()))
        btn_layout.addWidget((ok_button := QPushButton("OK")))
        btn_layout.addWidget((cancel_button := QPushButton("Cancel")))

        ok_button.clicked.connect(self.accept)
        cancel_button.clicked.connect(self.reject)
        self.name_edit.textChanged.connect(self.edit_name)
        self.count_spin.valueChanged.connect(self.select_count)

    def edit_name(self, name: str):
        if name := name.strip():
            self.record.name = name

    def select_count(self, count: int):
        self.record.count = count
