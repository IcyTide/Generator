import json

from PySide6.QtWidgets import QFileDialog, QTabWidget

from kungfus import SUPPORT_KUNGFUS
from qt.classes.gains.consumable import Consumables
from qt.classes.gains.formation import Formation
from qt.classes.gear import Gears
from qt.classes.kungfu import Kungfu
from qt.classes.recipe import Recipes
from qt.classes.section import Sections
from qt.classes.talent import Talents
from qt.component.top_widget.widget import TopWidget
from qt.script.bonus import BonusScript
from qt.script.build import BuildScript
from qt.script.gear import GearScript
from qt.script.loop import LoopScript


class TopScript:
    kungfu: Kungfu

    def __init__(
            self, widget: TopWidget, tabs: QTabWidget,
            loop_script: LoopScript, gear_script: GearScript, build_script: BuildScript, bonus_script: BonusScript
    ):

        self.widget = widget
        self.tabs = tabs

        self.kungfus = {}
        for kungfu in SUPPORT_KUNGFUS:
            kungfu = Kungfu(kungfu)
            self.kungfus[kungfu.name] = kungfu

        self.cache_content = {}
        self.loop_script = loop_script
        self.gear_script = gear_script
        self.build_script = build_script
        self.bonus_script = bonus_script

        self.connect()

    def connect(self):
        self.widget.kungfu_combo.set_items(self.kungfus, -1)
        self.widget.kungfu_combo.currentTextChanged.connect(self.select_kungfu)
        self.widget.save_btn.clicked.connect(self.save)
        self.widget.load_btn.clicked.connect(self.load)

    def select_kungfu(self, kungfu):
        if kungfu not in self.kungfus:
            return
        self.kungfu = self.kungfus[kungfu]
        if kungfu not in self.cache_content:
            self.cache_content[kungfu] = dict(
                gear=self.gear_script.init(self.kungfu),
                loop=self.loop_script.init(self.kungfu),
                **self.build_script.init(self.kungfu),
                **self.bonus_script.init(self.kungfu)
            )
        else:
            cache = self.cache_content[kungfu]
            cache["gear"] = self.gear_script.init(self.kungfu, cache["gear"])
            cache["loop"] = self.loop_script.init(self.kungfu, cache["loop"])
            build = self.build_script.init(self.kungfu, cache["talents"], cache["recipes"])
            cache["talents"], cache["recipes"] = build["talents"], build["recipes"]
            bonus = self.bonus_script.init(self.kungfu, cache["consumables"], cache["formation"])
            cache["consumables"], cache["formation"] = bonus["consumables"], bonus["formation"]
        self.tabs.show()
        self.widget.window().showMaximized()
        self.widget.load_btn.hide()
        self.widget.save_btn.show()

    def save(self):
        file_path, _ = QFileDialog.getSaveFileName(
            self.widget,
            "Save Cache",
            "cache.json",
            "JSON(*.json)"
        )
        if not file_path:
            return
        json.dump(
            self.cache_content, open(file_path, "w", encoding="utf-8"),
            ensure_ascii=False, default=lambda x: x.to_dict()
        )

    def load(self):
        file_path, _ = QFileDialog.getOpenFileName(
            self.widget,
            "Load Cache",
            "",
            "JSON(*.json)"
        )
        if not file_path:
            return
        for k, v in json.load(open(file_path, "r", encoding="utf-8")).items():
            kungfu = self.kungfus[k]
            self.cache_content[k] = dict(
                gear=Gears.from_dict(v["gear"]),
                loop=Sections.from_dict(kungfu.kungfu_id, v["loop"]),
                talents=Talents.from_dict(kungfu.kungfu_id, v["talents"]),
                recipes=Recipes.from_dict(kungfu.kungfu_id, v["recipes"]),
                consumables=Consumables.from_dict({}),
                formation=Formation.from_dict({})
            )
