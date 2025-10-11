from PySide6.QtWidgets import QHBoxLayout, QPushButton, QWidget

from qt import ComboBox


class TopWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setLayout(layout := QHBoxLayout())
        self.kungfu_combo = ComboBox()
        layout.addWidget(self.kungfu_combo, 2)

        self.load_btn = QPushButton("Load")
        layout.addWidget(self.load_btn)
        self.save_btn = QPushButton("Save")
        layout.addWidget(self.save_btn)
        self.save_btn.hide()
        # self.attribute_btn = QPushButton("Attributes")
        # layout.addWidget(self.attribute_btn)
