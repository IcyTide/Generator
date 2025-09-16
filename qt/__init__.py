from typing import List

from PySide6.QtWidgets import QComboBox, QHBoxLayout, QHeaderView, QLabel, QTableWidget, QWidget


class LabelRow(QWidget):
    def __init__(self, label: str, field: QWidget):
        super().__init__()
        layout = QHBoxLayout(self)
        self.label = QLabel(label)
        self.field = field
        layout.addWidget(self.label)
        layout.addWidget(self.field)

    def set_label(self, label):
        self.label.setText(label)


class ComboBox(QComboBox):
    def set_items(self, items, index=None):
        items = [str(item) for item in items]
        current_text = self.currentText()
        self.clear()
        self.addItems(items)
        if index is not None:
            self.setCurrentIndex(index)
        else:
            if current_text in items:
                self.setCurrentText(current_text)
            else:
                self.setCurrentText(items[0])


class Table(QTableWidget):
    def __init__(self, headers: List[str]):
        super().__init__(0, len(headers))
        self.setHorizontalHeaderLabels(headers)
        self.setSelectionBehavior(QTableWidget.SelectionBehavior.SelectRows)  # 整行选择
        self.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)  # 自动拉伸填充
        self.setEditTriggers(QTableWidget.EditTrigger.NoEditTriggers)  # 禁止自动编辑
        self.verticalHeader().setVisible(False)
