from PySide6.QtWidgets import QHBoxLayout, QPushButton, QWidget

from kungfus import SUPPORT_KUNGFUS

from qt import ComboBox
from qt.classes.kungfu import DisplayKungfu


class TopWidget(QWidget):
    kungfu: DisplayKungfu

    def __init__(self):
        super().__init__()
        self.kungfus = {str(kungfu.kungfu_id): DisplayKungfu(kungfu) for kungfu in SUPPORT_KUNGFUS}
        self.cache_content = {}
        self.setLayout(layout := QHBoxLayout())
        self.kungfu_combo = ComboBox()
        layout.addWidget(self.kungfu_combo, 2)
        self.kungfu_combo.set_items(list(self.kungfus), -1)

        self.load_btn = QPushButton("Load")
        layout.addWidget(self.load_btn, 1)
        self.save_btn = QPushButton("Save")
        layout.addWidget(self.save_btn, 1)
