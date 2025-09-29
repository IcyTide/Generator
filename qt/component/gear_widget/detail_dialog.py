from PySide6.QtWidgets import QDialog, QLabel, QVBoxLayout, QWidget

from qt import LabelRow
from qt.classes.gear import Gear


class DetailDialog(QDialog):

    def __init__(self, gear: Gear, parent: QWidget = None):
        super().__init__(parent)
        self.setWindowTitle("Gear Detail")
        layout = QVBoxLayout(self)

        layout.addWidget(LabelRow("Name:", QLabel(gear.name)))
        layout.addWidget(QLabel("Base:"))
        for attr, value in gear.base.items():
            layout.addWidget(LabelRow(attr, QLabel(str(value))))

        layout.addWidget(QLabel("Magic:"))
        strength_magic = gear.strength_magic
        for attr, value in gear.magic.items():
            if strength_value := strength_magic.get(attr):
                layout.addWidget(LabelRow(attr, QLabel(f"{value}(+{strength_value})")))
            else:
                layout.addWidget(LabelRow(attr, QLabel(str(value))))

        if embeds := gear.embeds:
            layout.addWidget(QLabel("Embed:"))
            for attr, value in embeds.items():
                layout.addWidget(LabelRow(attr, QLabel(str(value))))

        if enchant := gear.enchant:
            layout.addWidget(QLabel("Enchant:"))
            for attr, value in enchant.attributes.items():
                layout.addWidget(LabelRow(attr, QLabel(str(value))))
