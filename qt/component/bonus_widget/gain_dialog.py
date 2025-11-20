from PySide6.QtWidgets import QCheckBox, QDialog, QVBoxLayout, QWidget

from qt import LabelRow
from qt.classes.gains.formation import FormationGain
from qt.classes.gains.team import TeamGain


class GainDialog(QDialog):
    def __init__(self, gains: dict[str, FormationGain | TeamGain], parent: QWidget = None):
        super().__init__(parent)
        self.setWindowTitle("均摊选项")

        layout = QVBoxLayout(self)

        for name, gain in gains.items():
            layout.addWidget(LabelRow(f"{name}:", check_box := QCheckBox()))
            check_box.setChecked(gain.average)
            check_box.stateChanged.connect(self.set_gain_average(gain))

    def set_gain_average(self, gain: FormationGain | TeamGain):
        def inner(state):
            gain.average = state

        return inner
