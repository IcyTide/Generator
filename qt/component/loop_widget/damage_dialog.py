from PySide6.QtWidgets import QDialog, QLabel, QSizePolicy, QToolBox, QVBoxLayout, QWidget

from base.constant import GRAD_VARIABLES, LEVEL_VARIABLES, SHIELD_BASE_MAP
from base.translate import get_translates
from qt import ComboBox, LabelRow, Table
from qt.classes.attribute import Attribute
from qt.classes.buff import Buff, BuffType
from qt.classes.damage import Damage
from qt.utils import percent


def add_buffs_to_attributes(buffs: list[Buff], current: Attribute, snapshot: Attribute = None):
    for buff in buffs:
        if buff.buff_type == BuffType.Both:
            current.add_buff(buff)
            if snapshot:
                snapshot.add_buff(buff)
        elif buff.buff_type == BuffType.Current:
            current.add_buff(buff)
        elif snapshot and buff.buff_type == BuffType.Snapshot:
            snapshot.add_buff(buff)


def sub_buffs_to_attributes(buffs: list[Buff], current: Attribute, snapshot: Attribute = None):
    for buff in buffs:
        if buff.buff_type == BuffType.Both:
            current.sub_buff(buff)
            if snapshot:
                snapshot.sub_buff(buff)
        elif buff.buff_type == BuffType.Current:
            current.sub_buff(buff)
        elif snapshot and buff.buff_type == BuffType.Snapshot:
            snapshot.sub_buff(buff)


class DamagesDialog(QDialog):
    duration: float = 0.

    damages: dict[str, Damage] = {}

    def __init__(self, name: str, count: int, parent: QWidget = None):
        super().__init__(parent)
        self.setWindowTitle("伤害细节")
        layout = QVBoxLayout(self)
        self.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        self.tool_box = QToolBox()
        layout.addWidget(self.tool_box)
        sub_layout = QVBoxLayout(sub_page := QWidget())
        sub_layout.addWidget(LabelRow("名称:", QLabel(name)))
        sub_layout.addWidget(LabelRow("数量:", QLabel(str(count))))
        sub_layout.addWidget(LabelRow("时长:", QLabel(str(self.duration))))
        self.target_level = ComboBox()
        sub_layout.addWidget(LabelRow("目标等级:", self.target_level))
        self.total_damage_label = QLabel("")
        sub_layout.addWidget(LabelRow("期望总伤害:", self.total_damage_label))
        self.dps_label = QLabel("")
        sub_layout.addWidget(LabelRow("期望DPS:", self.dps_label))
        self.tool_box.addItem(sub_page, "概述")

        sub_layout = QVBoxLayout(sub_page := QWidget())
        self.grad_labels: dict[str, QLabel] = {}
        translates, _ = get_translates(GRAD_VARIABLES)
        for attr in GRAD_VARIABLES:
            self.grad_labels[attr] = grad_label = QLabel("")
            sub_layout.addWidget(LabelRow(f"{translates[attr]}:", grad_label))
        self.tool_box.addItem(sub_page, "收益")

        sub_layout = QVBoxLayout(sub_page := QWidget())
        self.damage_table = Table(["名称", "次数", "伤害", "占比"])
        sub_layout.addWidget(self.damage_table)
        self.tool_box.addItem(sub_page, "统计")

        self.target_level.currentTextChanged.connect(self.select_target_level)
        self.target_level.set_items(SHIELD_BASE_MAP)

    def select_target_level(self, level):
        if not level:
            return
        level = int(level)
        variables = LEVEL_VARIABLES(level)
        damages, grad_damages = {}, {attr: 0 for attr in GRAD_VARIABLES}
        for name, damage in self.damages.items():
            damages[name] = int(damage.formula.evaluate(variables))
            for attr, delta in GRAD_VARIABLES.items():
                grad_damages[attr] += damage.formula.evaluate({**variables, attr: delta})
        total_damage = sum(damages.values())
        for attr, grad_damage in grad_damages.items():
            gradient = percent(grad_damage / total_damage - 1)
            self.grad_labels[attr].setText(str(gradient))

        damages_data = [
            (name, round(self.damages[name].count, 2), damage, percent(damage / total_damage))
            for name, damage in sorted(damages.items(), key=lambda x: x[1], reverse=True)
        ]
        self.damage_table.refresh_table(damages_data)
        self.total_damage_label.setText(str(total_damage))
        duration = self.duration if self.duration else 1
        dps = int(total_damage / duration)
        self.dps_label.setText(str(dps))
