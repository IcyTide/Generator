from base.constant import EXTRA_VARIABLES
from base.expression import Constant, Expression, Variable
from qt.classes.dot import Dot
from qt.classes.skill import Skill


def percent(num):
    return f"{round(num * 100, 2)}%"


def evaluate_critical_strike(skill: Skill, variables: dict):
    if skill.critical_strike == 0:
        return Constant(0)
    else:
        return skill.critical_strike.evaluate(variables)


def evaluate_damage(skill: Skill, variables: dict, count: float = 1):
    total_damage = 0
    for damage in skill.damages:
        if isinstance(damage, Expression):
            total_damage += damage.evaluate(variables)
        else:
            total_damage += damage
    total_damage *= count
    return total_damage


def evaluate_skill(skill: Skill, variables: dict, count: float = 1):
    critical_strike = evaluate_critical_strike(skill, variables)
    total_damage = evaluate_damage(skill, variables | {e: Variable(e) for e in EXTRA_VARIABLES}, count)
    return total_damage, critical_strike


def evaluate_skill_expectation(skill: Skill, variables: dict, count: float = 1):
    critical_strike = evaluate_critical_strike(skill, variables)
    total_damage = evaluate_damage(skill, variables | dict(rand=0.5, is_critical=critical_strike), count)
    return total_damage
