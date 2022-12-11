import inputAoC as aoc
import re

data = aoc.get_input_file(11,2022)

regex = """Monkey \d+:
  Starting items: (\d+[, \d+]*)
  Operation: new = old (\*|\+) (old|\d+)
  Test: divisible by (\d+)
    If true: throw to monkey (\d+)
    If false: throw to monkey (\d+)"""
class Monkey:
    def __init__(self,data) -> None:
        args = re.match(regex,data).groups()
        self.items = list(map(int, args[0].split(', ')))
        op, d = args[1], args[2]
        if d == "old": self.operation = lambda old:old**2
        elif op == "*": self.operation = lambda old:old*int(d)
        else: self.operation = lambda old:old+int(d)
        prime, if_true, if_false = int(args[3]), int(args[4]), int(args[5])
        self.test = lambda new: if_false if new%prime else if_true
        self.nb_inspections = 0

monkeys = []
for data_monkey in data.split('\n\n'):
    monkeys.append(Monkey(data_monkey))

n = len(monkeys)
operations = [monkey.operation for monkey in monkeys]
tests = [monkey.test for monkey in monkeys]
items = [monkey.items for monkey in monkeys]
nb_inspections = [monkey.nb_inspections for monkey in monkeys]

primes = [2,3,5,7,11,13,17,19]
prod = 1
for p in primes: prod *= p
def round():
    for monkey in range(n):
        for item in items[monkey]:
            new = operations[monkey](item)
            new %= prod
            n_monkey = tests[monkey](new)
            items[n_monkey].append(new)
        nb_inspections[monkey] += len(items[monkey])
        items[monkey].clear()

for r in range(10000):
    if not r%1000: print("round",r)
    round()

nb_inspections_sorted = sorted(nb_inspections)
res1 = nb_inspections_sorted[-1] * nb_inspections_sorted[-2]
print(res1)
