import sys

from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication, QMainWindow, QTabWidget, QVBoxLayout, QWidget

from qt.component.gear_widget.widget import GearWidget
from qt.component.loop_widget.widget import LoopWidget
from qt.component.top_widget.widget import TopWidget
from qt.script.gear import GearScript
from qt.script.loop import LoopScript
from qt.script.top import TopScript


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("")
        self.icon = QIcon("assets/icon.ico")
        self.setWindowIcon(self.icon)

        # 主体布局
        self.setCentralWidget(widget := QWidget(self))
        layout = QVBoxLayout(widget)
        self.top_widget = TopWidget()
        layout.addWidget(self.top_widget)
        self.tabs = QTabWidget()
        layout.addWidget(self.tabs)
        self.loop_widget = LoopWidget()
        self.gear_widget = GearWidget()
        self.tabs.addTab(self.gear_widget, "Gear")
        self.tabs.addTab(self.loop_widget, "Loop")
        self.tabs.hide()

        loop_script = LoopScript(self.loop_widget)
        gear_script = GearScript(self.gear_widget)
        # top_script(self.top_widget, self.tabs, loop_script, gear_script)
        self.top_script = TopScript(self.top_widget, self.tabs, loop_script, gear_script)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
