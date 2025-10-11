from qt.classes.dot import Dot
from qt.classes.skill import Skill


def percent(num):
    return round(num * 100, 2)


def evaluate_skill(skill: Skill, variables: dict):
    damage = skill.damage.evaluate(variables) * skill.count
    critical_strike = skill.critical_strike.evaluate(variables)
    critical_damage = skill.critical_damage.evaluate({**variables, "damage": damage})
    expected_damage = damage * (1 - critical_strike) + critical_damage * critical_strike
    return damage, critical_strike, critical_damage, expected_damage


def evaluate_dot(dot: Dot, variables: dict):
    damage = dot.source.damage.evaluate({**variables, "tick": dot.tick}) * dot.stack * dot.count
    critical_strike = dot.source.critical_strike.evaluate(variables)
    critical_damage = dot.source.critical_damage.evaluate({**variables, "damage": damage})
    expected_damage = damage * (1 - critical_strike) + critical_damage * critical_strike
    return damage, critical_strike, critical_damage, expected_damage
