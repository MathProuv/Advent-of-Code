import inputAoC as aoc

input = open("../inputs/2022_10_example.txt").read()
input = aoc.get_input_file(10,2022)

instrs = input.splitlines()

x = 1
xs = [x]
for instr in instrs:
    if instr == "noop":
        xs += [x]
    else:
        xs += [x,x]
        x += int(instr[5:])

res1 = 0
for i in range(20,222,40):
    res1 += i * xs[i]
print(res1)

res2 = ""
for c in range(1,241):
    if abs(xs[c] - c%40) <= 1: res2 += "#"
    else: res2 += "."

for i in range(0,202,40):
    print(res2[i:i+40])

res2 = "EALGULPG" #read the console
print(res1, res2)