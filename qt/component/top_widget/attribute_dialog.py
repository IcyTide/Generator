from PySide6.QtWidgets import QDialog, QLabel, QToolBox, QVBoxLayout, QWidget

from qt import LabelRow


class AttributeDialog(QDialog):

    def __init__(self, attributes: dict[str, int], recipes: list[str], gains: list[str], parent: QWidget = None):
        super().__init__(parent)
        self.setWindowTitle("Attribute Detail")

        layout = QVBoxLayout(self)

        layout.addWidget(toolbox := QToolBox())

        attribute_layout = QVBoxLayout(attribute_page := QWidget())
        for k, v in attributes.items():
            attribute_layout.addWidget(LabelRow(k, QLabel(str(v))))
        toolbox.addItem(attribute_page, "Attributes")

        if recipes:
            recipe_layout = QVBoxLayout(recipe_page := QWidget())
            for recipe in recipes:
                recipe_layout.addWidget(LabelRow("recipe:", QLabel(recipe)))
            toolbox.addItem(recipe_page, "Recipes")
        if gains:
            gain_layout = QVBoxLayout(gain_page := QWidget())
            for gain in gains:
                gain_layout.addWidget(LabelRow("gain:", QLabel(gain)))
            toolbox.addItem(gain_page, "Gains")
