import json

from PySide6.QtWidgets import QDialog, QFileDialog, QTabWidget

from kungfus import SUPPORT_KUNGFUS
from qt.classes.kungfu import Kungfu
from qt.component.top_widget.cache_dialog import CacheDialog
from qt.component.top_widget.widget import TopWidget
from qt.script.bonus import BonusScript
from qt.script.build import BuildScript
from qt.script.gear import GearScript
from qt.script.loop import LoopScript


class TopScript:
    kungfu: Kungfu = None

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

    def refresh_cache(self, kungfu):
        cache = self.cache_content[kungfu]
        cache["gear"] = self.gear_script.init(self.kungfu, cache.get("gear"))
        cache["loop"] = self.loop_script.init(self.kungfu, cache.get("loop"))
        build = self.build_script.init(self.kungfu, cache.get("talents"), cache.get("recipes"))
        cache["talents"], cache["recipes"] = build["talents"], build["recipes"]
        bonus = self.bonus_script.init(
            self.kungfu, cache.get("consumables"), cache.get("formation"), cache.get("team_gains")
        )
        for k, v in bonus.items():
            cache[k] = v

    def select_kungfu(self, kungfu):
        if kungfu not in self.kungfus:
            return
        self.kungfu = self.kungfus[kungfu]

        if kungfu not in self.cache_content:
            self.cache_content[kungfu] = {}
        self.refresh_cache(kungfu)

        self.tabs.show()
        self.widget.window().showMaximized()
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
        dialog = CacheDialog(self.cache_content, parent=self.widget)
        if dialog.exec() == QDialog.DialogCode.Accepted:
            json.dump(
                dialog.need_content, open(file_path, "w", encoding="utf-8"),
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

        cache_content = json.load(open(file_path, "r", encoding="utf-8"))
        if not cache_content:
            return
        dialog = CacheDialog(cache_content, parent=self.widget)
        if dialog.exec() == QDialog.DialogCode.Accepted:
            for kungfu, content in dialog.need_content.items():
                self.cache_content[kungfu] = content
                if self.kungfu == self.kungfus[kungfu]:
                    self.refresh_cache(kungfu)
                if not self.kungfu:
                    self.widget.kungfu_combo.setCurrentText(kungfu)
