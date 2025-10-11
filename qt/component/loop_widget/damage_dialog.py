from PySide6.QtWidgets import QDialog, QLabel, QToolBox, QVBoxLayout, QWidget

from base.constant import GRAD_VARIABLES, LEVEL_VARIABLES, SHIELD_BASE_MAP
from base.expression import Expression
from qt import ComboBox, LabelRow
from qt.utils import percent


class DamagesDialog(QDialog):
    duration: float = 0.

    damages: dict[str, int | Expression] = {}

    def __init__(self, name: str, count:int, parent: QWidget = None):
        super().__init__(parent)
        self.setWindowTitle("Damage Detail")
        layout = QVBoxLayout(self)
        self.tool_box = QToolBox()
        layout.addWidget(self.tool_box)
        sub_layout = QVBoxLayout(sub_page := QWidget())
        sub_layout.addWidget(LabelRow("Name:",  QLabel(name)))
        sub_layout.addWidget(LabelRow("Count:", QLabel(str(count))))
        sub_layout.addWidget(LabelRow("Duration:", QLabel(str(self.duration))))
        self.target_level = ComboBox()
        sub_layout.addWidget(LabelRow("Target Level:", self.target_level))
        self.expected_damage_label = QLabel("")
        sub_layout.addWidget(LabelRow("Expected Damage:", self.expected_damage_label))
        self.expected_dps_label = QLabel("")
        sub_layout.addWidget(LabelRow("Expected DPS:", self.expected_dps_label))
        self.tool_box.addItem(sub_page, "Abstract")

        sub_layout = QVBoxLayout(sub_page := QWidget())
        self.grad_labels: dict[str, QLabel] = {}
        for attr in GRAD_VARIABLES:
            self.grad_labels[attr] = grad_label = QLabel("")
            sub_layout.addWidget(LabelRow(f"{attr}:", grad_label))
        self.tool_box.addItem(sub_page, "Gradient")

        sub_layout = QVBoxLayout(sub_page := QWidget())
        self.damage_labels: dict[str, QLabel] = {}
        for name in self.damages:
            self.damage_labels[name] = damage_label = QLabel("")
            sub_layout.addWidget(LabelRow(name, damage_label))
        self.tool_box.addItem(sub_page, "Details")

        self.target_level.currentTextChanged.connect(self.select_target_level)
        self.target_level.set_items(SHIELD_BASE_MAP)

    def select_target_level(self, level):
        if not level:
            return
        level = int(level)
        variables = LEVEL_VARIABLES(level)
        total_expected_damage = 0
        grad_damages = {attr: 0 for attr in GRAD_VARIABLES}
        for name, damage in self.damages.items():
            expected_damage = int(damage.evaluate(variables))
            self.damage_labels[name].setText(str(expected_damage))
            for attr, delta in GRAD_VARIABLES.items():
                grad_damages[attr] += damage.evaluate({**variables, attr: delta})
            total_expected_damage += expected_damage

        for attr, grad_damage in grad_damages.items():
            gradient = percent(grad_damage / total_expected_damage - 1)
            self.grad_labels[attr].setText(str(gradient))

        self.expected_damage_label.setText(str(total_expected_damage))
        duration = self.duration if self.duration else 1
        expected_dps = int(total_expected_damage / duration)
        self.expected_dps_label.setText(str(expected_dps))
