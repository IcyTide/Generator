from qt.classes.gains.consumable import Consumables
from qt.classes.gains.formation import FormationGains
from qt.classes.gains.team import TeamGains
from qt.classes.kungfu import Kungfu
from qt.component.bonus_widget.gain_dialog import GainDialog
from qt.component.bonus_widget.widget import BonusWidget, ConsumableWidget, FormationWidget, TeamWidget


class ConsumableScript:
    def __init__(self, consumable_widget: ConsumableWidget, bonus_script: "BonusScript"):
        self.widget = consumable_widget
        self.parent = bonus_script

        self.connect()

    def connect(self):
        for belong, combo in self.widget.consumable_combos.items():
            combo.currentTextChanged.connect(self.select_consumable(belong))

    def select_consumable(self, belong):
        def inner(consumable: str):
            if not consumable:
                self.parent.consumables.pop(belong)
            else:
                self.parent.consumables[belong] = consumable
            self.parent.update_kungfu()

        return inner

    def init(self, consumables: Consumables):
        for belong, combo in self.widget.consumable_combos.items():
            combo.setCurrentText(consumables.get(belong))


class FormationScript:
    def __init__(self, formation_widget: FormationWidget, bonus_script: "BonusScript"):
        self.widget = formation_widget
        self.parent = bonus_script

        self.connect()

    def connect(self):
        self.widget.average_button.clicked.connect(self.set_average)
        self.widget.belong_combo.currentTextChanged.connect(self.select_formation)
        self.widget.level_4_spin.valueChanged.connect(self.select_level_4)
        self.widget.level_5_spin.valueChanged.connect(self.select_level_5)
        self.widget.level_6_spin.valueChanged.connect(self.select_level_6)

    def set_average(self):
        if gains := self.parent.formation_gains.content:
            GainDialog(gains, parent=self.widget).exec()

    def select_formation(self, formation: str):
        if not formation:
            self.parent.formation_gains.formation = ""
            self.widget.level_4_spin.setValue(0)
            self.widget.level_5_spin.setValue(0)
            self.widget.level_6_spin.setValue(0)
            self.parent.update_kungfu()
            return
        self.parent.formation_gains.formation = formation
        level_4_rate, level_5_rate, level_6_rate = self.parent.formation_gains.get(formation)
        self.widget.level_4_spin.setValue(level_4_rate)
        self.widget.level_5_spin.setValue(level_5_rate)
        self.widget.level_6_spin.setValue(level_6_rate)

        self.parent.update_kungfu()

    def select_level_4(self, level_4_rate: float):
        if not self.parent.formation_gains.formation:
            return
        self.parent.formation_gains.rates[self.parent.formation_gains.formation][0] = level_4_rate
        self.parent.update_kungfu()

    def select_level_5(self, level_5_rate: float):
        if not self.parent.formation_gains.formation:
            return
        self.parent.formation_gains.rates[self.parent.formation_gains.formation][1] = level_5_rate
        self.parent.update_kungfu()

    def select_level_6(self, level_6_rate: float):
        if not self.parent.formation_gains.formation:
            return
        self.parent.formation_gains.rates[self.parent.formation_gains.formation][2] = level_6_rate
        self.parent.update_kungfu()

    def init(self, formation_gains: FormationGains):
        if formation := formation_gains.formation:
            self.widget.belong_combo.setCurrentText(formation)
        else:
            self.widget.belong_combo.setCurrentText("")


class TeamGainScript:
    def __init__(self, team_widget: TeamWidget, bonus_script: "BonusScript"):
        self.widget = team_widget
        self.parent = bonus_script

        self.connect()

    def connect(self):
        self.widget.average_button.clicked.connect(self.set_average)
        self.widget.belong_combo.currentTextChanged.connect(self.select_team)
        self.widget.stack_spin.valueChanged.connect(self.select_stack)
        self.widget.rate_spin.valueChanged.connect(self.select_rate)

    def set_average(self):
        if gains := self.parent.team_gains.content:
            GainDialog(gains, parent=self.widget).exec()

    def select_team(self, gain_name: str):
        if not gain_name:
            self.widget.stack_spin.setValue(0)
            self.widget.rate_spin.setValue(0)
            return
        team_gain = self.parent.team_gains.get(gain_name)
        stack, max_stack, rate = team_gain.stack, team_gain.max_stack, team_gain.rate
        self.widget.stack_spin.setMaximum(max_stack)
        self.widget.stack_spin.setValue(stack)
        self.widget.rate_spin.setValue(rate)

    def select_stack(self, stack: int):
        gain_name = self.widget.belong_combo.currentText()
        if not gain_name:
            return
        team_gain = self.parent.team_gains.get(gain_name)
        team_gain.stack = stack
        self.parent.update_kungfu()

    def select_rate(self, rate: float):
        gain_name = self.widget.belong_combo.currentText()
        if not gain_name:
            return
        team_gain = self.parent.team_gains.get(gain_name)
        team_gain.rate = rate
        self.parent.update_kungfu()

    def init(self, team_gains: TeamGains):
        ...


class BonusScript:
    kungfu: Kungfu

    consumables: Consumables

    formation_gains: FormationGains

    team_gains: TeamGains

    def __init__(self, bonus_widget: BonusWidget):
        self.widget = bonus_widget

        self.consumable_script = ConsumableScript(self.widget.consumable_widget, self)
        self.formation_script = FormationScript(self.widget.formation_widget, self)
        self.team_script = TeamGainScript(self.widget.team_widget, self)

    def init(
            self, kungfu: Kungfu,
            consumables: Consumables | dict = None,
            formation_gains: FormationGains | dict = None,
            team_gains: TeamGains | dict = None
    ):
        self.kungfu = kungfu

        if not consumables:
            self.consumables = Consumables()
        elif isinstance(consumables, Consumables):
            self.consumables = consumables
        else:
            self.consumables = Consumables.from_dict(consumables)

        if not formation_gains:
            self.formation_gains = FormationGains()
        elif isinstance(formation_gains, FormationGains):
            self.formation_gains = formation_gains
        else:
            self.formation_gains = FormationGains.from_dict(formation_gains)

        if not team_gains:
            self.team_gains = TeamGains()
        elif isinstance(team_gains, TeamGains):
            self.team_gains = team_gains
        else:
            self.team_gains = TeamGains.from_dict(team_gains)

        self.consumable_script.init(self.consumables)
        self.formation_script.init(self.formation_gains)
        self.team_script.init(self.team_gains)

        return dict(consumables=self.consumables, formation=self.formation_gains, team_gains=self.team_gains)

    def update_kungfu(self):
        attributes = self.consumables.content
        gains = self.formation_gains.content | self.team_gains.content
        self.kungfu.bonus_attributes = attributes
        self.kungfu.bonus_gains = gains
