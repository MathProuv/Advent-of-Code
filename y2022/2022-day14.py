import inputAoC as aoc

input = """498,4 -> 498,6 -> 496,6
503,4 -> 502,4 -> 502,9 -> 494,9"""
input = aoc.get_input_file(14,2022)
paths = input.splitlines()

start = (500,0)

lines = []
points = []
y_max = start[1]
x_min, x_max = start[0], start[0]
for path in paths:
    coords = path.split(" -> ")
    for i in range(len(coords)):
        point = tuple(map(int,coords[i].split(',')))
        coords[i] = point
        if i >= 1: lines.append((coords[i-1],coords[i]))
        y_max = max(y_max,point[1])
        x_min = min(x_min,point[0])
        x_max = max(x_max,point[0])

def get_grid_and_start(lines,start=start):
    y_max = start[1]
    x_min, x_max = start[0], start[0]
    for point1,point2 in lines:
        y_max = max(y_max,point1[1],point2[1])
        x_min = min(x_min,point1[0],point2[0])
        x_max = max(x_max,point1[0],point2[0])
    grid = [
        [0 for x in range(x_min,x_max+1)] 
        for y in range(y_max+1)
    ]
    for point1,point2 in lines:
        xs = [point1[0],point2[0]]    
        ys = [point1[1],point2[1]]
        for x in range(min(xs),max(xs)+1):
            for y in range(min(ys),max(ys)+1):
                grid[y][x-x_min] = 2
    start = (start[0]-x_min,start[1])
    return grid,start

grid1,start1 = get_grid_and_start(lines)
lines.append([(start[0]-y_max-2,y_max+2), (start[0]+y_max+2,y_max+2)])
grid2,start2 = get_grid_and_start(lines)

def add_sand(pos, grid):
    if not(0<pos[0]<len(grid[0])-1 and pos[1]<len(grid)-1 and grid[pos[1]][pos[0]]==0):
        return False
    if grid[pos[1]+1][pos[0]] == 0:
        return add_sand((pos[0],pos[1]+1),grid)
    if grid[pos[1]+1][pos[0]-1] == 0:
        return add_sand((pos[0]-1,pos[1]+1),grid)
    if grid[pos[1]+1][pos[0]+1] == 0:
        return add_sand((pos[0]+1,pos[1]+1),grid)
    grid[pos[1]][pos[0]] = 1
    return True

res1 = 0
add_sand_condition = True
while add_sand_condition:
    add_sand_condition = add_sand(start1, grid1)
    res1 += add_sand_condition
print(res1)

res2 = 0
add_sand_condition = True
while add_sand_condition:
    add_sand_condition = add_sand(start2, grid2)
    res2 += add_sand_condition
print(res2)