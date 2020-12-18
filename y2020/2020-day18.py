import inputAoC as aoc

exprs = aoc.get_input_file(18,2020).splitlines()

def eval_parentheses(expr: str, fct_eval) -> str:
    """Renvoit l'expression dont les parenthèses ont été évaluées"""
    while "(" in expr:
        expr1 = "("
        i, par = expr.index("(") + 1, 1
        while par:
            carac = expr[i]
            if carac == ")": par -= 1
            if carac == "(": par += 1
            expr1 += carac
            i += 1
        res1 = fct_eval(expr1[1:-1])
        expr = expr.replace(expr1, str(res1))
    return expr

def evaluate(expr: str) -> int:
    """Renvoit la valeur de l'expression évaluée dans l'ordre: () > + = *"""
    # on évalue les ()
    expr = eval_parentheses(expr, evaluate)

    # on évalue les + et les *
    parts = expr.split()
    temp = int(parts[0])
    op = None
    for part in parts[1:]:
        if part == "+":
            op = lambda a,b: a + b
        elif part == "*":
            op = lambda a,b: a * b
        else:
            temp = op(temp, int(part))
    return temp

res1 = sum([evaluate(expr) for expr in exprs])
print(res1)


def evaluate2(expr: str) -> int:
    """Renvoit la valeur de l'expression évaluée dans l'ordre: () > + > *"""
    # on évalue les ()
    expr = eval_parentheses(expr, evaluate2)

    parts = expr.split()
    # on évalue les +
    while "+" in parts:
        i = parts.index("+")
        a, b = int(parts[i-1]), int(parts[i+1])
        del parts[i:i+2]
        parts[i-1] = a + b
    
    # on évalue les *
    res = 1
    for nb in parts[::2]:
        res *= int(nb)
    
    return res

res2 = sum([evaluate2(expr) for expr in exprs])
print(res2)