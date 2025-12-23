from PySide6.QtWidgets import QCheckBox, QDialog, QLabel, QToolBox, QVBoxLayout, QWidget

from base.translate import get_translates
from qt import LabelRow
from qt.classes.gains.gear import GearGain


class AttributeDialog(QDialog):
    def __init__(self, attributes: dict[str, int], recipes: list[str], gains: list[GearGain], parent: QWidget = None):
        super().__init__(parent)
        self.setWindowTitle("配装总属性")

        layout = QVBoxLayout(self)

        layout.addWidget(toolbox := QToolBox())

        attribute_layout = QVBoxLayout(attribute_page := QWidget())
        translates, _ = get_translates(attributes)
        for k, v in attributes.items():
            attribute_layout.addWidget(LabelRow(translates[k], QLabel(str(v))))
        toolbox.addItem(attribute_page, "属性")

        if recipes:
            recipe_layout = QVBoxLayout(recipe_page := QWidget())
            for recipe in recipes:
                recipe_layout.addWidget(LabelRow("秘籍:", QLabel(recipe)))
            toolbox.addItem(recipe_page, "秘籍")
        if gains:
            gain_layout = QVBoxLayout(gain_page := QWidget())
            for gain in gains:
                if not gain.name:
                    continue
                gain_layout.addWidget(LabelRow(f"{gain.name}:", check_box := QCheckBox()))
                check_box.setChecked(gain.average)
                check_box.stateChanged.connect(self.set_gain_average(gain))
            toolbox.addItem(gain_page, "特效")

    @staticmethod
    def set_gain_average(gain: GearGain):
        def inner(state):
            gain.average = state

        return inner
