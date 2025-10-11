from PySide6.QtWidgets import QDialog, QLabel, QToolBox, QVBoxLayout, QWidget

from qt import LabelRow
from qt.classes.attribute import Attribute
from qt.utils import percent


class AttributeDialog(QDialog):
    def __init__(self, current_attribute: Attribute, snapshot_attribute: Attribute, parent: QWidget = None):
        super().__init__(parent)
        self.setWindowTitle("Attribute Detail")

        layout = QVBoxLayout(self)

        layout.addWidget(toolbox := QToolBox())

        current_layout = QVBoxLayout(current_page := QWidget())
        self.display_attribute(current_layout, current_attribute)
        toolbox.addItem(current_page, "Current Attribute")
        if current_attribute.recipes:
            current_layout = QVBoxLayout(current_page := QWidget())
            for recipe in current_attribute.recipes:
                current_layout.addWidget(LabelRow("recipe:", QLabel(recipe)))
            toolbox.addItem(current_page, "Current Recipes")

        snapshot_layout = QVBoxLayout(snapshot_page := QWidget())
        self.display_attribute(snapshot_layout, snapshot_attribute)
        toolbox.addItem(snapshot_page, "Snapshot Attribute")
        if snapshot_attribute.recipes:
            snapshot_layout = QVBoxLayout(snapshot_page := QWidget())
            for recipe in snapshot_attribute.recipes:
                snapshot_layout.addWidget(LabelRow("recipe:", QLabel(recipe)))
            toolbox.addItem(snapshot_page, "Snapshot Recipes")

    @staticmethod
    def display_attribute(layout: QVBoxLayout, attribute: Attribute):
        major = f"{attribute.major_base}/{attribute.major}"
        layout.addWidget(LabelRow("Major:", QLabel(major)))
        attack_power = f"{attribute.base_attack_power}/{attribute.attack_power}"
        layout.addWidget(LabelRow("AttackPower:", QLabel(attack_power)))
        surplus = f"{attribute.surplus_base}/{attribute.surplus}"
        layout.addWidget(LabelRow("Surplus:", QLabel(surplus)))
        strain = f"{attribute.strain_base}/{attribute.final_strain}"
        strain += f"({percent(attribute.strain_percent)}/{percent(attribute.strain)})"
        layout.addWidget(LabelRow("Strain:", QLabel(strain)))
        overcome = f"{attribute.base_overcome}/{attribute.final_overcome}"
        overcome += f"({percent(attribute.overcome)})"
        layout.addWidget(LabelRow("Overcome:", QLabel(overcome)))
        critical_strike = f"{attribute.final_critical_strike}"
        critical_strike += f"({percent(attribute.critical_strike_percent)}/{percent(attribute.critical_strike)})"
        layout.addWidget(LabelRow("Critical Strike:", QLabel(critical_strike)))
        critical_power = f"{attribute.critical_power_base}"
        critical_power += f"({percent(attribute.critical_power_percent)}/{percent(attribute.critical_power)})"
        layout.addWidget(LabelRow("Critical Power:", QLabel(critical_power)))
