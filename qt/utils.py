from base.expression import Constant, Min
from qt.classes.dot import Dot
from qt.classes.skill import Skill


def percent(num):
    return f"{round(num * 100, 2)}%"


def evaluate_skill(skill: Skill, variables: dict, count: float = 1):
    hit_damage = 0
    for damage in skill.damages:
        hit_damage += damage.evaluate(variables)
    hit_damage *= count
    if skill.critical_strike == 0:
        critical_strike = Constant(0)
    else:
        critical_strike = Min(skill.critical_strike.evaluate(variables), 1)
    if skill.critical_power == 0:
        critical_power = Constant(0)
    else:
        critical_power = skill.critical_power.evaluate(variables)
    critical_damage = hit_damage * critical_power
    expected_damage = hit_damage * (1 - critical_strike) + critical_damage * critical_strike
    return hit_damage, critical_strike, critical_damage, expected_damage


def evaluate_dot(dot: Dot, variables: dict):
    count = dot.stack * dot.consume_tick
    return evaluate_skill(dot.source, variables, count)
