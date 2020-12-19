import inputAoC as aoc
import my_utils
import re

rules_aoc, matching = aoc.get_input_file(19, 2020).split("\n\n")


"""rules = dict()

for rule in rules_aoc.splitlines():
    index = rule.index(":")
    nb = int(rule[:index])
    real_rule = rule[index+2:]
    rules[nb] = real_rule"""

rules = rules_aoc.splitlines()


def get_value(rule, values):
    val = re.match(r"\"([a-z])\"", rule)
    one_rule = re.match(r"(\d+)", rule)
    rules = re.match(r"(\d+) (\d+)", rule)
    pipe = re.match(r"(.+) \| (.+)", rule)
    if val:
        return val.groups()[0]
    if one_rule:
        r1 = int(one_rule.groups()[0])
        if r1 in values:
            return values[r1]
    elif rules:
        r1, r2 = [int(r) for r in rules.groups()]
        if r1 in values and r2 in values:
            return [values[r1], values[r2]]
    elif pipe:
        rul1, rul2 = pipe.groups()
        r1, r2 = get_value(rul1, values), get_value(rul2, values)
        if r1 and r2:
            return [r1, r2]
    else:
        print("no matching")



def constr_values(rules):
    values = dict()
    rules = rules[::]
    repeat = True
    while repeat:
        repeat = False
        for rule in rules:
            i = rule.index(":")
            n, r = int(rule[:i]), rule[i+2:] #len(": ")
            val = get_value(r, values)
            if val != None:
                repeat = True
                values[n] = val
                rules.remove(rule)
    return values

vals = constr_values(rules)

print(vals)




print(get_value("40 127 | 127 40", vals))