from PySide6.QtWidgets import QDialog, QHBoxLayout, QLabel, QPushButton, QVBoxLayout, QWidget

from base.buff import Buff, BuffType
from qt import ComboBox, LabelRow


class BuffEditorDialog(QDialog):
    buffs: dict[str, dict[int, dict[int, dict]]] = {}
    buff: Buff = None

    def __init__(self, buffs: dict = None, buff: Buff = None, parent: QWidget = None):
        super().__init__(parent)
        self.setWindowTitle("Edit Buff")
        layout = QVBoxLayout(self)

        self.buffs = buffs
        self.belong_combo = ComboBox()
        self.id_combo = ComboBox()
        self.level_combo = ComboBox()
        self.stack_combo = ComboBox()
        self.type_combo = ComboBox()
        self.type_combo.set_items([str(e) for e in BuffType])

        layout.addWidget(LabelRow("Belong:", self.belong_combo))
        layout.addWidget(LabelRow("ID:", self.id_combo))
        layout.addWidget(LabelRow("Level:", self.level_combo))
        layout.addWidget(LabelRow("Stack:", self.stack_combo))
        layout.addWidget(LabelRow("Type:", self.type_combo))

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
        self.stack_combo.currentTextChanged.connect(self.select_stack)
        self.type_combo.currentTextChanged.connect(self.select_type)

        if buffs:
            self.belong_combo.set_items(list(buffs))
        if buff:
            self.belong_combo.setCurrentText(buff.belong)
            self.id_combo.setCurrentText(str(buff.buff_id))
            self.level_combo.setCurrentText(str(buff.buff_level))
            self.stack_combo.setCurrentText(str(buff.stack))
            self.type_combo.setCurrentText(str(buff.buff_type))

    def select_belong(self, belong: str):
        if belong not in self.buffs:
            return
        self.id_combo.set_items([str(buff_id) for buff_id in self.buffs[belong]])

    def select_id(self, buff_id: str):
        if not buff_id:
            return
        belong = self.belong_combo.currentText()
        buff_id = int(buff_id)
        self.level_combo.set_items([str(level) for level in self.buffs[belong][buff_id]])

    def select_level(self, buff_level: str):
        if not buff_level:
            return
        belong = self.belong_combo.currentText()
        buff_id = int(self.id_combo.currentText())
        buff_level = int(buff_level)
        buff_type = self.type_combo.currentText()
        self.buff = Buff(belong, buff_id, buff_level, buff_type, **self.buffs[belong][buff_id][buff_level])

        self.stack_combo.set_items([str(i + 1) for i in range(self.buff.max_stack)])
        self.name_label.setText(self.buff.name)
        self.comment_label.setText(self.buff.comment)

    def select_stack(self, stack: str):
        if not self.buff or not stack:
            return
        self.buff.stack = int(stack)

    def select_type(self, buff_type: str):
        if not self.buff:
            return
        self.buff.type = BuffType(buff_type)
