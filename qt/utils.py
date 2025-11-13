from base.expression import Constant, Min
from qt.classes.dot import Dot
from qt.classes.skill import Skill


def percent(num):
    return f"{round(num * 100, 2)}%"


def evaluate_skill(skill: Skill, variables: dict):
    damage = skill.damage.evaluate(variables)
    if skill.critical_strike == 0:
        critical_strike = Constant(0)
    else:
        critical_strike = Min(skill.critical_strike.evaluate(variables), 1)
    critical_damage = skill.critical_damage.evaluate({**variables, "damage": damage})
    expected_damage = damage * (1 - critical_strike) + critical_damage * critical_strike
    return damage, critical_strike, critical_damage, expected_damage


def evaluate_dot(dot: Dot, variables: dict):
    count = dot.stack * dot.consume_tick
    damage = dot.source.damage.evaluate({**variables, "tick": dot.current_tick}) * count
    if dot.source.critical_strike == 0:
        critical_strike = Constant(0)
    else:
        critical_strike = Min(dot.source.critical_strike.evaluate(variables), 1)
    critical_damage = dot.source.critical_damage.evaluate({**variables, "damage": damage})
    expected_damage = damage * (1 - critical_strike) + critical_damage * critical_strike
    return damage, critical_strike, critical_damage, expected_damage
