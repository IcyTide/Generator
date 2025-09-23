from PySide6.QtWidgets import QHBoxLayout, QPushButton, QWidget

from kungfus import DisplayKungfu, SUPPORT_KUNGFUS
from qt import ComboBox


class TopWidget(QWidget):

    def __init__(self):
        super().__init__()
        self.kungfus = {str(kungfu.kungfu_id): DisplayKungfu(kungfu) for kungfu in SUPPORT_KUNGFUS}
        self.cache_content = {}
        self.setLayout(layout := QHBoxLayout())
        self.combo = ComboBox()
        layout.addWidget(self.combo, 2)
        self.combo.set_items(list(self.kungfus), -1)

        self.load_button = QPushButton("Load")
        layout.addWidget(self.load_button, 1)
        self.save_button = QPushButton("Save")
        layout.addWidget(self.save_button, 1)
