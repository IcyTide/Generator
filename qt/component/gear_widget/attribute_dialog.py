from PySide6.QtWidgets import QDialog, QLabel, QToolBox, QVBoxLayout, QWidget

from base.translate import get_translates
from qt import LabelRow


class AttributeDialog(QDialog):

    def __init__(self, attributes: dict[str, int], recipes: list[str], gains: list[str], parent: QWidget = None):
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
                gain_layout.addWidget(LabelRow("特效:", QLabel(gain)))
            toolbox.addItem(gain_page, "特效")
