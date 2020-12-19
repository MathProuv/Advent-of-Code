import inputAoC as aoc
import my_utils
import re

rules_aoc, matching_aoc = aoc.get_input_file(19, 2020).split("\n\n")

ex = '''0: 4 1
6: 0 5
1: 2 3 | 3 2
2: 4 4 | 5 5
3: 4 5 | 5 4
4: "a"
5: "b"
7: 4 5
14: 7 7
21: 7 14
28: 14 14
8: 7 | 4
9: 4 | 7
10: 2 3 | 3 2
11: 3 2 | 2 3'''.splitlines()
messages_ex = '''ababbb
bababa
abbbab
aaabbb
aaaabbb'''.splitlines()

rules = rules_aoc.splitlines()
messages = matching_aoc.splitlines()


def concat_2vals_set(v1, v2):
    if type(v1) == str and type(v2) == str:
        return v1 + v2
    elif type(v1) == set and type(v2) == set:
        return set([concat_2vals_set(v,w) for v in v1 for w in v2])
    elif type(v1) == set:
        return set([concat_2vals_set(v, v2) for v in v1])
    elif type(v2) == set:
        return set([concat_2vals_set(v1, v) for v in v2])
    else:
        print("pb concat", v1, v2)
        return [v1, v2]


def pip_2vals_set(v1, v2):
    if type(v1) == str and type(v2) == str:
        return set((v1, v2))
    elif type(v1) == set and type(v2) == set:
        return v1.union(v2)
    elif type(v1) == set and type(v2) == str:
        return v1.union(set((v2,)))
    elif type(v1) == str and type(v2) == set:
        return v2.union(set((v1,)))
    else:
        print("pb pipe", v1, v2)
        return (v1, v2)



def get_value(rule, values):
    val = re.match(r"^\"([a-z])\"$", rule)
    one_rule = re.match(r"^(\d+)$", rule)
    rules = re.match(r"^(\d+) (\d+)$", rule)
    pipe = re.match(r"^(.+) \| (.+)$", rule)
    if val:
        return val.groups()[0]
    elif one_rule:
        r1 = int(one_rule.groups()[0])
        if r1 in values:
            return values[r1]
    elif rules:
        r1, r2 = [int(r) for r in rules.groups()]
        if r1 in values and r2 in values:
            v1, v2 = values[r1], values[r2]
            return concat_2vals_set(v1, v2)
    elif pipe:
        rul1, rul2 = pipe.groups()
        v1, v2 = get_value(rul1, values), get_value(rul2, values)
        if v1 and v2:
            return pip_2vals_set(v1, v2)
    else:
        print("no matching")



def constr_values(rules: [str]):
    values = dict()
    rules = rules[::]
    repeat = True
    while repeat:
        repeat = False
        to_remove = []
        for rule in rules:
            i = rule.index(":")
            n, r = int(rule[:i]), rule[i+2:] #len(": ")
            val = get_value(r, values)
            if val != None:
                # print(rule, val)
                repeat = True
                values[n] = val
                to_remove.append(rule)
        for to_rem in to_remove:
            rules.remove(to_rem)
    assert len(rules) == 0
    return values

def count_valids(messages, values, rule):
    return len(set(messages).intersection(values[rule]))


vals_ex = constr_values(ex)
my_utils.print_dict(vals_ex)

print("res ex", count_valids(messages_ex, vals_ex, 6))

vals = constr_values(rules)
print("nb de possibilités",len(vals[0]))

res1 = count_valids(messages, vals, 0)
print(res1)
