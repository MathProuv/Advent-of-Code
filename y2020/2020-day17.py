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

def agrandir_grid(grid,n=1):
    res = [0] * (len(grid) + 2*n)
    for z in range(len(res)):
        res[z] = [0] * (len(grid[0]) + 2*n)
        for y in range(len(res[z])):
            if n <= z < len(grid)+n and n <= y < len(grid[z-n])+n:
                res[z][y] = '.' * n +  grid[z-n][y-n] + '.' * n
            else:
                res[z][y] = '.' * (len(grid[0][0]) + 2*n)
    return res

def turn_pixel(pixel, neighbors):
    if neighbors == 3 or (neighbors == 2 and pixel == "#"):
        return "#"
    else:
        return "."

def turn(grid):
    grid = agrandir_grid(grid)
    voisins = get_neighbors(grid)
    res = ['.'] * len(grid)
    for z in range(len(grid)):
        res[z] = ["."] * len(grid[z])
        for y in range(len(grid[z])):
            res[z][y] = ""
            for x in range(len(grid[z][y])):
                res[z][y] += turn_pixel(grid[z][y][x], voisins[z][y][x])
    return res

def turns(start,n, turn_fct=turn):
    grid = turn_fct(start)
    for _ in range(1,n):
        grid = turn_fct(grid)
    return grid

def count_active(grid):
    res = 0
    for z in grid:
        for y in z:
            res += y.count("#")
    return res

#print(start)

grid = [start.splitlines()]
grid_ex = [ex.splitlines()]

#my_utils.print_list(grid)

after_1turn = turn(grid)

after_6turns = turns(grid,6)

#my_utils.print_list(after_1turn)

# print(count_active(turns(grid_ex,6)))
res1 = count_active(after_6turns)
print(res1)


#########



def get_pixel_neighbors4D(grid, x,y,z,w):
    res = 0
    for l in range(w-1,w+2):
        if not(0 <= l < len(grid)):
                continue
        for k in range(z-1, z+2):
            if not(0 <= k < len(grid[l])):
                continue
            for j in range(y-1, y+2):
                if not(0 <= j < len(grid[l][k])):
                    continue
                for i in range(x-1,x+2):
                    if not(0 <= i < len(grid[l][k][j])):
                        continue
                    if not( i==x and j==y and k==z ):
                        res += grid[l][k][j][i]=="#"
    return res


def get_neighbors4D(grid4D):
    res = [0] * len(grid4D)
    for w in range(len(grid4D)):
        res[w] = [0] * len(grid4D[w])
        for z in range(len(grid4D[w])):
            res[w][z] = [0] * len(grid4D[w][z])
            for y in range(len(grid4D[w][z])):
                res[w][z][y] = [0] * len(grid4D[w][z][y])
                for x in range(len(grid4D[w][z][y])):
                    res[w][z][y][x] = get_pixel_neighbors4D(grid4D, x, y, z, w)
    return res

def agrandir_grid4D(grid4D,n=1):
    res = []
    for l in range(len(grid4D) + 2*n):
        if n <= l < len(grid4D) + n:
            res.append(agrandir_grid(grid4D[l-n]))
        else:
            grid3D = [0] * (len(grid4D[0]) + 2*n)
            for k in range(len(grid3D)):
                grid3D[k] = [0] * (len(grid4D[0][0]) + 2*n)
                for j in range(len(grid3D[k])):
                    grid3D[k][j] = '.' * (len(grid4D[0][0][0]) + 2*n)
            res.append(grid3D)
    return res

def turn4D(grid4D):
    grid4D = agrandir_grid4D(grid4D)
    voisins = get_neighbors4D(grid4D)
    res = ['.'] * len(grid4D)
    for w in range(len(grid4D)):
        res[w] = ["."] * len(grid4D[w])
        for z in range(len(grid4D[w])):
            res[w][z] = ["."] * len(grid4D[w][z])
            for y in range(len(grid4D[w][z])):
                res[w][z][y] = ""
                for x in range(len(grid4D[w][z][y])):
                    res[w][z][y] += turn_pixel(grid4D[w][z][y][x], voisins[w][z][y][x])
    return res


def count_active4D(grid):
    res = 0
    for grid3D in grid:
        res += count_active(grid3D)
    return res

# turns4D = turns(.,.,turn4D)

grid4D = [[start.splitlines()]]
grid4D_aggrandie = agrandir_grid4D(grid4D)
grid4D_agg_voisins = get_neighbors4D(grid4D_aggrandie)
after_1turn4D = turn4D(grid4D)
after_6turns4D = turns(grid4D, 6, turn4D)

"""my_utils.print_list(grid4D)
my_utils.print_list(grid4D_aggrandie)
my_utils.print_list(grid4D_agg_voisins)
my_utils.print_list(after_1turn4D)"""


grid4D_ex = [[ex.splitlines()]]
my_utils.print_list(grid4D_ex)
after_1turn_ex = turn4D(grid4D_ex)
after_6turns_ex = turns(grid4D_ex,6,turn4D)
my_utils.print_list(after_1turn_ex)
# print(turn(grid_ex)) #rappel en 3D
print("ex 4D", count_active4D(after_6turns_ex))

res2 = count_active4D(after_6turns4D)
print(res2)