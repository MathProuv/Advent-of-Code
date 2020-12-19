import inputAoC as aoc
import my_utils
import re

rules_aoc, matching_aoc = aoc.get_input_file(19, 2020).split("\n\n")


"""rules = dict()

for rule in rules_aoc.splitlines():
    index = rule.index(":")
    nb = int(rule[:index])
    real_rule = rule[index+2:]
    rules[nb] = real_rule"""

rules = rules_aoc.splitlines()
messages = matching_aoc.splitlines()

def concat_2vals(v1, v2):
    if type(v1) == str and type(v2) == str:
        return v1 + v2
    elif type(v1) == tuple and type(v2) == tuple:
        return tuple([concat_2vals(v,w) for v in v1 for w in v2])
    elif type(v1) == tuple:
        return tuple([concat_2vals(v, v2) for v in v1])
    elif type(v2) == tuple:
        return tuple([concat_2vals(v1, v) for v in v2])
    else:
        print("pb concat", v1, v2)
        return [v1, v2]

def pip_2vals(v1, v2):
    if type(v1) == str and type(v2) == str:
        return (v1, v2)
    elif type(v1) == tuple or type(v2) == tuple:
        return tuple(v1) + tuple(v2)
    else:
        print("pb concat", v1, v2)
        return (v1, v2)

def get_value(rule, values):
    val = re.match(r"^\"([a-z])\"$", rule)
    one_rule = re.match(r"^(\d+)$", rule)
    rules = re.match(r"^(\d+) (\d+)$", rule)
    pipe = re.match(r"^(.+) \| (.+)$", rule)
    if val:
        return val.groups()[0]
    if one_rule:
        r1 = int(one_rule.groups()[0])
        if r1 in values:
            return values[r1]
    elif rules:
        r1, r2 = [int(r) for r in rules.groups()]
        if r1 in values and r2 in values:
            v1, v2 = values[r1], values[r2]
            return concat_2vals(v1, v2)
    elif pipe:
        rul1, rul2 = pipe.groups()
        v1, v2 = get_value(rul1, values), get_value(rul2, values)
        if v1 and v2:
            return pip_2vals(v1, v2)
    else:
        print("no matching")



def constr_values(rules: [str]):
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
                # print(rule, val)
                repeat = True
                values[n] = val
                rules.remove(rule)
    return values

def count_valids(messages, values, rule):
    res = 0
    for message in messages:
        res += message in values[rule]
    return res

ex = '''0: 4 1
6: 0 5
1: 2 3 | 3 2
2: 4 4 | 5 5
3: 4 5 | 5 4
4: "a"
5: "b"'''

vals = constr_values(ex.splitlines())
my_utils.print_dict(vals)



vals = constr_values(rules)
my_utils.print_dict(vals)

res1 = count_valids(messages, vals, 0)
print(res1)