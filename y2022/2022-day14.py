import inputAoC as aoc

input = """498,4 -> 498,6 -> 496,6
503,4 -> 502,4 -> 502,9 -> 494,9"""
example = True
input, example = aoc.get_input_file(14,2022), False
paths = input.splitlines()

start = (500,0)

lines = []
points = []
x_min, x_max, y_max = start[0], start[0], start[1]
for path in paths:
    coords = path.split(" -> ")
    for i in range(len(coords)):
        point = tuple(map(int,coords[i].split(',')))
        coords[i] = point
        if i >= 1: lines.append((coords[i-1],coords[i]))
        y_max = max(y_max,point[1])
        x_min = min(x_min,point[0])
        x_max = max(x_max,point[0])

def get_grid(lines,start=start):
    x_min, x_max, y_max = start[0], start[0], start[1]
    for point1,point2 in lines:
        y_max = max(y_max,point1[1],point2[1])
        x_min = min(x_min,point1[0],point2[0])
        x_max = max(x_max,point1[0],point2[0])
    grid = [[0 for x in range(x_min-1,x_max+2)] for y in range(y_max+1)]
    for point1,point2 in lines:
        xs = [point1[0],point2[0]]    
        ys = [point1[1],point2[1]]
        for x in range(min(xs),max(xs)+1):
            for y in range(min(ys),max(ys)+1):
                grid[y][x-x_min+1] = 2
    return grid

grid1 = get_grid(lines)
start1 = (start[0]-x_min+1,start[1])

lines.append([(start[0]-y_max-2,y_max+2), (start[0]+y_max+2,y_max+2)])

grid2 = get_grid(lines)
start2 = (y_max+3,start[1])

def add_sand(pos, grid):
    x,y = pos
    if not(0<x<len(grid[0])-1 and y<len(grid)-1 and grid[y][x]==0):
        return False
    if grid[y+1][x] == 0: #under
        return add_sand((x,y+1),grid)
    if grid[y+1][x-1] == 0: #diagonal left
        return add_sand((x-1,y+1),grid)
    if grid[y+1][x+1] == 0: #diagonal right
        return add_sand((x+1,y+1),grid)
    grid[y][x] = 1
    return True

def simulation(start, grid):
    res = 0
    while add_sand(start, grid): res += 1
    return res

print(res1 := simulation(start1,grid1))
print(res2 := simulation(start2,grid2))

def visualisation(grid,start,without_grid=True):
    with_grid = not without_grid
    res = ""
    n = len(grid[0]) + 2*with_grid
    for line in grid:
        if with_grid: res += "~"
        for point in line:
            if point == 0: res += " " if without_grid else "."
            if point == 1: res += "." if without_grid else "o"
            if point == 2: res += "#"
        if with_grid: res += "~"
        res += "\n"
    if with_grid: res += "~"*(len(grid[0])+2) + "\n"
    empty = " " if without_grid else "."
    res = empty*(start[0]+with_grid) +"+"+ empty*(n-start[0]-1-with_grid) + \
            "\n" + "\n".join(res.splitlines()[1:]) + "\n"
    return res[:-1]

if example:
    print(visualisation(grid1,start1,False))
    print(visualisation(grid2,start2))
    print(res1,res2)
else:
    file1 = open("../outputs/2022_14_1.txt","w")
    file1.write(visualisation(grid1,start1))
    file1.close()
    file2 = open("../outputs/2022_14_2.txt","w")
    file2.write(visualisation(grid2,start2))
    file2.close()
