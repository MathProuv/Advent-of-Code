import inputAoC as aoc

input = """2199943210
3987894921
9856789892
8767896789
9899965678"""
input = aoc.get_input_file(9,2021)

mapp = input.split()
for i in range(len(mapp)):
    mapp[i] = [int(j) for j in mapp[i]]

#print(mapp)

def neighbors(mapp,i,j):
    """retourne la liste des valeurs des voisins"""
    res = []
    for x in [i-1,i+1]:
        if 0 <= x < len(mapp):
            res.append(mapp[x][j])
    for y in [j-1,j+1]:
        if 0 <= y < len(mapp[0]):
            res.append(mapp[i][y])
    return res

def is_low(mapp,i,j):
    pos = mapp[i][j]
    for neigh in neighbors(mapp,i,j):
        if neigh <= pos: return False
    return True

def get_lows(mapp):
    """retourne la liste des positions des lows"""
    res = []
    for i in range(len(mapp)):
        for j in range(len(mapp[i])):
            if is_low(mapp,i,j):
                #print(i,j, mapp[i][j])
                res.append((i,j))
    return res

def risk_levels(mapp):
    lows = get_lows(mapp)
    res = 0
    for low in lows:
        res += mapp[low[0]][low[1]] + 1
    return res

res1 = risk_levels(mapp)
print(res1)


def low_neighbors(mapp,pos):
    """retourne la liste des positions des voisins du même basin que pos"""
    i,j = pos
    res = []
    for x in [i-1,i+1]:
        if 0 <= x < len(mapp) and mapp[x][j] < 9:
            res.append((x,j))
    for y in [j-1,j+1]:
        if 0 <= y < len(mapp[0]) and mapp[i][y] < 9:
            res.append((i,y))
    return res

def basin(low,mapp):
    """retourne le basin qui contient low, càd la liste des positions du basin de low"""
    res = set()
    res.add(low)
    new = res.copy()
    while len(new):
        temp = set()
        for pos in new:
            neighs = low_neighbors(mapp,pos)
            for neigh in neighs:
                if neigh not in res:
                    temp.add(neigh)
        res.update(temp)
        new = temp.copy()
    return list(res)

def basins(mapp):
    """retourne la liste des basins"""
    res = []
    lows = get_lows(mapp)
    #print(lows)
    for low in lows:
        res.append(basin(low,mapp))
    return res

def n_max(liste,n=3):
    copie = liste[:]
    res = []
    for _ in range(n):
        res.append(max(copie))
        copie.remove(max(copie))
    return res

def largests_basins(mapp):
    """retourne le produit des 3 plus grandes len de basin"""
    basins_len = [len(zon) for zon in basins(mapp)]
    maxs = n_max(basins_len,3)
    #print(maxs)
    res = 1
    for m in maxs: res *= m
    return res

res2 = largests_basins(mapp)
print(res2)