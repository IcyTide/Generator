from PySide6.QtWidgets import QDialog

from qt.classes.gear import Enchant, Gear
from qt.component.gear_widget.detail_dialog import DetailDialog
from qt.component.gear_widget.stone_dialog import StoneDialog
from qt.component.gear_widget.widget import GearWidget, SubGearWidget


class SubGearScript:
    def __init__(self, sub_gear_widget: SubGearWidget, gear_widget: GearWidget):
        self.widget = sub_gear_widget
        self.parent = gear_widget

        self.connect()

    def connect(self):
        self.widget.school_combo.currentTextChanged.connect(self.select_school)
        self.widget.kind_combo.currentTextChanged.connect(self.select_kind)
        self.widget.equipment_combo.currentTextChanged.connect(self.select_equipment)
        self.widget.enchant_combo.currentTextChanged.connect(self.select_enchant)
        self.widget.strength_combo.currentTextChanged.connect(self.select_strength)
        for i, embed_widget in enumerate(self.widget.embed_widgets):
            embed_widget.field.currentTextChanged.connect(self.select_embed(i))
        self.widget.detail_btn.clicked.connect(self.show_detail)

    def select_school(self, school):
        if school not in self.widget.equip_data:
            self.widget.kind_combo.clear()
            return
        kinds = list(self.widget.equip_data[school])
        self.widget.kind_combo.set_items([""] + kinds)
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
        for i, embed_widget in enumerate(self.widget.embed_widgets):
            embed_widget.set_label(f"Embed{i + 1}:")
        school, kind = self.widget.school_combo.currentText(), self.widget.kind_combo.currentText()
        if school not in self.widget.equip_data:
            return
        if kind not in self.widget.equip_data[school]:
            return
        if equipment not in self.widget.equip_data[school][kind]:
            self.widget.gear = None
            return
        detail = self.widget.equip_data[school][kind][equipment]
        gear = self.widget.gear = self.parent.gears[self.widget.position] = Gear(school, kind, equipment, detail)

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
        for embed_attr, embed_widget in zip(gear.embed, self.widget.embed_widgets):
            embed_widget.set_label(embed_attr)
            embed_level = embed_widget.field.currentText()
            embed_levels[len(embed_levels)] = int(embed_level)
        gear.embed_levels = embed_levels

    def select_enchant(self, enchant):
        if not self.widget.gear:
            return
        if enchant not in self.widget.enchant_data:
            self.widget.gear.enchant = None
            return
        self.widget.gear.enchant = Enchant(enchant, self.widget.enchant_data[enchant])

    def select_strength(self, strength):
        if not self.widget.gear:
            return
        self.widget.gear.strength_level = int(strength)

    def select_embed(self, index):
        def inner(embed):
            if not self.widget.gear:
                return
            self.widget.gear.embed_levels[index] = int(embed)

        return inner

    def show_detail(self):
        if not self.widget.gear:
            return
        DetailDialog(self.widget.gear, parent=self.parent).exec()

    def refresh_attribute(self):
        if not self.widget.gear:
            return

    def init(self, gear: Gear):
        if gear:
            self.widget.school_combo.setCurrentText(gear.school)
            self.widget.kind_combo.setCurrentText(gear.kind)
            self.widget.equipment_combo.setCurrentText(gear.name)
            if gear.enchant:
                self.widget.enchant_combo.setCurrentText(gear.enchant.name)
            self.widget.strength_combo.setCurrentText(str(gear.strength_level))
            for i, embed_attr in enumerate(gear.embed):
                self.widget.embed_widgets[i].field.setCurrentText(str(gear.embed_levels[i]))
        else:
            self.widget.gear = None
            if self.parent.kungfu.school in self.widget.equip_data:
                self.widget.school_combo.setCurrentText(self.parent.kungfu.school)
            else:
                self.widget.school_combo.setCurrentText("通用")
            self.widget.equipment_combo.setCurrentText("")
            self.widget.enchant_combo.setCurrentText("")
            for i, embed_widget in enumerate(self.widget.embed_widgets):
                embed_widget.set_label(f"Embed{i + 1}:")


class GearScript:

    def __init__(self, gear_widget: GearWidget):
        self.widget = gear_widget
        self.sub_scripts: dict[str, SubGearScript] = {}
        for sub_widget in self.widget.sub_widgets.values():
            self.sub_scripts[sub_widget.position] = SubGearScript(sub_widget, self.widget)
        self.connect()

    def connect(self):
        self.widget.stone_btn.clicked.connect(self.select_stone)
        self.widget.strength_combo.currentTextChanged.connect(self.select_strength)
        self.widget.embed_combo.currentTextChanged.connect(self.select_embed)

    def select_stone(self):
        dialog = StoneDialog(self.widget.stone, parent=self.widget)
        if dialog.exec() == QDialog.DialogCode.Accepted:
            self.widget.stone = dialog.stone

    def select_strength(self, strength):
        for sub_script in self.sub_scripts.values():
            if sub_script.widget.gear:
                strength = min(int(strength), sub_script.widget.gear.max_strength)
                sub_script.widget.strength_combo.setCurrentText(str(strength))

    def select_embed(self, embed):
        for sub_script in self.sub_scripts.values():
            if sub_script.widget.gear:
                for embed_widget in sub_script.widget.embed_widgets:
                    embed_widget.field.setCurrentText(str(embed))

    def display(self):
        pass

    def init(self, gears: dict[str, Gear] = None):
        if gears:
            self.widget.gears = gears
        else:
            self.widget.gears = {}
        for position, sub_script in self.sub_scripts.items():
            sub_script.init(self.widget.gears.get(position))
        return self.widget.gears
