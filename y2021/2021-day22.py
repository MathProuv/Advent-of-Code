import inputAoC as aoc
from functools import reduce

input = aoc.get_input_file(22,2021)

def get_cuboid(instr):
    mode = instr[:3].strip()
    mode = True if mode == "on" else False
    instr = instr[3:].strip()
    coords = list(map(lambda x: list(map(int,x[2:].split('..'))),instr.split(',')))
    coords.insert(0,mode)
    return coords

instrs = list(map(get_cuboid,input.splitlines()))
#for instr in instrs: print(instr)

def part1(instr):
    _,x,y,z = instr
    r = range(-50,51)
    return x[0] in r and x[1] in r and y[0] in r and y[1] in r and z[0] in r and z[1] in r 

def modelisation(instrs):
    grid = [0]*101
    for x in range(101):
        grid[x] = [0] * 101
        for y in range(101):
            grid[x][y] = [False] * 101
    for instr in instrs:
        if not part1(instr): continue
        mode,X,Y,Z = instr
        for x in range(X[0],X[1]+1):
            for y in range(Y[0],Y[1]+1):
                for z in range(Z[0],Z[1]+1):
                    grid[x][y][z] = mode
    compt = 0
    for x in range(101):
        for y in range(101):
            for z in range(101):
                compt += grid[x][y][z]
    return compt

res1 = modelisation(instrs)
print(res1)

print([i[1] for i in instrs])

X_MIN = reduce(lambda acc,x:min(x[0],acc),[i[1] for i in instrs],0)
X_MAX = reduce(lambda acc,x:max(x[1],acc),[i[1] for i in instrs],0)
Y_MIN = reduce(lambda acc,y:min(y[0],acc),[i[2] for i in instrs],0)
Y_MAX = reduce(lambda acc,y:max(y[1],acc),[i[2] for i in instrs],0)
Z_MIN = reduce(lambda acc,z:min(z[0],acc),[i[3] for i in instrs],0)
Z_MAX = reduce(lambda acc,z:max(z[1],acc),[i[3] for i in instrs],0)

print(X_MIN,X_MAX)
print(Y_MIN,Y_MAX)
print(Z_MIN,Z_MAX)