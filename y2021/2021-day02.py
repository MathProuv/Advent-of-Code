import inputAoC as aoc

ex = """forward 5
down 5
forward 8
up 3
down 8
forward 2"""
data = aoc.get_input_file(2,2021).splitlines()
#data = ex.splitlines()
instrs = [instr.split(" ") for instr in data]

horizontal = 0
depth = 0
for instr in instrs:
    dir, x = instr[0], int(instr[1])
    if dir == "down":
        depth += x
    elif dir == "up":
        depth -= x
    elif dir == "forward":
        horizontal += x
res1 = horizontal*depth
print(res1)

#horizontal = 0 #Ca sera la même distance horizontale
depth = 0
aim = 0
for instr in instrs:
    dir, x = instr[0], int(instr[1])
    if dir == "down":
        aim += x
    elif dir == "up":
        aim -= x
    elif dir == "forward":
        #horizontal += x
        depth += aim*x
    #print(aim, depth, horizontal)
res2 = depth*horizontal
print(res2)