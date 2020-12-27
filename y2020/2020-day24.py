""" Une grille hex représentée dans un tableau 2D:
y = -2: -2  -1  +0  +1  +2
y = -1:   -2  -1  +0  +1  +2
y =  0:     -2  -1  +0  +1  +2
y = +1:       -2  -1  +0  +1  +2
"""

import inputAoC as aoc
import my_utils

DESTS = ['e', 'w', 'ne', 'nw', 'se', 'sw']

def decode(raw_tile, x=0, y=0):
    if len(raw_tile) == 0:
        return x, y
    nb = 1
    carac = raw_tile[:1]
    if carac not in DESTS:
        nb += 1
    dest = raw_tile[:nb]

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

raw_tiles = aoc.get_input_file(24,2020).splitlines()

tiles_switches = []

for raw_tile in raw_tiles:
    # petite optimisation
    raw_tile = raw_tile.replace('sew', 'sw').replace('swe', 'se')
    raw_tile = raw_tile.replace('new', 'nw').replace('nwe', 'ne')
    tile = decode(raw_tile)
    #print(tile)
    tiles_switches.append(tile)



x_s = [tile[0] for tile in tiles_switches]
y_s = [tile[1] for tile in tiles_switches]
x_min, x_max = min(x_s), max(x_s)
y_min, y_max = min(y_s), max(y_s)

hex_grid = dict()
for y in range(y_min, y_max + 1):
    hex_grid[y] = dict()
    for x in range(x_min, y_max+1):
        hex_grid[y][x] = tiles_switches.count((x,y)) % 2


res1 = sum([sum(hex_grid[y].values()) for y in hex_grid])
print(res1)


agrandir_grid = my_utils.agrandir_grid