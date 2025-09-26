from PySide6.QtWidgets import QTabWidget

from qt.component.top_widget.widget import TopWidget
from qt.script.gear import GearScript
from qt.script.loop import LoopScript


class TopScript:
    def __init__(self, widget: TopWidget, tabs: QTabWidget, loop_script: LoopScript, gear_script: GearScript):
        self.widget = widget
        self.tabs = tabs
        self.loop_script = loop_script
        self.gear_script = gear_script

        self.widget.kungfu_combo.currentTextChanged.connect(self.select_kungfu)

    def select_kungfu(self, kungfu_id):
        if kungfu_id not in self.widget.kungfus:
            return
        kungfu = self.widget.kungfu = self.widget.kungfus[kungfu_id]
        self.loop_script.widget.kungfu = self.gear_script.widget.kungfu = kungfu
        if kungfu_id not in self.widget.cache_content:
            self.widget.cache_content[kungfu_id] = dict(
                loop=self.loop_script.init(),
                gear=self.gear_script.init(),
            )
        else:
            self.loop_script.init(self.widget.cache_content[kungfu_id]["loop"])
            self.gear_script.init(self.widget.cache_content[kungfu_id]["gear"])
        self.tabs.show()
