from PySide6.QtWidgets import QDialog, QHBoxLayout, QListWidget, QPushButton, QVBoxLayout, QWidget

from qt import ComboBox, LabelRow


class CacheDialog(QDialog):
    need_content: dict[str, dict]

    def __init__(self, content: dict[str, dict] = None, parent: QWidget = None):
        super().__init__(parent)
        self.setWindowTitle("选择缓存项")
        layout = QVBoxLayout(self)

        self.cache_content = content
        self.need_content = content.copy()

        self.kungfu_combo = ComboBox()
        layout.addWidget(LabelRow("心法:", self.kungfu_combo))

        self.kungfu_combo.set_items(list(self.cache_content), -1)

        self.content_list = QListWidget()
        self.content_list.setSelectionMode(QListWidget.SelectionMode.MultiSelection)
        layout.addWidget(LabelRow("缓存项:", self.content_list))

        layout.addLayout((btn_layout := QHBoxLayout()))
        btn_layout.addWidget((ok_button := QPushButton("确定")))
        btn_layout.addWidget((cancel_button := QPushButton("取消")))

        ok_button.clicked.connect(self.accept)
        cancel_button.clicked.connect(self.reject)

        self.kungfu_combo.currentTextChanged.connect(self.select_kungfu)
        self.content_list.itemSelectionChanged.connect(self.select_content)
        self.kungfu_combo.setCurrentText(list(self.cache_content)[0])

    def select_kungfu(self, kungfu: str):
        if kungfu not in self.need_content:
            return

        need_contents = self.need_content[kungfu]
        self.content_list.clear()
        self.content_list.addItems(self.cache_content[kungfu])
        for i in range(self.content_list.count()):
            item = self.content_list.item(i)
            item.setSelected(item.text() in need_contents)

    def select_content(self):
        kungfu = self.kungfu_combo.currentText()
        if kungfu not in self.need_content:
            return
        selected_items = self.content_list.selectedItems()
        self.need_content[kungfu] = {}
        for item in selected_items:
            item = item.text()
            self.need_content[kungfu][item] = self.cache_content[kungfu][item]

