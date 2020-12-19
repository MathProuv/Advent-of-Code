import inputAoC as aoc
import my_utils

rules_aoc, matching = aoc.get_input_file(19, 2020).split("\n\n")

rules = dict()

for rule in rules_aoc.splitlines():
    index = rule.index(":")
    nb = int(rule[:index])
    real_rule = rule[index+2:]
    rules[nb] = real_rule

my_utils.print_dict(rules)