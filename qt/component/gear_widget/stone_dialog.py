from PySide6.QtWidgets import QDialog, QHBoxLayout, QLabel, QPushButton, QSizePolicy, QVBoxLayout, QWidget

from assets.raw.stones import STONES
from base.translate import get_translates
from qt import ComboBox, LabelRow
from qt.classes.gear import Stone


class StoneDialog(QDialog):
    stone: Stone | None

    def __init__(self, stone: Stone = None, parent: QWidget = None):
        super().__init__(parent)
        self.setWindowTitle("选择五彩石")

        self.stone_data = STONES
        layout = QVBoxLayout(self)

        self.attr_combo_1 = ComboBox()
        self.attr_combo_1.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        layout.addWidget(LabelRow("属性 1:", self.attr_combo_1))
        _, translates = get_translates(self.stone_data)
        self.attr_combo_1.set_items([""] + list(translates))

        self.attr_combo_2 = ComboBox()
        self.attr_combo_2.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        layout.addWidget(LabelRow("属性 2:", self.attr_combo_2))

        self.attr_combo_3 = ComboBox()
        self.attr_combo_3.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        layout.addWidget(LabelRow("属性 3:", self.attr_combo_3))

        self.attr_combos = [self.attr_combo_1, self.attr_combo_2, self.attr_combo_3]

        self.level_combo = ComboBox()
        layout.addWidget(LabelRow("等级:", self.level_combo))

        self.name_label = QLabel("")
        layout.addWidget(LabelRow("名称:", self.name_label))

        layout.addLayout((btn_layout := QHBoxLayout()))
        btn_layout.addWidget((ok_button := QPushButton("确认")))
        btn_layout.addWidget((cancel_button := QPushButton("取消")))

        ok_button.clicked.connect(self.accept)
        cancel_button.clicked.connect(self.reject)
        self.attr_combo_1.currentTextChanged.connect(self.select_attr_1)
        self.attr_combo_2.currentTextChanged.connect(self.select_attr_2)
        self.attr_combo_3.currentTextChanged.connect(self.select_attr_3)
        self.level_combo.currentTextChanged.connect(self.select_level)

        if stone:
            node = self.stone_data
            for attr, attr_combo in zip(stone.attributes, self.attr_combos):
                translates, _  = get_translates(node)
                attr_combo.setCurrentText(translates[attr])
                node = node[attr]
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
        _, translates = get_translates(self.stone_data)
        if attr in translates:
            attr = translates[attr]
            _, translates = get_translates(self.stone_data[attr])
            self.attr_combo_2.set_items([""] + list(translates))
        else:
            self.attr_combo_2.clear()
            self.attr_combo_3.clear()
            self.level_combo.clear()

    def select_attr_2(self, attr: str):
        self.set_stone()
        attr_1 = self.attr_combo_1.currentText()
        _, translates = get_translates(self.stone_data)
        if attr_1 in translates:
            attr_1 = translates[attr_1]
        else:
            return
        _, translates = get_translates(self.stone_data[attr_1])
        if attr in translates:
            attr = translates[attr]
            if self.is_stone_node(self.stone_data[attr_1][attr]):
                self.attr_combo_3.clear()
                self.level_combo.set_items([""] + list(self.stone_data[attr_1][attr]))
            else:
                _, translates = get_translates(self.stone_data[attr_1][attr])
                self.attr_combo_3.set_items([""] + list(translates))
        else:
            self.attr_combo_3.clear()
            self.level_combo.clear()

    def select_attr_3(self, attr: str):
        self.set_stone()
        attr_1 = self.attr_combo_1.currentText()
        _, translates = get_translates(self.stone_data)
        if attr_1 in translates:
            attr_1 = translates[attr_1]
        else:
            return
        attr_2 = self.attr_combo_2.currentText()
        _, translates = get_translates(self.stone_data[attr_1])
        if attr_2 in translates:
            attr_2 = translates[attr_2]
        else:
            return
        _, translates = get_translates(self.stone_data[attr_1][attr_2])
        if attr in translates:
            attr = translates[attr]
            self.level_combo.set_items([""] + list(self.stone_data[attr_1][attr_2][attr]))
        else:
            self.level_combo.clear()

    def select_level(self, level: str):
        self.set_stone()
        if not level:
            return
        attr_1 = self.attr_combo_1.currentText()
        _, translates = get_translates(self.stone_data)
        if attr_1 in translates:
            attr_1 = translates[attr_1]
        else:
            return
        attr_2 = self.attr_combo_2.currentText()
        _, translates = get_translates(self.stone_data[attr_1])
        if attr_2 in translates:
            attr_2 = translates[attr_2]
        else:
            return

        if self.is_stone_node(self.stone_data[attr_1][attr_2]):
            stone_node = self.stone_data[attr_1][attr_2]
        else:
            attr_3 = self.attr_combo_3.currentText()
            _, translates = get_translates(self.stone_data[attr_1][attr_2])
            if attr_3 in translates:
                attr_3 = translates[attr_3]
            else:
                return
            stone_node = self.stone_data[attr_1][attr_2][attr_3]
        if int(level) in stone_node:
            self.set_stone(stone_node[int(level)])
        else:
            return
