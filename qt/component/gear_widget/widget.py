from PySide6.QtCore import Qt
from PySide6.QtWidgets import QGridLayout, QHBoxLayout, QLabel, QPushButton, QSizePolicy, QVBoxLayout, QWidget

from assets.raw.enchants import ENCHANTS
from assets.raw.equipments import EQUIPMENTS
from base.constant import EMBED_POSITIONS, MAX_EMBED_LEVEL, MAX_STRENGTH_LEVEL, POSITION_MAP
from qt import ComboBox, LabelColumn
from qt.classes.gear import Gear, Stone
from qt.classes.kungfu import DisplayKungfu


class SubGearWidget:
    gear: Gear | None = None

    def __init__(self, position: str, row: int, layout: QGridLayout):
        self.position = position
        layout.addWidget(LabelColumn("", QLabel(position)), row, 0)
        self.equip_data = EQUIPMENTS[position]
        self.enchant_data = ENCHANTS.get(position)

        self.school_combo = ComboBox()
        layout.addWidget(LabelColumn("", self.school_combo), row, 1)
        self.school_combo.set_items([""] + list(self.equip_data))
        self.kind_combo = ComboBox()
        layout.addWidget(LabelColumn("", self.kind_combo), row, 2)
        self.equipment_combo = ComboBox()
        layout.addWidget(LabelColumn("", self.equipment_combo), row, 3)

        if self.enchant_data:
            self.enchant_combo = ComboBox()
            layout.addWidget(LabelColumn("", self.enchant_combo), row, 4)
            self.enchant_combo.set_items([""] + list(self.enchant_data))
        else:
            self.enchant_combo = None

        self.strength_combo = ComboBox()
        layout.addWidget(LabelColumn("", self.strength_combo), row, 5)
        self.embed_widgets = []
        for i in range(EMBED_POSITIONS[position]):
            embed_widget = LabelColumn("Embed:", embed_combo := ComboBox())
            self.embed_widgets.append(embed_widget)
            embed_combo.set_items(range(MAX_EMBED_LEVEL + 1), MAX_EMBED_LEVEL)
            layout.addWidget(embed_widget, row, 6 + i)
        self.detail_btn = QPushButton("Detail")
        layout.addWidget(LabelColumn("", self.detail_btn), row, 9)


class GearWidget(QWidget):
    kungfu: DisplayKungfu
    gears: dict
    stone: Stone = None
    HEADERS = ["Position", "School", "Kind", "Equip", "Enchant", "Strength", "Embed1", "Embed2", "Embed3", "Detail"]

    def __init__(self):
        super().__init__()
        layout = QVBoxLayout(self)

        top_layout = QHBoxLayout()
        layout.addLayout(top_layout)
        self.stone_btn = QPushButton("Select Stone")
        top_layout.addWidget(LabelColumn("", self.stone_btn))
        self.strength_combo = ComboBox()
        self.strength_combo.set_items(range(MAX_STRENGTH_LEVEL + 1), -1)
        top_layout.addWidget(LabelColumn("All Strength", self.strength_combo))
        self.embed_combo = ComboBox()
        self.embed_combo.set_items(range(MAX_EMBED_LEVEL + 1), -1)
        top_layout.addWidget(LabelColumn("All Embed", self.embed_combo))
        self.display_btn = QPushButton("Display")
        top_layout.addWidget(LabelColumn("", self.display_btn))

        grid_layout = QGridLayout()
        layout.addLayout(grid_layout)

        self.sub_widgets: dict[str, SubGearWidget] = {}
        for i, header in enumerate(self.HEADERS):
            label = QLabel(header)
            label.setAlignment(Qt.AlignmentFlag.AlignCenter)
            label.setStyleSheet("font-weight: bold;")
            label.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
            grid_layout.addWidget(label, 0, i)
        for i, position in enumerate(POSITION_MAP.values()):
            self.sub_widgets[position] = SubGearWidget(position, i + 1, grid_layout)

        layout.addStretch()
