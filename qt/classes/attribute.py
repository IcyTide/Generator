import math

from base.attribute import BaseAttribute
from base.constant import *
from base.expression import Expression, Variable
from qt.classes.buff import Buff
from tools.lua.enums import SKILL_KIND_TYPE


class Target(BaseAttribute):
    level: Expression = Variable("level")
    shield_constant: Expression = Variable("shield_constant")

    physical_shield_base: Expression = Variable("shield_base")
    solar_shield_base: Expression = Variable("shield_base")
    lunar_shield_base: Expression = Variable("shield_base")
    neutral_shield_base: Expression = Variable("shield_base")
    poison_shield_base: Expression = Variable("shield_base")


class Attribute(BaseAttribute):
    level: int = LEVEL

    buffs: dict[str, float]
    recipes: list[str]
    belongs: list[str]

    def __init__(self, major_type: str, damage_type: str, critical_type: str):
        super().__init__(major_type, damage_type, critical_type)

        self.buffs = {}
        self.recipes, self.belongs = [], []

        self.target = Target(major_type, damage_type, critical_type)

    @property
    def current(self):
        variables: dict = {**self.buffs, **EXTRA_VARIABLES}
        for e in SKILL_KIND_TYPE:
            for template in CURRENT_VARIABLE_TEMPLATES:
                attr = template.format(e)
                variables[attr] = self[attr]
            for template in TARGET_VARIABLE_TEMPLATES:
                attr = template.format(e)
                variables[attr] = self.target[attr]
        for attr in CURRENT_VARIABLES:
            variables[attr] = self[attr]
        for attr in TARGET_VARIABLES:
            variables[attr] = self.target[attr]
        return variables

    @property
    def snapshot(self):
        variables: dict = {recipe: 1. for recipe in self.recipes + self.belongs}
        for e in SKILL_KIND_TYPE:
            for template in SNAPSHOT_VARIABLE_TEMPLATES:
                attr = template.format(e)
                variables[attr] = self[attr]
        for attr in SNAPSHOT_VARIABLES:
            variables[attr] = self[attr]
        return variables

    def add_buff(self, buff: Buff):
        if buff.buff_key:
            self.buffs[buff.buff_key] = buff.stack * buff.buff_level
        else:
            attribute = self.target if buff.on_target else self
            for k, v in buff.attributes.items():
                if not hasattr(attribute, k):
                    continue
                attribute[k] += math.ceil(v * buff.stack)
        self.recipes += buff.recipes

    def sub_buff(self, buff: Buff):
        if buff.buff_key:
            self.buffs.pop(buff.buff_key, None)
        else:
            attribute = self.target if buff.on_target else self
            for k, v in buff.attributes.items():
                attribute[k] -= math.ceil(v * buff.stack)
        for recipe in buff.recipes:
            if recipe in self.recipes:
                self.recipes.remove(recipe)

    def require_grad(self):
        for attr in GRAD_VARIABLES:
            self[attr] += Variable(attr)
