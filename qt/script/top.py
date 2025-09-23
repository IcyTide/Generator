from PySide6.QtWidgets import QTabWidget

from qt.component.loop_widget.widget import LoopWidget
from qt.component.top_widget.widget import TopWidget

def top_script(self: TopWidget, tabs: QTabWidget, loop_widget: LoopWidget):
    def select_kungfu(kungfu_id):
        if kungfu_id not in self.kungfus:
            return
        loop_widget.kungfu = self.kungfus[kungfu_id]
        if kungfu_id not in self.cache_content:
            self.cache_content[kungfu_id] = dict(
                loop=loop_widget.init_loop()
            )
        else:
            loop_widget.init_loop(self.cache_content[kungfu_id]["loop"])
        tabs.show()

    self.combo.currentTextChanged.connect(select_kungfu)
