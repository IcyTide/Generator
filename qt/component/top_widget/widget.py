from PySide6.QtWidgets import QHBoxLayout, QPushButton, QWidget

from qt import ComboBox


class TopWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setLayout(layout := QHBoxLayout())
        self.kungfu_combo = ComboBox()
        layout.addWidget(self.kungfu_combo, 2)

        self.load_btn = QPushButton("加载配置")
        layout.addWidget(self.load_btn, 1)
        self.save_btn = QPushButton("保存配置")
        layout.addWidget(self.save_btn, 1)
        # self.attribute_btn = QPushButton("Attributes")
        # layout.addWidget(self.attribute_btn)
