from PySide6.QtWidgets import QDialog

from qt.classes.gear import Enchant, Gear, Gears
from qt.classes.kungfu import Kungfu
from qt.component.gear_widget.detail_dialog import DetailDialog
from qt.component.gear_widget.stone_dialog import StoneDialog
from qt.component.gear_widget.widget import GearWidget, SubGearWidget
from qt.component.top_widget.attribute_dialog import AttributeDialog


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
        self.widget.strength_combo.currentTextChanged.connect(self.select_strength)
        for i, embed_combo in enumerate(self.widget.embed_combos):
            embed_combo.currentTextChanged.connect(self.select_embed(i))
        self.widget.detail_btn.clicked.connect(self.show_detail)

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
            self.parent.gears.pop(self.widget.position)
            self.gear = None
            self.parent.update_kungfu()
            return
        detail = self.widget.equip_data[school][kind][equipment]
        gear = self.gear = self.parent.gears[self.widget.position] = Gear(school, kind, equipment, detail)

        enchant = self.widget.enchant_combo.currentText()
        if enchant_detail := self.widget.enchant_data.get(enchant):
            gear.enchant = Enchant(enchant, enchant_detail)

        strength_level = self.widget.strength_combo.currentText()
        if strength_level and int(strength_level) <= gear.max_strength:
            gear.strength_level = int(strength_level)
        else:
            self.widget.strength_combo.set_items(range(gear.max_strength + 1), gear.max_strength)
            gear.strength_level = gear.max_strength

        embed_levels = {}
        for embed_attr, embed_combo in zip(gear.embed, self.widget.embed_combos):
            embed_level = embed_combo.currentText()
            embed_levels[len(embed_levels)] = int(embed_level)
        gear.embed_levels = embed_levels
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
            self.widget.strength_combo.setCurrentText(str(gear.strength_level))
            for i, embed_attr in enumerate(gear.embed):
                self.widget.embed_combos[i].setCurrentText(str(gear.embed_levels[i]))
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
            self.sub_scripts[sub_widget.position] = SubGearScript(sub_widget, self)
        self.connect()

    def connect(self):
        self.widget.stone_btn.clicked.connect(self.select_stone)
        self.widget.strength_combo.currentTextChanged.connect(self.select_strength)
        self.widget.embed_combo.currentTextChanged.connect(self.select_embed)
        self.widget.detail_btn.clicked.connect(self.show_detail)

    def select_stone(self):
        dialog = StoneDialog(self.gears.stone, parent=self.widget)
        if dialog.exec() == QDialog.DialogCode.Accepted:
            self.gears.stone = dialog.stone

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
        attributes, recipes, gains = self.gears.attributes
        if attributes:
            AttributeDialog(attributes, recipes, gains, parent=self.widget).exec()

    def init(self, kungfu: Kungfu, gears: Gears = None):
        self.kungfu = kungfu
        if not gears:
            self.gears = Gears()
        else:
            self.gears = gears
        for position, sub_script in self.sub_scripts.items():
            sub_script.init(self.gears.get(position))
        return self.gears

    def update_kungfu(self):
        attributes, recipes, gains = self.gears.attributes
        self.kungfu.gear_attributes = attributes
        self.kungfu.gear_recipes = recipes
        self.kungfu.gear_gains = gains