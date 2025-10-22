from PySide6.QtCore import Qt
from PySide6.QtWidgets import QCheckBox, QGridLayout, QHBoxLayout, QLabel, QPushButton, QSizePolicy, QVBoxLayout, \
    QWidget

from assets.raw.enchants import ENCHANTS
from assets.raw.equipments import EQUIPMENTS
from base.constant import EMBED_POSITIONS, MAX_EMBED_LEVEL, MAX_STRENGTH_LEVEL, POSITIONS, SPECIAL_ENCHANT_MAP, \
    STONE_POSITIONS
from qt import ComboBox, LabelColumn


class SubGearWidget:
    def __init__(self, label: str, row: int, layout: QGridLayout):
        self.label = label
        self.position = POSITIONS[label]
        layout.addWidget(QLabel(self.label), row, 0)
        self.equip_data = EQUIPMENTS[self.position]
        self.enchant_data = ENCHANTS.get(self.position)

        self.school_combo = ComboBox()
        layout.addWidget(self.school_combo, row, 1)
        self.school_combo.set_items(list(self.equip_data), -1)
        self.kind_combo = ComboBox()
        layout.addWidget(self.kind_combo, row, 2)
        self.equipment_combo = ComboBox()
        layout.addWidget(self.equipment_combo, row, 3)

        self.enchant_combo = ComboBox()
        layout.addWidget(self.enchant_combo, row, 4)
        self.enchant_combo.set_items([""] + list(self.enchant_data))

        if self.position in SPECIAL_ENCHANT_MAP:
            self.special_enchant: QCheckBox | None = QCheckBox()
            layout.addWidget(self.special_enchant, row, 5)
        else:
            self.special_enchant = None

        self.strength_combo = ComboBox()
        layout.addWidget(self.strength_combo, row, 6)
        self.embed_combos: list[ComboBox] = []
        for i in range(EMBED_POSITIONS[self.position]):
            self.embed_combos.append(embed_combo := ComboBox())
            embed_combo.set_items(range(MAX_EMBED_LEVEL + 1), MAX_EMBED_LEVEL)
            layout.addWidget(embed_combo, row, 7 + i)
        if self.position in STONE_POSITIONS:
            self.stone_btn = QPushButton("五彩石")
            layout.addWidget(self.stone_btn, row, 10)
        else:
            self.stone_btn = None
        self.detail_btn = QPushButton("细节")
        layout.addWidget(self.detail_btn, row, 11)


class GearWidget(QWidget):
    HEADERS = [
        "部位", "一级目录", "二级目录", "装备", "附魔", "大附魔",
        "精炼", "镶嵌1", "镶嵌2", "镶嵌3", "五彩石", "细节"
    ]

    def __init__(self):
        super().__init__()
        layout = QVBoxLayout(self)

        top_layout = QHBoxLayout()
        layout.addLayout(top_layout)
        self.gain_attribute = QCheckBox()
        top_layout.addWidget(LabelColumn("均摊特效属性", self.gain_attribute), 1)
        self.gain_attribute.setChecked(True)
        self.special_enchant = QCheckBox()
        top_layout.addWidget(LabelColumn("全部大附魔", self.special_enchant), 1)
        self.strength_combo = ComboBox()
        self.strength_combo.set_items(range(MAX_STRENGTH_LEVEL + 1), -1)
        top_layout.addWidget(LabelColumn("全部精炼", self.strength_combo), 2)
        self.embed_combo = ComboBox()
        self.embed_combo.set_items(range(MAX_EMBED_LEVEL + 1), -1)
        top_layout.addWidget(LabelColumn("全部精炼", self.embed_combo), 2)
        self.detail_btn = QPushButton("总属性")
        top_layout.addWidget(LabelColumn("", self.detail_btn), 2)

        grid_layout = QGridLayout()
        layout.addLayout(grid_layout)

        self.sub_widgets: dict[str, SubGearWidget] = {}
        for i, header in enumerate(self.HEADERS):
            label = QLabel(header)
            label.setAlignment(Qt.AlignmentFlag.AlignCenter)
            label.setStyleSheet("font-weight: bold;")
            label.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
            grid_layout.addWidget(label, 0, i)
            grid_layout.setColumnStretch(i, 0)
        for i, position in enumerate(POSITIONS):
            self.sub_widgets[position] = SubGearWidget(position, i + 1, grid_layout)
        grid_layout.setColumnStretch(self.HEADERS.index("装备"), 1)

        layout.addStretch()
