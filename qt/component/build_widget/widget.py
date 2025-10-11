from PySide6.QtWidgets import QGridLayout, QLabel, QListWidget, QTableWidget, QVBoxLayout, QWidget

from base.constant import MAX_TALENT_COUNT
from qt import ComboBox, LabelColumn, Table


class TalentWidget(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout(self)
        layout.addWidget(QLabel("Talent:"))
        grid_layout = QGridLayout(grid_widget := QWidget())
        self.talent_combos: list[ComboBox] = []
        for i in range(MAX_TALENT_COUNT):
            grid_layout.addWidget(LabelColumn(f"No. {i + 1}", talent_combo := ComboBox()), 0, i)
            self.talent_combos.append(talent_combo)
        self.talent_pool = QListWidget()
        self.talent_pool.setSelectionMode(QListWidget.SelectionMode.MultiSelection)
        grid_layout.addWidget(LabelColumn("Pool", self.talent_pool), 0, MAX_TALENT_COUNT)
        for i in range(MAX_TALENT_COUNT + 1):
            grid_layout.setColumnStretch(i, 1)
        layout.addWidget(grid_widget)
        layout.addStretch()


class RecipeWidget(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout(self)
        layout.addWidget(QLabel("Recipes:"))
        grid_layout = QGridLayout()
        layout.addLayout(grid_layout)

        self.skill_combo = ComboBox()
        grid_layout.addWidget(LabelColumn("Skill", self.skill_combo), 0, 0)
        grid_layout.setColumnStretch(0, 1)
        self.recipe_table = Table(["Name", "Desc"])
        self.recipe_table.setSelectionMode(QTableWidget.SelectionMode.MultiSelection)
        grid_layout.addWidget(LabelColumn("Recipe List", self.recipe_table), 0, 1)
        grid_layout.setColumnStretch(1, 2)


class BuildWidget(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout(self)
        self.talent_widget = TalentWidget()
        layout.addWidget(self.talent_widget)
        self.recipe_widget = RecipeWidget()
        layout.addWidget(self.recipe_widget)
