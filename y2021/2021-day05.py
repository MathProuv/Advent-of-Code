import inputAoC as aoc

ex = """0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2"""
input = ex
input = aoc.get_input_file(5,2021)
input = input.splitlines()

n = len(input)
input = list(map(lambda x: x.split(' -> '),input))

max_x = 0
max_y = 0
for i in range(len(input)):
    pos1,pos2 = input[i]
    pos1 = tuple(map(int,pos1.split(','))) #(x1,y1)
    pos2 = tuple(map(int,pos2.split(','))) #(x2,y2)
    input[i] = pos1,pos2
    for pos in (pos1,pos2):
        max_x = max(max_x,pos[0])
        max_y = max(max_y,pos[1])

carte = [0] * (max_x+1)
for i in range(len(carte)):
    carte[i] = [0] * (max_y+1)

def score(carte):
    res = 0
    for x in range(len(carte)):
        for y in range(len(carte[0])):
            if carte[x][y] > 1:
                res += 1
    return res

"""
for line in input:
    pos1, pos2 = line
    if pos1[0] == pos2[0]: #vertical
        x = pos1[0]
        y1,y2 = pos1[1], pos2[1]
        for y in range(min(y1,y2),max(y1,y2)+1):
            carte[x][y] += 1
        #print("vertical",pos1,pos2)
    elif pos1[1] == pos2[1]: #horizontal
        y = pos1[1]
        x1,x2 = pos1[0], pos2[0]
        for x in range(min(x1,x2),max(x1,x2)+1):
            carte[x][y] += 1
        #print("horizontal",pos1,pos2)
    else: #diagonal
        x,y = x1,y1
        x1,x2 = pos1[0], pos2[0]
        y1,y2 = pos1[1], pos2[1]
        if x1<x2: dx = 1
        else: dx = -1
        if y1<y2: dy = 1
        else: dy = -1
        for d in range(max(x1-x2,x2-x1)+1):
            x,y = x1+d*dx,y1+d*dy
            carte[x][y] += 1

print(score(carte))"""


carte1 = [0] * (max_x+1)
for i in range(len(carte)):
    carte1[i] = [0] * (max_y+1)
carte2 = [0] * (max_x+1)
for i in range(len(carte)):
    carte2[i] = [0] * (max_y+1)

for line in input:
    pos1, pos2 = line
    x1,x2 = pos1[0], pos2[0]
    y1,y2 = pos1[1], pos2[1]
    if x1<x2: dx = 1
    elif x1==x2: dx=0
    else: dx = -1
    if y1<y2: dy = 1
    elif y1==y2: dy=0
    else: dy = -1
    for d in range(max(x1-x2,x2-x1,y1-y2,y2-y1)+1):
        x,y = x1+d*dx,y1+d*dy
        carte2[x][y] += 1
        # horizontal ou vertical
        if dx*dy==0: carte1[x][y] += 1

res1 = score(carte1)
res2 = score(carte2)
print(res1,res2)