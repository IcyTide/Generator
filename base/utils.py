from base.expression import Ceil, Expression, Int, Max, Min, Variable


def get_variables(formula: str) -> dict[str, Variable]:
    variable = ""
    variables = {}

    for c in formula:
        if c.isalpha() or c == "_":
            variable += c
        elif variable:
            if c.isnumeric():
                variable += c
            else:
                variables[variable] = Variable(variable)
                variable = ""
    variables[variable] = Variable(variable)
    return variables


def parse_expr(formula: str) -> Expression:
    variables = get_variables(formula)
    expr = eval(formula, {
        **variables,
        "int": Int, "ceil": Ceil, "max": Max, "min": Min
    })
    return expr