import json

from PySide6.QtWidgets import QTabWidget

from qt.classes.gear import Gears
from qt.classes.section import Section
from qt.component.top_widget.widget import TopWidget
from qt.script.gear import GearScript
from qt.script.loop import LoopScript


class TopScript:
    def __init__(self, widget: TopWidget, tabs: QTabWidget, loop_script: LoopScript, gear_script: GearScript):
        self.widget = widget
        self.tabs = tabs
        self.loop_script = loop_script
        self.gear_script = gear_script

        self.connect()

    def connect(self):
        self.widget.kungfu_combo.currentTextChanged.connect(self.select_kungfu)
        self.widget.save_btn.clicked.connect(self.save)
        self.widget.load_btn.clicked.connect(self.load)

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

    def save(self):
        json.dump(
            self.widget.cache_content, open("cache.json", "w", encoding="utf-8"),
            ensure_ascii=False, default=lambda x: x.to_dict()
        )

    def load(self):
        for k, v in json.load(open("cache.json", "r", encoding="utf-8")).items():
            self.widget.cache_content[k] = dict(
                loop=[Section.from_dict(self.widget.kungfu.kungfu_id, e) for e in v["loop"]],
                gear=Gears.from_dict(v["gear"]),
            )
        self.select_kungfu(self.widget.kungfu.kungfu_id)
