from qt.classes.gains.consumable import Consumables
from qt.classes.kungfu import Kungfu
from qt.component.bonus_widget.widget import BonusWidget, ConsumableWidget


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
                return
            self.parent.consumables[belong] = consumable
            self.parent.update_kungfu()
        return inner

    def init(self, consumables: Consumables):
        for belong, combo in self.widget.consumable_combos.items():
            combo.setCurrentText(consumables.get(belong))


class BonusScript:
    kungfu: Kungfu

    consumables: Consumables

    def __init__(self, bonus_widget: BonusWidget):
        self.widget = bonus_widget

        self.consumable_script = ConsumableScript(self.widget.consumable_widget, self)

    def init(self, kungfu: Kungfu, consumables: Consumables = None):
        self.kungfu = kungfu

        if not consumables:
            self.consumables = Consumables()
        else:
            self.consumables = consumables

        self.consumable_script.init(self.consumables)

        return dict(consumables=self.consumables)

    def update_kungfu(self):
        attributes = self.consumables.content
        gains = {}
        self.kungfu.bonus_attributes = attributes
        self.kungfu.bonus_gains = gains