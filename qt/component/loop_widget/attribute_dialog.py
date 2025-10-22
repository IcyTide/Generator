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
        toolbox.addItem(current_page, "当前属性")
        if current_attribute.recipes:
            current_layout = QVBoxLayout(current_page := QWidget())
            for recipe in current_attribute.recipes:
                current_layout.addWidget(LabelRow("秘籍:", QLabel(recipe)))
            toolbox.addItem(current_page, "当前秘籍")

        snapshot_layout = QVBoxLayout(snapshot_page := QWidget())
        self.display_attribute(snapshot_layout, snapshot_attribute)
        toolbox.addItem(snapshot_page, "快照属性")
        if snapshot_attribute.recipes:
            snapshot_layout = QVBoxLayout(snapshot_page := QWidget())
            for recipe in snapshot_attribute.recipes:
                snapshot_layout.addWidget(LabelRow("秘籍:", QLabel(recipe)))
            toolbox.addItem(snapshot_page, "快照秘籍")

    @staticmethod
    def display_attribute(layout: QVBoxLayout, attribute: Attribute):
        major = f"{attribute.major_base}/{attribute.major}"
        layout.addWidget(LabelRow("主属性:", QLabel(major)))
        attack_power = f"{attribute.base_attack_power}/{attribute.attack_power}"
        layout.addWidget(LabelRow("基础攻击/最终攻击:", QLabel(attack_power)))
        surplus = f"{attribute.surplus_base}/{attribute.surplus}"
        layout.addWidget(LabelRow("基础破招/最终破招:", QLabel(surplus)))
        strain = f"{attribute.strain_base}/{attribute.final_strain}"
        strain += f"({percent(attribute.strain_percent)}/{percent(attribute.strain)})"
        layout.addWidget(LabelRow("基础无双/最终无双(无双百分比/最终无双百分比):", QLabel(strain)))
        overcome = f"{attribute.base_overcome}/{attribute.final_overcome}"
        overcome += f"({percent(attribute.overcome)})"
        layout.addWidget(LabelRow("基础破防/最终破防(破防百分比):", QLabel(overcome)))
        critical_strike = f"{attribute.final_critical_strike}"
        critical_strike += f"({percent(attribute.critical_strike_percent)}/{percent(attribute.critical_strike)})"
        layout.addWidget(LabelRow("会心(会心百分比/最终会心百分比):", QLabel(critical_strike)))
        critical_power = f"{attribute.critical_power_base}"
        critical_power += f"({percent(attribute.critical_power_percent)}/{percent(attribute.critical_power)})"
        layout.addWidget(LabelRow("会效(会效百分比/最终会效百分比):", QLabel(critical_power)))
