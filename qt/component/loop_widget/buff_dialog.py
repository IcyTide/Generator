from PySide6.QtWidgets import QDialog, QDoubleSpinBox, QHBoxLayout, QLabel, QPushButton, QVBoxLayout, QWidget

from qt import ComboBox, LabelRow
from qt.classes.buff import Buff, BuffType


class BuffEditorDialog(QDialog):
    buffs: dict[str, dict[int, dict[int, dict]]] = {}
    buff: Buff = None

    def __init__(self, buffs: dict = None, buff: Buff = None, parent: QWidget = None):
        super().__init__(parent)
        self.setWindowTitle("编辑增益")
        layout = QVBoxLayout(self)
        self.buffs = buffs
        self.belong_combo = ComboBox()
        self.id_combo = ComboBox()
        self.level_combo = ComboBox()
        self.stack_spin = QDoubleSpinBox(minimum=1, value=1, singleStep=1)
        self.type_combo = ComboBox()
        self.type_combo.set_items([str(e) for e in BuffType])

        layout.addWidget(LabelRow("类别:", self.belong_combo))
        layout.addWidget(LabelRow("ID:", self.id_combo))
        layout.addWidget(LabelRow("等级:", self.level_combo))
        layout.addWidget(LabelRow("层数:", self.stack_spin))
        layout.addWidget(LabelRow("类型:", self.type_combo))

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
        self.stack_spin.valueChanged.connect(self.select_stack)
        self.type_combo.currentTextChanged.connect(self.select_type)

        if buffs:
            self.belong_combo.set_items(list(buffs))
        if buff:
            self.belong_combo.setCurrentText(buff.belong)
            self.id_combo.setCurrentText(str(buff.buff_id))
            self.level_combo.setCurrentText(str(buff.buff_level))
            self.stack_spin.setValue(buff.stack)
            self.type_combo.setCurrentText(str(buff.buff_type))

    def select_belong(self, belong: str):
        if belong not in self.buffs:
            return
        self.id_combo.set_items(list(self.buffs[belong]))

    def select_id(self, buff_id: str):
        if not buff_id:
            return
        belong = self.belong_combo.currentText()
        buff_id = int(buff_id)
        self.level_combo.set_items(list(self.buffs[belong][buff_id]))

    def select_level(self, buff_level: str):
        if not buff_level:
            return
        belong = self.belong_combo.currentText()
        buff_id = int(self.id_combo.currentText())
        buff_level = int(buff_level)
        buff_type = self.type_combo.currentText()
        stack = self.stack_spin.value()
        stack = int(stack) if int(stack) == stack else stack

        self.buff = Buff(belong, buff_id, buff_level, buff_type, **self.buffs[belong][buff_id][buff_level])
        self.buff.stack = min(stack, self.buff.max_stack)

        self.stack_spin.setMaximum(self.buff.max_stack)
        self.stack_spin.setValue(self.buff.stack)
        self.name_label.setText(self.buff.name)
        self.comment_label.setText(self.buff.comment)

    def select_stack(self, stack: float):
        if not self.buff or not stack:
            return
        stack = int(stack) if int(stack) == stack else stack
        self.buff.stack = stack

    def select_type(self, buff_type: str):
        if not self.buff:
            return
        self.buff.buff_type = BuffType(buff_type)
