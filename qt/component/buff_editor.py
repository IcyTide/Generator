from PySide6.QtWidgets import QDialog, QWidget, QVBoxLayout, QHBoxLayout, QPushButton

from base.buff import Buff, BuffType
from qt import ComboBox, LabelRow


class BuffEditorDialog(QDialog):
    buff: Buff = None

    def __init__(self, items: list = None, value: Buff = None, parent: QWidget = None):
        super().__init__(parent)
        self.setWindowTitle("Edit Buff")
        layout = QVBoxLayout(self)

        self.type_combo = ComboBox()
        self.type_combo.set_items([str(e) for e in BuffType])
        self.id_combo = ComboBox()
        self.level_combo = ComboBox()
        self.stack_combo = ComboBox()

        layout.addWidget(LabelRow("Type:", self.type_combo))
        layout.addWidget(LabelRow("ID:", self.id_combo))
        layout.addWidget(LabelRow("Level:", self.level_combo))
        layout.addWidget(LabelRow("Stack:", self.stack_combo))

        layout.addLayout((btn_layout := QHBoxLayout()))
        btn_layout.addWidget((ok_button := QPushButton("OK")))
        btn_layout.addWidget((cancel_button := QPushButton("Cancel")))

        ok_button.clicked.connect(self.accept)
        cancel_button.clicked.connect(self.reject)
        self.type_combo.currentTextChanged.connect(self.select_type)
        self.id_combo.currentTextChanged.connect(self.select_id)
        self.level_combo.currentTextChanged.connect(self.select_level)
        self.stack_combo.currentTextChanged.connect(self.select_stack)

        if items:
            self.id_combo.set_items(items, -1)
        if value:
            self.id_combo.setCurrentText(str(value.id))
            self.type_combo.setCurrentText(str(value.type))
            self.level_combo.setCurrentText(str(value.level))
            self.stack_combo.setCurrentText(str(value.stack))

    def select_type(self, buff_type: str):
        if not self.buff:
            return
        self.buff.type = BuffType(buff_type)

    def select_id(self, buff_id: str):
        if not buff_id:
            return
        self.buff = Buff(int(buff_id), type=BuffType(self.type_combo.currentText()))
        self.level_combo.set_items([str(level + 1) for level in range(self.buff.max_level)])
        self.stack_combo.set_items([str(stack + 1) for stack in range(self.buff.max_stack)])

    def select_level(self, level: str):
        if not self.buff or not level:
            return
        self.buff.level = int(level)

    def select_stack(self, stack: str):
        if not self.buff or not stack:
            return
        self.buff.stack = int(stack)