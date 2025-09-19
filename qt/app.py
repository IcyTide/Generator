import sys

from PySide6.QtGui import QIcon
from PySide6.QtWidgets import (QApplication, QComboBox, QMainWindow, QSizePolicy, QTabWidget, QVBoxLayout, QWidget)

from kungfus import DisplayKungfu, SUPPORT_KUNGFUS
from qt.component.loop_widget.widget import LoopWidget


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("")
        self.icon = QIcon("assets/icon.ico")
        self.setWindowIcon(self.icon)

        self.kungfus = {str(kungfu.kungfu_id): DisplayKungfu(kungfu) for kungfu in SUPPORT_KUNGFUS}
        # 主体布局
        self.setCentralWidget(widget := QWidget(self))
        layout = QVBoxLayout(widget)
        self.combo = QComboBox()
        layout.addWidget(self.combo)
        self.combo.addItems(list(self.kungfus))
        self.combo.setCurrentIndex(-1)
        self.tabs = QTabWidget()
        layout.addWidget(self.tabs)
        self.loop_widget = LoopWidget()
        self.tabs.addTab(self.loop_widget, "Loop")

        self.tabs.hide()
        self.combo.currentTextChanged.connect(self.select_kungfu)

    def select_kungfu(self, kungfu_id):
        if kungfu_id not in self.kungfus:
            return
        self.loop_widget.kungfu = self.kungfus[kungfu_id]
        self.setGeometry(100, 100, 1200, 800)
        self.tabs.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
