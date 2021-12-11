import inputAoC as aoc

input = """5483143223
2745854711
5264556173
6141336146
6357385478
4167524645
2176841721
6882881134
4846848554
5283751526"""
input = aoc.get_input_file(11,2021)
def print_carte(carte):
    for line in carte: print(line)

carte = [list(map(int,line)) for line in input.splitlines()]

def coord_neighbors(carte,i,j):
    res = []
    for x in range(i-1,i+2):
        for y in range(j-1,j+2):
            if 0 <= x < len(carte) and 0 <= y < len(carte[x]) and not(x==i and y==j):
                res.append((x,y))
    return res

def step(carte):
    """modifie carte et retourne le nb de flashs"""
    for i in range(len(carte)):
        for j in range(len(carte[i])):
            carte[i][j] += 1
    flashes = set()
    there_is_new_flash = True
    while there_is_new_flash: 
        there_is_new_flash = False
        new_flashes = set()
        for i in range(len(carte)):
            for j in range(len(carte[i])):
                if (i,j) not in flashes and carte[i][j] > 9:
                    new_flashes.add((i,j))
                    there_is_new_flash = True
        for flash in new_flashes:
            neighbors = coord_neighbors(carte, flash[0], flash[1])
            for neigh in neighbors:
                carte[neigh[0]][neigh[1]] += 1
        flashes.update(new_flashes)
    
    for flash in flashes:
        carte[flash[0]][flash[1]] = 0
    return len(flashes)

def n_steps(carte,n_fin=100):
    res = 0
    for _ in range(n_fin):
        res += step(carte)
    return res

res1 = n_steps(carte)
print(res1)

def is_synchro(carte):
    for lin in carte:
        for col in lin:
            if col > 0: return False
    return True

def simultaneous(carte,n_deb=100):
    """n_deb est par défault à 100 car j'ai déjà fait 100 steps pour res1"""
    while not(is_synchro(carte)):
        step(carte)
        n_deb += 1
    return n_deb

res2 = simultaneous(carte)
print(res2)