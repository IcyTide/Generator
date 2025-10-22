from PySide6.QtWidgets import QDialog, QLabel, QVBoxLayout, QWidget

from base.translate import get_translates
from qt import LabelRow
from qt.classes.gear import Gear


class DetailDialog(QDialog):

    def __init__(self, gear: Gear, parent: QWidget = None):
        super().__init__(parent)
        self.setWindowTitle("装备属性")
        layout = QVBoxLayout(self)

        layout.addWidget(LabelRow("名称:", QLabel(gear.name)))
        layout.addWidget(QLabel("基础属性:"))
        translates, _ = get_translates(gear.base)
        for attr, value in gear.base.items():
            layout.addWidget(LabelRow(translates[attr], QLabel(str(value))))

        layout.addWidget(QLabel("精炼属性:"))
        strength_magic = gear.strength_magic
        translates, _ = get_translates(strength_magic)
        for attr, value in gear.magic.items():
            if strength_value := strength_magic.get(attr):
                layout.addWidget(LabelRow(translates[attr], QLabel(f"{value}(+{strength_value})")))
            else:
                layout.addWidget(LabelRow(translates[attr], QLabel(str(value))))

        if embeds := gear.embeds:
            layout.addWidget(QLabel("镶嵌属性:"))
            translates, _ = get_translates(embeds)
            for attr, value in embeds.items():
                layout.addWidget(LabelRow(translates[attr], QLabel(str(value))))

        if enchant := gear.enchant:
            layout.addWidget(QLabel("附魔属性:"))
            translates, _ = get_translates(enchant.attributes)
            for attr, value in enchant.attributes.items():
                layout.addWidget(LabelRow(translates[attr], QLabel(str(value))))

        if stone := gear.stone:
            layout.addWidget(QLabel("五彩石属性:"))
            translates, _ = get_translates(stone.attributes)
            for attr, value in stone.attributes.items():
                layout.addWidget(LabelRow(translates[attr], QLabel(str(value))))
