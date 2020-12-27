""" Une grille hex représentée dans un tableau 2D:

y = -2: -2  -1  +0  +1  +2
y = -1:   -2  -1  +0  +1  +2
y =  0:     -2  -1  +0  +1  +2
y = +1:       -2  -1  +0  +1  +2
            n
avec     e -|- w
            s
Les voisins de (x,y) sont :
nw=(x,y-1), ne=(x+1,y-1), e=(x+1,y), se=(x,y+1), sw=(x-1,y+1), w=(x-1,y)

Par exemple, les six voisins de (0,0) sont :
(0,-1), (1,-1), (1,0), (0,1), (-1,1), (-1,0)

hex_grid est un dict de dict, afin d'avoir des coordonnées négatives
"""

import inputAoC as aoc
import my_utils

raw_tiles = aoc.get_input_file(24,2020).splitlines()
raw_tiles_ex = """sesenwnenenewseeswwswswwnenewsewsw
neeenesenwnwwswnenewnwwsewnenwseswesw
seswneswswsenwwnwse
nwnwneseeswswnenewneswwnewseswneseene
swweswneswnenwsewnwneneseenw
eesenwseswswnenwswnwnwsewwnwsene
sewnenenenesenwsewnenwwwse
wenwwweseeeweswwwnwwe
wsweesenenewnwwnwsenewsenwwsesesenwne
neeswseenwwswnwswswnw
nenwswwsewswnenenewsenwsenwnesesenew
enewnwewneswsewnwswenweswnenwsenwsw
sweneswneswneneenwnewenewwneswswnese
swwesenesewenwneswnwwneseswwne
enesenwswwswneneswsenwnewswseenwsese
wnwnesenesenenwwnenwsewesewsesesew
nenewswnwewswnenesenwnesewesw
eneswnwswnwsenenwnwnwwseeswneewsenese
neswnwewnwnwseenwseesewsenwsweewe
wseweeenwnesenwwwswnew""".splitlines()

DESTS = ['e', 'w', 'ne', 'nw', 'se', 'sw']

def decode(raw_tile, x=0, y=0):
    """Permet d'obtenir la position relative d'une tuile
    
    x et y sont initialisés à 0
    nw=(x,y-1), ne=(x+1,y-1), e=(x+1,y), se=(x,y+1), sw=(x-1,y+1), w=(x-1,y)
    """
    if len(raw_tile) == 0:
        return x, y
    nb = 1
    carac = raw_tile[:1]
    if carac not in DESTS:
        nb += 1
    dest = raw_tile[:nb]
    assert dest in DESTS

    if len(dest) == 1:
        dy = 0
        dx = +1 if dest == 'e' else -1 #'w'
    else:
        # n selon y_mathématique mais -y_informatique
        dy = +1 if dest[0] == 's' else -1 #'n'
        if dest == 'sw':
            dx = -1
        elif dest == 'ne':
            dx = +1
        else: #'se' or 'nw'
            dx = 0

    raw_tile = raw_tile[nb:]
    return decode(raw_tile, x + dx, y + dy)


def get_hex_grid(raw_tiles):
    #tiles switches
    tiles_switches = []

    for raw_tile in raw_tiles:
        # petite optimisation qui enlève qq coups inutiles
        raw_tile = raw_tile.replace('sew', 'sw').replace('swe', 'se')
        raw_tile = raw_tile.replace('new', 'nw').replace('nwe', 'ne')
        tile = decode(raw_tile)
        #print(tile)
        tiles_switches.append(tile)
    
    #dimensions nécessaires
    x_s = [tile[0] for tile in tiles_switches]
    y_s = [tile[1] for tile in tiles_switches]
    x_min, x_max = min(x_s), max(x_s)
    y_min, y_max = min(y_s), max(y_s)

    #hex_grid
    hex_grid = dict()
    for y in range(y_min, y_max + 1):
        hex_grid[y] = dict()
        for x in range(x_min, y_max+1):
            hex_grid[y][x] = tiles_switches.count((x,y)) & 1 # same as % 2
    
    return hex_grid


def dims(hex_grid):
    """(x_min, x_max), (y_min, y_max) de hex_grid
    
    /!\ Il faut y=0 appartienne à la grille
    /!\ On ne vérifie pas que chaque ligne est de la même taille"""
    y_min, y_max = min(hex_grid), max(hex_grid)
    x_min, x_max = min(hex_grid[0]), max(hex_grid[0])
    return (x_min, x_max), (y_min, y_max)

def agrandir_grid(hex_grid):
    """Ajoute une bordure partout"""
    (x_min, x_max), (y_min, y_max) = dims(hex_grid)
    y_min2, y_max2 = y_min - 1, y_max + 1

    hex_grid[y_min2] = dict()
    hex_grid[y_max2] = dict()
    for x in range(x_min,x_max+1):
        hex_grid[y_min2][x] = 0
        hex_grid[y_max2][x] = 0

    for y in range(y_min2, y_max2 + 1):
        hex_grid[y][x_min-1] = 0
        hex_grid[y][x_max+1] = 0

def recadrer(hex_grid):
    """Enlever les lignes et colonnes de bordure vides (inutiles)"""
    (x_min, x_max), (y_min, y_max) = dims(hex_grid)

    # il faut garder y=0 pour pouvoir calculer les dimensions
    if y_min != 0 and not sum(hex_grid[y_min].values()): del hex_grid[y_min]
    if y_max != 0 and not sum(hex_grid[y_max].values()): del hex_grid[y_max]
    (x_min, x_max), (y_min, y_max) = dims(hex_grid)

    if sum([hex_grid[y][x_min] for y in range(y_min, y_max+1)]) == 0:
        for y in range(y_min, y_max+1): del hex_grid[y][x_min]
    if sum([hex_grid[y][x_max] for y in range(y_min, y_max+1)]) == 0:
        for y in range(y_min, y_max+1): del hex_grid[y][x_max]


def number_neighbors(x,y, hex_grid):
    (x_min, x_max), (y_min, y_max) = dims(hex_grid)
    
    res = 0
    # nw=(x,y-1), ne=(x+1,y-1), e=(x+1,y), se=(x,y+1), sw=(x-1,y+1), w=(x-1,y)
    for xv, yv in [(x,y-1), (x+1,y-1), (x+1,y), (x,y+1), (x-1,y+1), (x-1,y)]:
        if x_min <= xv <= x_max and y_min <= yv <= y_max:
            res += hex_grid[yv][xv]
    return res


def game_of_life_1(hex_grid):
    """Un tour du Jeu de la Vie"""
    # on ajoute une bordure pour prévoir l'extension de la grille
    agrandir_grid(hex_grid)
    (x_min, x_max), (y_min, y_max) = dims(hex_grid)

    # construction de la grille des voisins
    voisins = dict()
    for y in range(y_min, y_max+1):
        voisins[y] = dict()
        for x in range(x_min, x_max+1):
            voisins[y][x] = number_neighbors(x, y, hex_grid)    
    #my_utils.print_dict(voisins)
    
    # actualisation de la grille
    for y in range(y_min, y_max+1):
        for x in range(x_min, x_max+1):
            if hex_grid[y][x]: # == 1
                voisin = voisins[y][x]
                if voisin == 0 or voisin > 2:
                    hex_grid[y][x] = 0
            else: # == 0
                if voisins[y][x] == 2:
                    hex_grid[y][x] = 1
    
    # on enlève les bordures vides pour éviter des calculs inutiles
    recadrer(hex_grid)


def game_of_life(hex_grid, n=100):
    """n tours du Jeu de la Vie"""
    for move in range(n):
        #print(move)
        game_of_life_1(hex_grid)

def count_active(hex_grid):
    return sum([sum(hex_grid[y].values()) for y in hex_grid])


""" # Programme pour l'exemple
hex_grid_ex = get_hex_grid(raw_tiles_ex)
#my_utils.print_dict(hex_grid_ex)
assert count_active(hex_grid_ex) == 10
game_of_life(hex_grid_ex)
#my_utils.print_dict(hex_grid_ex)
assert count_active(hex_grid_ex) == 2208
"""

hex_grid = get_hex_grid(raw_tiles)

res1 = count_active(hex_grid)
print(res1)

game_of_life(hex_grid)
res2 = count_active(hex_grid)
print(res2)
