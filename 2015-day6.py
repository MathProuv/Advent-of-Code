import inputAoC

file = inputAoC.get_input_file(6, 2015)

size = 1000
instructs = file.split("\n")

grid = [0]*size
for i in range(size):
    grid[i] = [0]*size

def turn_on(i,j):
    #grid[j][i] = 1
    grid[j][i] += 1
def turn_off(i,j):
    #grid[j][i] = 0
    if grid[j][i]: grid[j][i] -= 1 
def toggle(i,j):
    #grid[j][i] = 1-grid[j][i]
    grid[j][i] += 2

def through(p1, p2, act):
    for i in range(p1[0], p2[0]+1):
        for j in range(p1[1], p2[1]+1):
            act(i,j)

for instr in instructs:
    instr = instr.split(" ")
    p2 = list(map(int, instr[-1].split(",")))
    p1 = list(map(int, instr[-3].split(",")))
    if instr[0] == "toggle":
        act = toggle
    elif instr[1] == "on":
        act = turn_on
    else:
        act = turn_off
    through(p1, p2, act)

print(sum([sum(lign) for lign in grid]))
