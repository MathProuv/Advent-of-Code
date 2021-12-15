import inputAoC as aoc
from math import inf as infty

input = """1163751742
1381373672
2136511328
3694931569
7463417111
1319128137
1359912421
3125421639
1293138521
2311944581"""
input = aoc.get_input_file(15,2021)

def print_carte(carte):
    for line in carte: print(line)


def trouve_min(Q,d):
    """retourne le sommet de distance minimale et sa distance"""
    mini = infty
    s = (-1,-1)
    for i,j in Q:
        if d[i][j] <= mini:
            s = (i,j)
            mini = d[i][j]
    return s

def maj_distances(s1,s2,d,carte):
    """mise à jour de la distance de s2 dans d quand on ajoute s1"""
    new_dist = d[s1[0]][s1[1]] + carte[s2[0]][s2[1]]
    if d[s2[0]][s2[1]] > new_dist:
        d[s2[0]][s2[1]] = new_dist

def neighbors(s,P,Q,n,m):
    """retourne la liste des voisins de s qui ne sont pas dans P en les ajoutant à Q s'ils n'y sont pas déjà"""
    x,y = s
    res = []
    #for i in range(x-1,x+2):
    #    for j in range(y-1,y+2):
    for i,j in [(x,y-1),(x,y+1),(x-1,y),(x+1,y)]:
            if (x==i or y==j) and not(x==i and y==j) and 0 <= i < n and 0 <= j < m and (i,j) not in P:
                res.append((i,j))
                Q.add((i,j)) #Q est un set donc add pas s'il y est déjà
    return res

def dijsktra(carte):
    n,m = len(carte),len(carte[0])
    start = (0,0)
    end = (n-1, m-1)
    P = set()
    Q = set()
    d = [infty] * n
    for i in range(n): 
        d[i] = [infty] * m
    d[start[0]][start[1]] = 0
    Q.add(start)
    neighbors(start,P,Q,n,m)
    while end not in P:
        sommet = trouve_min(Q,d)
        P.add(sommet)
        Q.remove(sommet)
        voisins = neighbors(sommet,P,Q,n,m)
        for s in voisins:
            maj_distances(sommet,s,d,carte)
    return d[end[0]][end[1]]

carte1 = [[int(c) for c in line] for line in input.splitlines()]
res1 = dijsktra(carte1)
print(res1)
