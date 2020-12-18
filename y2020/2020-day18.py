import inputAoC as aoc
from functools import reduce
from collections import deque

exprs = aoc.get_input_file(18,2020).splitlines()

def eval_parentheses(expr, fct_eval):
    while "(" in expr:
        expr1 = ""
        i, par = expr.index("(") + 1, 1
        while par:
            carac = expr[i]
            if carac == ")": par -= 1
            if carac == "(": par += 1
            expr1 += carac
            i += 1
        res1 = fct_eval(expr1[:-1])
        expr = expr.replace("(" + expr1, str(res1))
    return expr

def evaluate(expr: str) -> int:
    expr = eval_parentheses(expr, evaluate)

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

def evaluate2(expr):
    expr = eval_parentheses(expr, evaluate2)

    parts = expr.split()
    while "+" in parts:
        i = parts.index("+")
        a, b = int(parts[i-1]), int(parts[i+1])
        del parts[i:i+2]
        parts[i-1] = a + b
    
    while "*" in parts:
        i = parts.index("*")
        a, b = int(parts[i-1]), int(parts[i+1])
        del parts[i:i+2]
        parts[i-1] = a * b
    
    return int(parts[0])

res2 = sum([evaluate2(expr) for expr in exprs])
print(res2)