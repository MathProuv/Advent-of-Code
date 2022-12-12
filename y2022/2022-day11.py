import inputAoC as aoc
import re

data = aoc.get_input_file(11,2022)

regex = """Monkey (\d+):
  Starting items: (\d+[, \d+]*)
  Operation: new = ([old \*\+\d]+)
  Test: divisible by (\d+)
    If true: throw to monkey (\d+)
    If false: throw to monkey (\d+)"""
class Monkey:
    def __init__(self,data) -> None:
        args = re.match(regex,data).groups()
        self.name = int(args[0])
        self.items = list(map(int, args[1].split(', ')))
        self.operation = eval("lambda old:" + args[2])
        self.prime, if_true, if_false = int(args[3]), int(args[4]), int(args[5])
        self.test = lambda new: if_false if new % self.prime else if_true

monkeys = [Monkey(data_monkey) for data_monkey in data.split('\n\n')]
primes = [monkey.prime for monkey in monkeys]
prod = 1
for p in primes: prod *= p

def res(nb,func, monkeys=monkeys):
    items = [monkey.items.copy() for monkey in monkeys]
    nb_inspections = [0 for _ in monkeys]
    for r in range(nb):
        #if not r%1000: print("round",r,"of",nb)
        for monkey in monkeys:
            for item in items[monkey.name]:
                new = monkey.operation(item)
                new = func(new)
                n_monkey = monkey.test(new)
                items[n_monkey].append(new)
            nb_inspections[monkey.name] += len(items[monkey.name])
            items[monkey.name].clear()
    nb_inspections = sorted(nb_inspections)
    return nb_inspections[-1] * nb_inspections[-2]

print(res1 := res(20,lambda n:n//3))
print(res2 := res(10000,lambda n:n%prod))