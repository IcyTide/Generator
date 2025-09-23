from PySide6.QtCore import Qt
from PySide6.QtWidgets import QGridLayout, QLabel, QPushButton, QSizePolicy, QWidget

from assets.raw.enchants import ENCHANTS
from assets.raw.equipments import EQUIPMENTS
from base.constant import EMBED_POSITIONS, MAX_EMBED_LEVEL, POSITION_MAP
from qt import ComboBox


class SubGearWidget:
    def __init__(self, position: str, row: int, layout: QGridLayout):
        layout.addWidget(QLabel(position), row, 0)
        self.equip_data = EQUIPMENTS[position]
        self.enchant_data = ENCHANTS.get(position)
        self.schools = []
        for equip in self.equip_data.values():
            if equip['school'] not in self.schools:
                self.schools.append(equip['school'])

        self.school_combo = ComboBox()
        layout.addWidget(self.school_combo, row, 1)
        self.school_combo.set_items([""] + self.schools)
        self.kind_combo = ComboBox()
        layout.addWidget(self.kind_combo, row, 2)
        self.equip_combo = ComboBox()
        layout.addWidget(self.equip_combo, row, 3)

        if self.enchant_data:
            self.enchant_combo = ComboBox()
            layout.addWidget(self.enchant_combo, row, 4)
            self.enchant_combo.set_items([""] + list(self.enchant_data))
        else:
            self.enchant_combo = None

        self.strength_combo = ComboBox()
        layout.addWidget(self.strength_combo, row, 5)
        self.embed_combos = []
        for i in range(EMBED_POSITIONS[position]):
            self.embed_combos.append(embed_combo := ComboBox())
            embed_combo.set_items(range(MAX_EMBED_LEVEL + 1))
            layout.addWidget(embed_combo, row, 6 + i)
        self.detail_btn = QPushButton("Detail")
        layout.addWidget(self.detail_btn, row, 9)


class GearWidget(QWidget):
    HEADERS = ["Position", "School", "Kind", "Equip", "Enchant", "Strength", "Embed1", "Embed2", "Embed3", "Detail"]

    def __init__(self):
        super().__init__()
        layout = QGridLayout(self)

        self.sub_widgets = []

        for i, header in enumerate(self.HEADERS):
            label = QLabel(header)
            label.setAlignment(Qt.AlignmentFlag.AlignCenter)
            label.setStyleSheet("font-weight: bold;")
            label.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
            layout.addWidget(label, 0, i)
        for i, position in enumerate(POSITION_MAP.values()):
            self.sub_widgets.append(SubGearWidget(position, i + 1, layout))
