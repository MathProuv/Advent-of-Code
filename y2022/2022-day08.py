import inputAoC as aoc

grid_str = """30373
25512
65332
33549
35390"""
grid_str = aoc.get_input_file(8,2022)

grid = [list(map(int,list(line))) for line in grid_str.splitlines()]

n,m = len(grid), len(grid[0])

is_visible = [[0 for _ in range(m)] for _ in range(n)]

for i in range(n):
    skyscraper_left, skyscraper_right = -1,-1
    for j in range(m):
        if grid[i][j] > skyscraper_left:
            is_visible[i][j] = 1
            skyscraper_left = grid[i][j]
        if grid[i][-j-1] > skyscraper_right:
            is_visible[i][-j-1] = 1
            skyscraper_right = grid[i][-j-1]
for j in range(m):
    skyscraper_top, skyscraper_bottom = -1,-1
    for i in range(n):
        if grid[i][j] > skyscraper_top:
            is_visible[i][j] = 1
            skyscraper_top = grid[i][j]
        if grid[-i-1][j] > skyscraper_bottom:
            is_visible[-i-1][j] = 1
            skyscraper_bottom = grid[-i-1][j]

res1 = sum([sum(line) for line in is_visible])
print(res1)

scenic_score = [[0 for _ in range(m)] for _ in range(n)]
for i in range(1,n-1):
    for j in range(1,m-1):
        value = grid[i][j]
        i_left,i_right = i-1,i+1
        j_top,j_bottom = j-1,j+1
        while i_left>0 and grid[i_left][j] < value: i_left -= 1
        while i_right<n-1 and grid[i_right][j] < value: i_right += 1
        while j_top>0 and grid[i][j_top] < value: j_top -= 1
        while j_bottom<m-1 and grid[i][j_bottom] < value: j_bottom += 1
        scenic_score[i][j] = (i-i_left)*(i_right-i)*(j-j_top)*(j_bottom-j)
res2 = max([max(line) for line in scenic_score])
print(res2)