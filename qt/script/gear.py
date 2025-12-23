from PySide6.QtWidgets import QDialog

from base.constant import SPECIAL_ENCHANT_MAP
from qt.classes.gear import Enchant, Gear, Gears
from qt.classes.kungfu import Kungfu
from qt.component.gear_widget.attribute_dialog import AttributeDialog
from qt.component.gear_widget.detail_dialog import DetailDialog
from qt.component.gear_widget.stone_dialog import StoneDialog
from qt.component.gear_widget.widget import GearWidget, SubGearWidget


class SubGearScript:
    gear: Gear | None

    def __init__(self, sub_gear_widget: SubGearWidget, gear_script: "GearScript"):
        self.widget = sub_gear_widget
        self.parent = gear_script

        self.connect()

    def connect(self):
        self.widget.school_combo.currentTextChanged.connect(self.select_school)
        self.widget.kind_combo.currentTextChanged.connect(self.select_kind)
        self.widget.equipment_combo.currentTextChanged.connect(self.select_equipment)
        self.widget.enchant_combo.currentTextChanged.connect(self.select_enchant)
        if self.widget.stone_btn:
            self.widget.stone_btn.clicked.connect(self.select_stone)
        if self.widget.special_enchant:
            self.widget.special_enchant.stateChanged.connect(self.select_special_enchant)
        self.widget.strength_combo.currentTextChanged.connect(self.select_strength)
        for i, embed_combo in enumerate(self.widget.embed_combos):
            embed_combo.currentTextChanged.connect(self.select_embed(i))
        self.widget.detail_btn.clicked.connect(self.show_detail)

    def get_special_enchant_gain(self):
        special_enchant = None
        kungfu_type = "tank" if self.gear.kind == "防御" else "dps"
        for level, gain in SPECIAL_ENCHANT_MAP[self.widget.position][kungfu_type].items():
            if self.gear.level >= level:
                special_enchant = gain
        return special_enchant

    def select_school(self, school):
        if school not in self.widget.equip_data:
            self.widget.kind_combo.clear()
            return
        kinds = list(self.widget.equip_data[school])
        self.widget.kind_combo.set_items(kinds, -1)
        if self.parent.kungfu.kind in kinds:
            self.widget.kind_combo.setCurrentText(self.parent.kungfu.kind)
        elif self.parent.kungfu.major in kinds:
            self.widget.kind_combo.setCurrentText(self.parent.kungfu.major)

    def select_kind(self, kind):
        school = self.widget.school_combo.currentText()
        if school not in self.widget.equip_data:
            return
        if kind not in self.widget.equip_data[school]:
            self.widget.equipment_combo.clear()
            return
        self.widget.equipment_combo.set_items([""] + list(self.widget.equip_data[school][kind]))

    def select_equipment(self, equipment):
        school, kind = self.widget.school_combo.currentText(), self.widget.kind_combo.currentText()
        if school not in self.widget.equip_data:
            return
        if kind not in self.widget.equip_data[school]:
            return
        if equipment not in self.widget.equip_data[school][kind]:
            self.parent.gears.pop(self.widget.label)
            self.gear = None
            self.parent.update_kungfu()
            return
        detail = self.widget.equip_data[school][kind][equipment]
        stone = self.gear.stone if self.gear else None
        gear = self.gear = self.parent.gears[self.widget.label] = Gear(school, kind, equipment, detail)
        gear.stone = stone

        enchant = self.widget.enchant_combo.currentText()
        if enchant_detail := self.widget.enchant_data.get(enchant):
            gear.enchant = Enchant(enchant, enchant_detail)

        if self.widget.special_enchant and self.widget.special_enchant.isChecked():
            gear.special_enchant = self.get_special_enchant_gain()

        strength_level = self.widget.strength_combo.currentText()
        self.widget.strength_combo.set_items(range(gear.max_strength + 1), gear.max_strength)
        if strength_level and int(strength_level) <= gear.max_strength:
            self.widget.strength_combo.setCurrentText(strength_level)
        else:
            self.widget.strength_combo.setCurrentText(str(gear.max_strength))

        embed_levels = {}
        for embed_attr, embed_combo in zip(gear.embed, self.widget.embed_combos):
            embed_level = embed_combo.currentText()
            embed_levels[len(embed_levels)] = int(embed_level)
        gear.embed_levels = embed_levels
        self.parent.update_kungfu()

    def select_special_enchant(self, state):
        if not self.gear:
            return
        special_enchant = self.get_special_enchant_gain()
        if state:
            self.gear.special_enchant = special_enchant
        else:
            self.gear.special_enchant = None
        self.parent.update_kungfu()

    def select_stone(self):
        if not self.gear:
            return
        dialog = StoneDialog(self.gear.stone, parent=self.parent.widget)
        if dialog.exec() == QDialog.DialogCode.Accepted:
            self.gear.stone = dialog.stone
            self.parent.update_kungfu()

    def select_enchant(self, enchant):
        if not self.gear:
            return
        if enchant not in self.widget.enchant_data:
            self.gear.enchant = None
            self.parent.update_kungfu()
            return
        self.gear.enchant = Enchant(enchant, self.widget.enchant_data[enchant])
        self.parent.update_kungfu()

    def select_strength(self, strength):
        if not self.gear:
            return
        self.gear.strength_level = int(strength)
        self.parent.update_kungfu()

    def select_embed(self, index):
        def inner(embed):
            if not self.gear:
                return
            self.gear.embed_levels[index] = int(embed)
            self.parent.update_kungfu()

        return inner

    def show_detail(self):
        if not self.gear:
            return
        DetailDialog(self.gear, parent=self.parent.widget).exec()

    def init(self, gear: Gear = None):
        if gear:
            self.gear = gear
            self.widget.school_combo.setCurrentText(gear.school)
            self.widget.kind_combo.setCurrentText(gear.kind)
            self.widget.equipment_combo.setCurrentText(gear.equipment)
            if gear.enchant:
                self.widget.enchant_combo.setCurrentText(gear.enchant.enchant)
            if gear.special_enchant:
                self.widget.special_enchant.setChecked(True)
            self.widget.strength_combo.setCurrentText(str(gear.strength_level))
            for i, embed_attr in enumerate(gear.embed):
                self.widget.embed_combos[i].setCurrentText(str(gear.embed_levels[i]))
            self.gear.stone = gear.stone
        else:
            self.gear = None
            if self.parent.kungfu.school in self.widget.equip_data:
                self.widget.school_combo.setCurrentText(self.parent.kungfu.school)
            else:
                self.widget.school_combo.setCurrentText("通用")
            self.widget.equipment_combo.setCurrentText("")
            self.widget.enchant_combo.setCurrentText("")


class GearScript:
    kungfu: Kungfu
    gears: Gears

    def __init__(self, gear_widget: GearWidget):
        self.widget = gear_widget
        self.sub_scripts: dict[str, SubGearScript] = {}
        for sub_widget in self.widget.sub_widgets.values():
            self.sub_scripts[sub_widget.label] = SubGearScript(sub_widget, self)
        self.connect()

    def connect(self):
        self.widget.special_enchant.stateChanged.connect(self.select_special_enchant)
        self.widget.strength_combo.currentTextChanged.connect(self.select_strength)
        self.widget.embed_combo.currentTextChanged.connect(self.select_embed)
        self.widget.detail_btn.clicked.connect(self.show_detail)

    def select_special_enchant(self, state):
        for sub_script in self.sub_scripts.values():
            if sub_script.gear and sub_script.widget.special_enchant:
                if state:
                    sub_script.widget.special_enchant.setChecked(True)
                else:
                    sub_script.widget.special_enchant.setChecked(False)

    def select_strength(self, strength):
        for sub_script in self.sub_scripts.values():
            if sub_script.gear:
                strength = min(int(strength), sub_script.gear.max_strength)
                sub_script.widget.strength_combo.setCurrentText(str(strength))

    def select_embed(self, embed):
        for sub_script in self.sub_scripts.values():
            if sub_script.gear:
                for embed_combo in sub_script.widget.embed_combos:
                    embed_combo.setCurrentText(str(embed))

    def show_detail(self):
        attributes, recipes, gains = self.kungfu.gear_attributes, self.kungfu.gear_recipes, self.kungfu.gear_gains
        if attributes:
            AttributeDialog(attributes, recipes, gains, parent=self.widget).exec()

    def init(self, kungfu: Kungfu, gears: Gears | dict = None):
        self.kungfu = kungfu
        if not gears:
            self.gears = Gears()
        elif isinstance(gears, Gears):
            self.gears = gears
        else:
            self.gears = Gears.from_dict(gears)
        for label, sub_script in self.sub_scripts.items():
            sub_script.init(self.gears.get(label))
        return self.gears

    def update_kungfu(self):
        attributes, recipes, gains = self.gears.content
        self.kungfu.gear_attributes = attributes
        self.kungfu.gear_recipes = recipes
        self.kungfu.gear_gains = gains
