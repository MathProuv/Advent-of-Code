import inputAoC as aoc

input = aoc.get_input(1,2022)

inputs_by_elf = [sum(list(map(int,inp.split("\n")))) for inp in input.split("\n\n")]
inputs_by_elf.sort()

res1 = inputs_by_elf[-1]
res2 = sum(inputs_by_elf[-3:])

print(res1)
print(res2)