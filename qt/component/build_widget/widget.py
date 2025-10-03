from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget, QVBoxLayout, QTableWidget, QListWidget, QGridLayout, QLabel

from base.constant import MAX_TALENT_COUNT
from kungfus import Kungfu
from qt import ComboBox, Table, LabelColumn


class TalentWidget(QWidget):
    kungfu: Kungfu

    def __init__(self):
        super().__init__()
        layout = QVBoxLayout(self)
        layout.addWidget(QLabel("Talent:"))
        grid_layout = QGridLayout(grid_widget := QWidget())
        self.talent_combos = []
        for i in range(MAX_TALENT_COUNT):
            grid_layout.addWidget(LabelColumn(f"No. {i + 1}", talent_combo := ComboBox()), 0, i)
            self.talent_combos.append(talent_combo)
        self.talent_pool = QListWidget()
        grid_layout.addWidget(LabelColumn("Pool", self.talent_pool), 0, MAX_TALENT_COUNT)
        layout.addWidget(grid_widget)
        layout.addStretch()


class RecipeWidget(QWidget):
    kungfu: Kungfu

    def __init__(self):
        super().__init__()
        layout = QVBoxLayout(self)
        layout.addWidget(QLabel("Recipes:"))
        grid_layout = QGridLayout()
        layout.addLayout(grid_layout)

        self.skill_combo = ComboBox()
        grid_layout.addWidget(LabelColumn("Skill", self.skill_combo), 0, 0)
        self.recipe_table = Table(["Name", "Desc", "Selected"])
        self.recipe_table.setSelectionMode(QTableWidget.SelectionMode.ExtendedSelection)
        grid_layout.addWidget(LabelColumn("Recipe List", self.recipe_table), 0, 1)


class BuildWidget(QWidget):
    kungfu: Kungfu

    def __init__(self):
        super().__init__()
        layout = QVBoxLayout(self)
        layout.addWidget(TalentWidget())
        layout.addWidget(RecipeWidget())
