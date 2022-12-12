import inputAoC as aoc

input = """Sabqponm
abcryxxl
accszExk
acctuvwj
abdefghi"""
input = aoc.get_input_file(12,2022)

start = input.index('S')
end = input.index('E')
grid = [list(map(lambda x:ord(x)-ord('a'), line)) for line in input.splitlines()]

n,m = len(grid),len(grid[0])
start = (start//(m+1),start%(m+1))
end = (end//(m+1),end%(m+1))
grid[start[0]][start[1]] = 0
grid[end[0]][end[1]] = 25

ds = [[-1 for _ in range(m)] for _ in range(n)]
ds[end[0]][end[1]] = 0

def get_neighbours(i,j):
    ans = set()
    if i>0: ans.add((i-1,j))
    if i<n-1: ans.add((i+1,j))
    if j>0: ans.add((i,j-1))
    if j<m-1: ans.add((i,j+1))
    return ans

to_check = set(get_neighbours(end[0],end[1]))
checked = set()
checked.add(end)
change = True
change_index = 0
while change:
    change = False
    for x,y in to_check.copy():
        neighs = get_neighbours(x,y)
        for i,j in neighs.intersection(checked):
            if grid[i][j] - grid[x][y] <= 1:
                if ds[x][y] < 0: 
                    ds[x][y] = ds[i][j] + 1
                    change = True
                else: ds[x][y] = min(ds[x][y],ds[i][j] + 1)
                checked.add((x,y))
                for to_add in get_neighbours(x,y).difference(checked):
                    to_check.add(to_add)
    #print(change_index := change_index + 1)

res1 = ds[start[0]][start[1]]
print(res1)

potential_starts = [(i,j) for i in range(n) for j in range(m) if grid[i][j] == 0]
res2 = res1
for i,j in potential_starts:
    if ds[i][j] >= 0:
        res2 = min(res2, ds[i][j])

print(res2)