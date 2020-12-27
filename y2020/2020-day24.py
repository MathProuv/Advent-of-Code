""" Une grille hex représentée dans un tableau 2D:

y = -2: -2  -1  +0  +1  +2
y = -1:   -2  -1  +0  +1  +2
y =  0:     -2  -1  +0  +1  +2
y = +1:       -2  -1  +0  +1  +2

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
        dy = +1 if dest[0] == 'n' else -1 #'s'
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
        # petite optimisation
        raw_tile = raw_tile.replace('sew', 'sw').replace('swe', 'se')
        raw_tile = raw_tile.replace('new', 'nw').replace('nwe', 'ne')
        tile = decode(raw_tile)
        #print(tile)
        tiles_switches.append(tile)
    
    #hex_grid
    x_s = [tile[0] for tile in tiles_switches]
    y_s = [tile[1] for tile in tiles_switches]
    x_min, x_max = min(x_s), max(x_s)
    y_min, y_max = min(y_s), max(y_s)

    hex_grid = dict()
    for y in range(y_min, y_max + 1):
        hex_grid[y] = dict()
        for x in range(x_min, y_max+1):
            hex_grid[y][x] = tiles_switches.count((x,y)) % 2
    
    return hex_grid


def dims(hex_grid):
    y_min, y_max = min(hex_grid), max(hex_grid)
    x_min, x_max = min(hex_grid[0]), max(hex_grid[0])
    return (x_min, x_max), (y_min, y_max)

def agrandir_grid(hex_grid):
    (x_min, x_max), (y_min, y_max) = dims(hex_grid)
    y_min2, y_max2 = y_min - 1, y_max + 1

    hex_grid[y_min2] = dict()
    hex_grid[y_max2] = dict()
    for x in range(x_min,x_max+1):
        hex_grid[y_min2][x] = 0
        hex_grid[y_max2][x] = 0

    for y in range(y_min2, y_max2 + 1):
        hex_grid[y][x_min - 1] = 0
        hex_grid[y][x_max + 1] = 0

def recadrer(hex_grid):
    """Enlever les lignes de y inutiles"""
    y_min, y_max = dims(hex_grid)[1]
    if y_min != 0 and not sum(hex_grid[y_min].values()): del hex_grid[y_min]
    if y_max != 0 and not sum(hex_grid[y_max].values()): del hex_grid[y_max]

def number_neighbors(x,y, hex_grid):
    (x_min, x_max), (y_min, y_max) = dims(hex_grid)
    #nw=(x,y-1), ne=(x+1,y-1), e=(x+1,y), se=(x,y+1), sw=(x-1,y+1), w=(x-1,y)

    res = 0
    for xv, yv in [(x,y+1), (x+1,y+1), (x+1,y), (x,y-1), (x-1,y-1), (x-1,y)]:
        if x_min <= xv <= x_max and y_min <= yv <= y_max:
            res += hex_grid[yv][xv]
    return res


def game_of_life_1(hex_grid):
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
            if hex_grid[y][x] == 1:
                if voisins[y][x] == 0 or voisins[y][x] > 2:
                    hex_grid[y][x] = 0
            else: # == 0
                if voisins[y][x] == 2:
                    hex_grid[y][x] = 1
    
    recadrer(hex_grid)

def game_of_life(hex_grid, n=100):
    for move in range(n):
        #print(move)
        game_of_life_1(hex_grid)



hex_grid_ex = get_hex_grid(raw_tiles_ex)
#my_utils.print_dict(hex_grid_ex)
assert sum([sum(hex_grid_ex[y].values()) for y in hex_grid_ex]) == 10
#game_of_life(hex_grid_ex)
#my_utils.print_dict(hex_grid_ex)
#assert sum([sum(hex_grid_ex[y].values()) for y in hex_grid_ex]) == 2208


hex_grid = get_hex_grid(raw_tiles)

res1 = sum([sum(hex_grid[y].values()) for y in hex_grid])
print(res1)

game_of_life(hex_grid)
res2 = sum([sum(hex_grid[y].values()) for y in hex_grid])
print(res2)
# 49959 is too high


