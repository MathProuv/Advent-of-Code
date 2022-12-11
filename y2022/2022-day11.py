import inputAoC as aoc
import re

data = aoc.get_input_file(11,2022)

def operation0(old): return old * 19
def operation1(old): return old * 11
def operation2(old): return old + 6
def operation3(old): return old + 5
def operation4(old): return old + 7
def operation5(old): return old * old
def operation6(old): return old + 2
def operation7(old): return old + 3

def test0(new): return 7 if new%17 else 4
def test1(new): return 2 if new%3 else 3
def test2(new): return 4 if new%19 else 0
def test3(new): return 0 if new%7 else 2
def test4(new): return 5 if new%2 else 7
def test5(new): return 6 if new%5 else 1
def test6(new): return 1 if new%11 else 3
def test7(new): return 6 if new%13 else 5

items0 = [72, 64, 51, 57, 93, 97, 68]
items1 = [62]
items2 = [57, 94, 69, 79, 72]
items3 = [80, 64, 92, 93, 64, 56]
items4 = [70, 88, 95, 99, 78, 72, 65, 94]
items5 = [57, 95, 81, 61]
items6 = [79, 99]
items7 = [68, 98, 62]

n = 8
functions = [operation0, operation1, operation2, operation3, operation4, operation5, operation6, operation7]
tests = [test0, test1, test2, test3, test4, test5, test6, test7]
items = [items0, items1, items2, items3, items4, items5, items6, items7]
nb_inspections = [0 for _ in range(n)]

primes = [2,3,5,7,11,13,17,19]
prod = 1
for p in primes: prod *= p
def round():
    for monkey in range(n):
        for item in items[monkey]:
            new = functions[monkey](item)
            new %= prod
            n_monkey = tests[monkey](new)
            items[n_monkey].append(new)
        nb_inspections[monkey] += len(items[monkey])
        items[monkey].clear()

for r in range(10000):
    #if not r%1000: print(r)
    round()

nb_inspections_sorted = sorted(nb_inspections)
res1 = nb_inspections_sorted[-1] * nb_inspections_sorted[-2]
print(res1)
