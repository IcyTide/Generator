from PySide6.QtWidgets import QGridLayout, QLabel, QVBoxLayout, QWidget

from qt import ComboBox, LabelColumn
from qt.classes.gains.consumable import *
from qt.classes.gains.formation import FORMATIONS
from qt.classes.gains.team import TEAMS


class ConsumableWidget(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout(self)
        layout.addWidget(QLabel("消耗品:"))
        grid_layout = QGridLayout()
        layout.addLayout(grid_layout)
        self.consumable_combos: dict[str, ComboBox] = {}
        self.major_food_combo = ComboBox()
        self.consumable_combos["辅助类食品"] = self.major_food_combo
        self.major_food_combo.set_items([""] + list(MAJOR_FOODS))
        grid_layout.addWidget(LabelColumn("辅助类食品", self.major_food_combo), 0, 0)
        self.minor_food_combo = ComboBox()
        self.consumable_combos["增强类食品"] = self.minor_food_combo
        self.minor_food_combo.set_items([""] + list(MINOR_FOODS))
        grid_layout.addWidget(LabelColumn("增强类食品", self.minor_food_combo), 0, 1)
        self.major_potion_combo = ComboBox()
        self.consumable_combos["辅助类药品"] = self.major_potion_combo
        self.major_potion_combo.set_items([""] + list(MAJOR_POTIONS))
        grid_layout.addWidget(LabelColumn("辅助类药品", self.major_potion_combo), 1, 0)
        self.minor_potion_combo = ComboBox()
        self.consumable_combos["增强类药品"] = self.minor_potion_combo
        self.minor_potion_combo.set_items([""] + list(MINOR_POTIONS))
        grid_layout.addWidget(LabelColumn("增强类药品", self.minor_potion_combo), 1, 1)
        self.weapon_enchant_combo = ComboBox()
        self.consumable_combos["武器磨石"] = self.weapon_enchant_combo
        self.weapon_enchant_combo.set_items([""] + list(WEAPON_ENCHANTS))
        grid_layout.addWidget(LabelColumn("武器磨石", self.weapon_enchant_combo), 2, 0)
        self.guild_spread = ComboBox()
        self.consumable_combos["帮会宴席"] = self.guild_spread
        self.guild_spread.set_items([""] + list(GUILD_SPREADS))
        grid_layout.addWidget(LabelColumn("帮会宴席", self.guild_spread), 3, 0)
        self.guild_food = ComboBox()
        self.consumable_combos["帮会食物"] = self.guild_food
        self.guild_food.set_items([""] + list(GUILD_FOODS))
        grid_layout.addWidget(LabelColumn("帮会食物", self.guild_food), 3, 1)
        self.spread_combo = ComboBox()
        self.consumable_combos["宴席"] = self.spread_combo
        self.spread_combo.set_items([""] + list(SPREADS))
        grid_layout.addWidget(LabelColumn("宴席", self.spread_combo), 4, 0)
        self.boiled_fish_combo = ComboBox()
        self.consumable_combos["水煮鱼"] = self.boiled_fish_combo
        self.boiled_fish_combo.set_items([""] + list(BOILED_FISHES))
        grid_layout.addWidget(LabelColumn("水煮鱼", self.boiled_fish_combo), 4, 1)
        self.snack_combo = ComboBox()
        self.consumable_combos["家园食物"] = self.snack_combo
        self.snack_combo.set_items([""] + list(SNACKS))
        grid_layout.addWidget(LabelColumn("家园食物", self.snack_combo), 5, 0)
        self.wine_combo = ComboBox()
        self.consumable_combos["家园酒"] = self.wine_combo
        self.wine_combo.set_items([""] + list(WINES))
        grid_layout.addWidget(LabelColumn("家园酒", self.wine_combo), 5, 1)
        layout.addStretch()


class FormationWidget(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout(self)
        layout.addWidget(QLabel("阵眼:"))
        grid_layout = QGridLayout()
        layout.addLayout(grid_layout)

        self.belong_combo = ComboBox()
        self.belong_combo.set_items([""] + list(FORMATIONS))
        grid_layout.addWidget(LabelColumn("来源", self.belong_combo), 0, 0)
        self.level_4_combo = ComboBox()
        grid_layout.addWidget(LabelColumn("四重覆盖率", self.level_4_combo), 1, 0)
        self.level_5_combo = ComboBox()
        grid_layout.addWidget(LabelColumn("五重覆盖率", self.level_5_combo), 2, 0)
        self.level_6_combo = ComboBox()
        grid_layout.addWidget(LabelColumn("六重覆盖率", self.level_6_combo), 3, 0)
        layout.addStretch()


class TeamWidget(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout(self)
        layout.addWidget(QLabel("团队增益:"))
        grid_layout = QGridLayout()
        layout.addLayout(grid_layout)

        self.belong_combo = ComboBox()
        self.belong_combo.set_items([""] + list(TEAMS))
        grid_layout.addWidget(LabelColumn("来源", self.belong_combo), 0, 0)
        self.stack_combo = ComboBox()
        grid_layout.addWidget(LabelColumn("层数", self.stack_combo), 1, 0)
        self.rate_combo = ComboBox()
        grid_layout.addWidget(LabelColumn("覆盖率", self.rate_combo), 2, 0)
        layout.addStretch()


class BonusWidget(QWidget):
    def __init__(self):
        super().__init__()
        layout = QGridLayout(self)
        self.consumable_widget = ConsumableWidget()
        layout.addWidget(self.consumable_widget, 0, 0, 2, 1)
        self.formation_widget = FormationWidget()
        layout.addWidget(self.formation_widget, 0, 1)
        self.team_widget = TeamWidget()
        layout.addWidget(self.team_widget, 1, 1)
