from PySide6.QtWidgets import QDialog, QHBoxLayout, QLabel, QPushButton, QSizePolicy, QVBoxLayout, QWidget

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
        self.attr_combo_1.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        layout.addWidget(LabelRow("Attribute 1:", self.attr_combo_1))
        self.attr_combo_1.set_items([""] + list(self.stone_data))

        self.attr_combo_2 = ComboBox()
        self.attr_combo_2.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        layout.addWidget(LabelRow("Attribute 2:", self.attr_combo_2))

        self.attr_combo_3 = ComboBox()
        self.attr_combo_3.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
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
            self.level_combo.setCurrentText(str(stone.level))

    @staticmethod
    def is_stone_node(node: dict):
        for key in node:
            if isinstance(key, int):
                return True
        return False

    def set_stone(self, stone: dict = None):
        if not stone:
            self.stone = None
            self.name_label.clear()
        else:
            self.stone = Stone(stone)
            self.name_label.setText(self.stone.name)

    def select_attr_1(self, attr: str):
        self.set_stone()
        if attr in self.stone_data:
            self.attr_combo_2.set_items([""] + list(self.stone_data[attr]))
        else:
            self.attr_combo_2.clear()
            self.attr_combo_3.clear()
            self.level_combo.clear()

    def select_attr_2(self, attr: str):
        self.set_stone()
        attr_1 = self.attr_combo_1.currentText()
        if attr_1 not in self.stone_data:
            return
        if attr in self.stone_data[attr_1]:
            if self.is_stone_node(self.stone_data[attr_1][attr]):
                self.attr_combo_3.clear()
                self.level_combo.set_items([""] + list(self.stone_data[attr_1][attr]))
            else:
                self.attr_combo_3.set_items([""] + list(self.stone_data[attr_1][attr]))
        else:
            self.attr_combo_3.clear()
            self.level_combo.clear()

    def select_attr_3(self, attr: str):
        self.set_stone()
        attr_1 = self.attr_combo_1.currentText()
        attr_2 = self.attr_combo_2.currentText()
        if attr_1 not in self.stone_data:
            return
        if attr_2 not in self.stone_data[attr_1]:
            return
        if attr in self.stone_data[attr_1][attr_2]:
            self.level_combo.set_items([""] + list(self.stone_data[attr_1][attr_2][attr]))
        else:
            self.level_combo.clear()

    def select_level(self, level: str):
        self.set_stone()
        if not level:
            return
        attr_1 = self.attr_combo_1.currentText()
        if attr_1 not in self.stone_data:
            return
        attr_2 = self.attr_combo_2.currentText()
        if attr_2 not in self.stone_data[attr_1]:
            return
        attr_3 = self.attr_combo_3.currentText()
        if attr_3 not in self.stone_data[attr_1][attr_2]:
            return
        if int(level) not in self.stone_data[attr_1][attr_2][attr_3]:
            return
        self.set_stone(self.stone_data[attr_1][attr_2][attr_3][int(level)])
