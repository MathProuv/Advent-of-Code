import inputAoC as aoc

input = """R 5
U 8
L 8
D 3
R 17
D 10
L 25
U 20"""
input = aoc.get_input_file(9,2022)
moves = [[line[0],int(line[2:])] for line in input.splitlines()]

def move_head(head,dir):
    if dir == 'L': head[0] -= 1
    elif dir == 'R': head[0] += 1
    elif dir == 'D': head[1] -= 1
    else: head[1] += 1

def move_knot(head,tail):
    dx, dy = head[0]-tail[0], head[1]-tail[1]
    if max(dx,dy,-dx,-dy)>1: # dx*dy => diagonal
        tail[0] += dx//abs(dx) if dx*dy else dx//2
        tail[1] += dy//abs(dy) if dx*dy else dy//2

knots = [[0,0] for _ in range(10)]
places_visited_by_T,places_visited_by_9 = set(),set()
places_visited_by_T.add((0,0))
places_visited_by_9.add((0,0))
for dir,nb in moves:
    for _ in range(nb):
        move_head(knots[0],dir)
        for i in range(1,10): 
            move_knot(knots[i-1],knots[i])
        places_visited_by_T.add(tuple(knots[1]))
        places_visited_by_9.add(tuple(knots[-1]))

res1 = len(places_visited_by_T)
res2 = len(places_visited_by_9)
print(res1,res2)