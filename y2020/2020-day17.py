import inputAoC as aoc
import my_utils

ex = """.#.
..#
###"""

start = aoc.get_input_file(17,2020)

def get_pixel_neighbors(grid, x,y,z):
    res = 0
    for k in range(z-1, z+2):
        if not(0 <= k < len(grid)):
            continue
        for j in range(y-1, y+2):
            if not(0 <= j < len(grid[k])):
                continue
            for i in range(x-1,x+2):
                if not(0 <= i < len(grid[k][j])):
                    continue
                if not( i==x and j==y and k==z ):
                    res += grid[k][j][i]=="#"
    return res

def get_neighbors(grid):
    res = [0] * len(grid)
    for z in range(len(grid)):
        res[z] = [0] * len(grid[z])
        for y in range(len(grid[z])):
            res[z][y] = [0] * len(grid[z][y])
            for x in range(len(grid[z][y])):
                res[z][y][x] = get_pixel_neighbors(grid, x, y, z)
    return res

def turn_pixel(pixel, neighbors):
    if neighbors == 3 or (neighbors == 2 and pixel == "#"):
        return "#"
    else:
        return "."

def agrandir_grid_n(grid,n=1):
    res = []
    res = [0] * (len(grid) + 2*n)
    for z in range(len(res)):
        res[z] = [0] * (len(grid[0]) + 2*n)
        for y in range(len(res[z])):
            if n <= z < len(grid)+n and n <= y < len(grid[z-n])+n:
                res[z][y] = '.' * n +  grid[z-n][y-n] + '.' * n
            else:
                res[z][y] = '.' * (len(grid[0][0]) + 2*n)
    return res


def turn(grid):
    grid = agrandir_grid_n(grid)
    voisins = get_neighbors(grid)
    res = ['.'] * len(grid)
    for z in range(len(grid)):
        res[z] = ["."] * len(grid[z])
        for y in range(len(grid[z])):
            res[z][y] = ""
            for x in range(len(grid[z][y])):
                res[z][y] += turn_pixel(grid[z][y][x], voisins[z][y][x])
    return res

def turns(start,n):
    grid = turn(start)
    for _ in range(1,n):
        grid = turn(grid)
    return grid

def count_active(grid):
    res = 0
    for z in grid:
        for y in z:
            res += y.count("#")
    return res

print(start)

grid = [start.splitlines()]
grid_ex = [ex.splitlines()]

my_utils.print_list(grid)

after_1turn = turn(grid)

after_6turns = turns(grid,6)

my_utils.print_list(after_1turn)

# print(count_active(turns(grid_ex,6)))
res1 = count_active(after_6turns)
print(res1)
