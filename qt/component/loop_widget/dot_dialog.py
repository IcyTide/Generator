from PySide6.QtWidgets import QDialog, QDoubleSpinBox, QHBoxLayout, QLabel, QPushButton, QSpinBox, QVBoxLayout, QWidget

from base.constant import LEVEL_VARIABLES, SHIELD_BASE_MAP
from qt import ComboBox, LabelRow
from qt.classes.attribute import Attribute
from qt.classes.dot import Dot
from qt.component.loop_widget.skill_dialog import SkillEditorDialog
from qt.component.loop_widget.widget import LoopWidget
from qt.utils import evaluate_dot


class SourceSkillEditorDialog(SkillEditorDialog):
    def __init__(self, max_stack: int, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.count_row.set_label("层数:")
        self.count_spin.setDecimals(0)
        self.count_spin.setMaximum(max_stack)


class DotEditorDialog(QDialog):
    dots: dict[str, dict[int, dict[int, dict]]]
    dot: Dot = None

    def __init__(self, dots: dict = None, dot: Dot = None, parent: LoopWidget = None):
        super().__init__(parent)
        self.setWindowTitle("编辑持续伤害")
        layout = QVBoxLayout(self)
        self.dots = dots
        self.belong_combo = ComboBox()
        self.id_combo = ComboBox()
        self.level_combo = ComboBox()
        self.source_button = QPushButton("")
        self.consume_tick_spin = QSpinBox(minimum=1, value=1)
        self.current_tick_spin = QSpinBox(minimum=1, value=1)
        self.count_spin = QDoubleSpinBox(minimum=0.01, value=1, singleStep=1)

        layout.addWidget(LabelRow("类别:", self.belong_combo))
        layout.addWidget(LabelRow("ID:", self.id_combo))
        layout.addWidget(LabelRow("等级:", self.level_combo))
        layout.addWidget(LabelRow("技能来源:", self.source_button))
        layout.addWidget(LabelRow("吞噬跳数:", self.consume_tick_spin))
        layout.addWidget(LabelRow("当前跳数:", self.current_tick_spin))
        layout.addWidget(LabelRow("数量:", self.count_spin))

        self.name_label = QLabel("")
        self.comment_label = QLabel("")
        layout.addWidget(LabelRow("名称:", self.name_label))
        layout.addWidget(LabelRow("注释:", self.comment_label))

        layout.addLayout((btn_layout := QHBoxLayout()))
        btn_layout.addWidget((ok_button := QPushButton("确定")))
        btn_layout.addWidget((cancel_button := QPushButton("取消")))

        ok_button.clicked.connect(self.accept)
        cancel_button.clicked.connect(self.reject)
        self.belong_combo.currentTextChanged.connect(self.select_belong)
        self.id_combo.currentTextChanged.connect(self.select_id)
        self.level_combo.currentTextChanged.connect(self.select_level)
        self.source_button.clicked.connect(self.select_source)
        self.consume_tick_spin.valueChanged.connect(self.select_consume_tick)
        self.current_tick_spin.valueChanged.connect(self.select_current_tick)
        self.count_spin.valueChanged.connect(self.select_count)

        if dots:
            self.belong_combo.set_items(list(dots))
        if dot:
            self.belong_combo.setCurrentText(dot.belong)
            self.id_combo.setCurrentText(str(dot.dot_id))
            self.level_combo.setCurrentText(str(dot.dot_level))
            if dot.source:
                self.dot.source = dot.source.copy()
                self.source_button.setText(str(self.dot.source))
            self.consume_tick_spin.setValue(dot.consume_tick)
            self.current_tick_spin.setValue(dot.current_tick)
            self.count_spin.setValue(dot.count)

    def select_belong(self, belong: str):
        if belong not in self.dots:
            return
        self.id_combo.set_items(list(self.dots[belong]))

    def select_id(self, dot_id: str):
        if not dot_id:
            return
        belong = self.belong_combo.currentText()
        dot_id = int(dot_id)
        self.level_combo.set_items([str(level) for level in self.dots[belong][dot_id]])

    def select_level(self, dot_level: str):
        if not dot_level:
            return
        belong = self.belong_combo.currentText()
        dot_id = int(self.id_combo.currentText())
        dot_level = int(dot_level)
        count = self.count_spin.value()
        consume_tick = self.consume_tick_spin.value()
        current_tick = self.current_tick_spin.value()

        self.dot = Dot(belong, dot_id, dot_level, count, **self.dots[belong][dot_id][dot_level])
        self.dot.consume_tick = min(consume_tick, self.dot.max_tick)
        self.dot.current_tick = min(current_tick, self.dot.max_tick)

        self.source_button.setText("选择来源")
        self.consume_tick_spin.setMaximum(self.dot.max_tick)
        self.consume_tick_spin.setValue(self.dot.consume_tick)
        self.current_tick_spin.setMaximum(self.dot.max_tick)
        self.current_tick_spin.setValue(self.dot.current_tick)
        self.name_label.setText(self.dot.name)
        self.comment_label.setText(self.dot.comment)

    def select_source(self):
        if not self.dot:
            return
        skills = {self.dot.name: self.dot.skills}
        dialog = SourceSkillEditorDialog(self.dot.max_stack, skill=self.dot.source, skills=skills, parent=self)
        if dialog.exec() == QDialog.DialogCode.Accepted and (skill := dialog.skill):
            self.dot.source = skill
            self.source_button.setText(str(skill))

    def select_consume_tick(self, tick: int):
        if not self.dot:
            return
        self.dot.consume_tick = tick

    def select_current_tick(self, tick: int):
        if not self.dot:
            return
        self.dot.current_tick = tick

    def select_count(self, count: float):
        if not self.dot:
            return
        count = int(count) if int(count) == count else count
        self.dot.count = count


class DotDamageDialog(QDialog):
    def __init__(
            self, dot: Dot, current: Attribute, snapshot: Attribute, parent: QWidget = None
    ):
        super().__init__(parent)
        self.setWindowTitle("持续伤害细节")

        layout = QVBoxLayout(self)

        variables = {**current.current, **snapshot.snapshot}
        self.damage, self.critical_strike, self.critical_damage, self.expected_damage = evaluate_dot(dot, variables)

        layout.addWidget(LabelRow("名称:", QLabel(dot.name)))
        layout.addWidget(LabelRow("ID:", QLabel(str(dot.dot_id))))
        layout.addWidget(LabelRow("等级:", QLabel(str(dot.dot_level))))
        layout.addWidget(LabelRow("层数:", QLabel(str(dot.stack))))
        layout.addWidget(LabelRow("吞噬跳数:", QLabel(str(dot.consume_tick))))
        layout.addWidget(LabelRow("当前跳数:", QLabel(str(dot.current_tick))))
        layout.addWidget(LabelRow("数量:", QLabel(str(dot.count))))
        self.target_level = ComboBox()
        layout.addWidget(LabelRow("目标等级:", self.target_level))
        self.critical_strike_label = QLabel("")
        layout.addWidget(LabelRow("期望会心:", self.critical_strike_label))
        self.damage_label = QLabel("")
        layout.addWidget(LabelRow("命中伤害:", self.damage_label))
        self.critical_damage_label = QLabel("")
        layout.addWidget(LabelRow("会心伤害:", self.critical_damage_label))
        self.expected_damage_label = QLabel("")
        layout.addWidget(LabelRow("期望伤害:", self.expected_damage_label))

        self.target_level.currentTextChanged.connect(self.select_target_level)
        self.target_level.set_items(SHIELD_BASE_MAP)

    def select_target_level(self, level):
        if not level:
            return
        level = int(level)
        variables = LEVEL_VARIABLES(level)
        critical_strike = self.critical_strike.evaluate(variables)
        self.critical_strike_label.setText(f"{round(critical_strike * 100, 2)}%")
        damage = int(self.damage.evaluate(variables))
        self.damage_label.setText(str(damage))
        critical_damage = int(self.critical_damage.evaluate(variables))
        self.critical_damage_label.setText(str(critical_damage))
        expected_damage = int(self.expected_damage.evaluate(variables))
        self.expected_damage_label.setText(str(expected_damage))
