from PySide6.QtWidgets import QDialog, QHBoxLayout, QLabel, QPushButton, QVBoxLayout, QWidget

from assets.raw.stones import STONES
from qt import ComboBox, LabelRow
from qt.classes.gear import Stone


class StoneDialog(QDialog):
    stone: Stone | None

    def __init__(self, stone: Stone = None, parent: QWidget = None):
        super().__init__(parent)
        self.setWindowTitle("Select Stone")

        self.stone_data = STONES
        layout = QVBoxLayout(self)

        self.attr_combo_1 = ComboBox()
        layout.addWidget(LabelRow("Attribute 1:", self.attr_combo_1))
        self.attr_combo_1.set_items([""] + list(self.stone_data))

        self.attr_combo_2 = ComboBox()
        layout.addWidget(LabelRow("Attribute 2:", self.attr_combo_2))
        self.attr_combo_3 = ComboBox()
        layout.addWidget(LabelRow("Attribute 3:", self.attr_combo_3))
        self.attr_combos = [self.attr_combo_1, self.attr_combo_2, self.attr_combo_3]

        self.level_combo = ComboBox()
        layout.addWidget(LabelRow("Level:", self.level_combo))

        self.name_label = QLabel("")
        layout.addWidget(LabelRow("Name:", self.name_label))

        layout.addLayout((btn_layout := QHBoxLayout()))
        btn_layout.addWidget((ok_button := QPushButton("OK")))
        btn_layout.addWidget((cancel_button := QPushButton("Cancel")))

        ok_button.clicked.connect(self.accept)
        cancel_button.clicked.connect(self.reject)
        self.attr_combo_1.currentTextChanged.connect(self.select_attr_1)
        self.attr_combo_2.currentTextChanged.connect(self.select_attr_2)
        self.attr_combo_3.currentTextChanged.connect(self.select_attr_3)
        self.level_combo.currentTextChanged.connect(self.select_level)

        if stone:
            for attr, attr_combo in zip(stone.attributes, self.attr_combos):
                attr_combo.setCurrentText(attr)

    def set_stone(self, stone: dict = None):
        if not stone:
            self.stone = None
            self.name_label.clear()
        else:
            self.stone = Stone(stone)
            self.name_label.setText(self.stone.name)

    def select_attr_1(self, attr: str):
        if attr not in self.stone_data:
            self.attr_combo_2.clear()
            self.set_stone()
            return
        self.attr_combo_2.set_items([""] + list(self.stone_data[attr]))
        self.set_stone()

    def select_attr_2(self, attr: str):
        attr_1 = self.attr_combo_1.currentText()
        if attr_1 not in self.stone_data:
            return
        if attr not in self.stone_data[attr_1]:
            self.attr_combo_3.clear()
            self.set_stone()
            return
        if any(isinstance(key, int) for key in self.stone_data[attr_1][attr]):
            self.attr_combo_3.clear()
            self.level_combo.set_items([""] + list(self.stone_data[attr_1][attr]))
            level = self.level_combo.currentText()
            if level and int(level) in self.stone_data[attr_1][attr]:
                self.set_stone(self.stone_data[attr_1][attr][int(level)])
        else:
            self.attr_combo_3.set_items([""] + list(self.stone_data[attr_1][attr]))
            self.set_stone()

    def select_attr_3(self, attr: str):
        attr_1 = self.attr_combo_1.currentText()
        attr_2 = self.attr_combo_2.currentText()
        if attr_1 not in self.stone_data:
            return
        if attr_2 not in self.stone_data[attr_1]:
            return
        if attr not in self.stone_data[attr_1][attr_2]:
            self.set_stone()
            return
        self.level_combo.set_items([""] + list(self.stone_data[attr_1][attr_2][attr]))
        self.set_stone()
        level = self.level_combo.currentText()
        if level and int(level) in self.stone_data[attr_1][attr_2][attr]:
            self.set_stone(self.stone_data[attr_1][attr_2][attr][int(level)])

    def select_level(self, level: str):
        attr_1 = self.attr_combo_1.currentText()
        if attr_1 not in self.stone_data:
            return
        attr_2 = self.attr_combo_2.currentText()
        if attr_2 not in self.stone_data[attr_1]:
            return
        if any(isinstance(key, int) for key in self.stone_data[attr_1][attr_2]):
            if level and int(level) in self.stone_data[attr_1][attr_2][attr_2]:
                self.set_stone(self.stone_data[attr_1][attr_2][int(level)])
            else:
                self.set_stone()
        else:
            attr_3 = self.attr_combo_3.currentText()
            if attr_3 not in self.stone_data[attr_1][attr_2]:
                return
            if level and int(level) in self.stone_data[attr_1][attr_2][attr_3]:
                self.set_stone(self.stone_data[attr_1][attr_2][attr_3][int(level)])
            else:
                self.set_stone()
