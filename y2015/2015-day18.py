import inputAoC as aoc

def print_grid(grid,text=""):
    print(text)
    for line in grid:
        print("".join(line))
    print()

input = """.#.#.#
...##.
#....#
..#...
#.#..#
####.."""
nb = 4
input,nb = aoc.get_input_file(18,2015), 100

grid = [list(line) for line in input.splitlines()]

def score(grid):
    res = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if is_on(grid[i][j]): res += 1
    return res

def is_on(lamp):
    if lamp == '#': return True
    elif lamp == '.': return False

def nb_neighbors_on(grid,i,j):
    res = 0
    for x in [i-1,i,i+1]:
        for y in [j-1,j,j+1]:
            #print(x,y)
            if 0 <= x < len(grid) and 0 <= y < len(grid[0]) and (x!=i or y!=j):
                res += is_on(grid[x][y])
    return res

def step_lamp(grid,i,j):
    lamp = grid[i][j]
    nb = nb_neighbors_on(grid,i,j)
    res = ''
    if (is_on(lamp) and 2 <= nb <= 3) or (not(is_on(lamp)) and nb == 3): res = "#"
    else : res = '.'
    #print(lamp, nb, res)
    return res

def step(grid):
    #copie
    new_grid = [0] * len(grid)
    for line in range(len(grid)):
        new_grid[line] = grid[line][:]
    #step de chaque lamp
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            new_grid[i][j] = step_lamp(grid,i,j)
    return new_grid

def steps(grid, n):
    #print_grid(grid,"grid initiale")
    for n_step in range(1,n+1):
        grid = step(grid)
        #print_grid(grid,"grid n°" + str(n_step))
    return grid

res1 = score(steps(grid,nb))
print(res1)


grid[0][0] = grid[-1][0] = grid[0][-1] = grid[-1][-1] = '#'

def step_lamp(grid,i,j):
    lamp = grid[i][j]
    nb = nb_neighbors_on(grid,i,j)
    res = ''
    if (is_on(lamp) and 2 <= nb <= 3) or (not(is_on(lamp)) and nb == 3): res = "#"
    else : res = '.'
    if (i,j) == (0,0) or (i,j) == (len(grid)-1,0) or (i,j) == (0,len(grid[0])-1) or (i,j) == (len(grid)-1,len(grid[0])-1): res = "#"
    #print(lamp, nb, res)
    return res


res2 = score(steps(grid,nb))
print(res2)