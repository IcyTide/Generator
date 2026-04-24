from PySide6.QtCore import Qt
from PySide6.QtGui import QKeySequence, QShortcut
from PySide6.QtWidgets import QApplication, QComboBox, QHBoxLayout, QHeaderView, QLabel, QTableWidget, QTableWidgetItem, \
    QVBoxLayout, QWidget


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


class LabelColumn(QWidget):
    def __init__(self, label: str, field: QWidget):
        super().__init__()
        layout = QVBoxLayout(self)
        self.label = QLabel(label)
        self.field = field
        layout.addWidget(self.label)
        layout.addWidget(self.field)
        layout.setAlignment(Qt.AlignmentFlag.AlignTop)

    def set_label(self, label):
        self.label.setText(label)


class ComboBox(QComboBox):
    def set_items(self, items, index=None):
        items = [str(item) for item in items]
        current_text = self.currentText()
        self.blockSignals(True)
        self.clear()
        self.addItems(items)
        self.setCurrentIndex(-1)
        self.blockSignals(False)
        if index is not None:
            self.setCurrentIndex(index)
        else:
            if current_text in items:
                self.setCurrentText(current_text)
            elif items:
                self.setCurrentText(items[0])


class Table(QTableWidget):
    def __init__(self, headers: list[str]):
        super().__init__(0, len(headers))
        self.setHorizontalHeaderLabels(headers)
        self.setSelectionBehavior(QTableWidget.SelectionBehavior.SelectRows)  # 整行选择
        self.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)  # 自动拉伸填充
        self.setEditTriggers(QTableWidget.EditTrigger.NoEditTriggers)  # 禁止自动编辑
        self.verticalHeader().setVisible(False)

        copy_shortcut = QShortcut(QKeySequence.StandardKey.Copy, self)
        copy_shortcut.activated.connect(self.copy_selection)

    def refresh_table(self, data, index=False):
        self.setRowCount(0)
        for i, row in enumerate(data):
            self.insertRow(i)
            if index:
                self.setItem(i, 0, QTableWidgetItem(str(i + 1)))
            for j, data in enumerate(row):
                self.setItem(i, j + int(index), QTableWidgetItem(str(data)))

    def set_current_row(self, row):
        if row < 0:
            row += self.rowCount()
        self.setCurrentCell(row, 0)

    def copy_selection(self):
        selected = self.selectedRanges()
        if not selected:
            return

        text = ""
        for r in range(selected[0].topRow(), selected[0].bottomRow() + 1):
            row_data = []
            for c in range(selected[0].leftColumn(), selected[0].rightColumn() + 1):
                item = self.item(r, c)
                row_data.append(item.text() if item else "")
            text += "\t".join(row_data) + "\n"

        clipboard = QApplication.clipboard()
        clipboard.setText(text.strip())