import inputAoC as aoc

input = """1000
2000
3000

4000

5000
6000

7000
8000
9000

10000"""
input = aoc.get_input_file(1,2022)
items = input.split("\n\n")

items_by_elf = sorted([sum(list(map(int,inp.split("\n")))) for inp in items])

res1 = items_by_elf[-1]
res2 = sum(items_by_elf[-3:])

print(res1)
print(res2)