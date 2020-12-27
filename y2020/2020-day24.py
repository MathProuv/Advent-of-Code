import inputAoC as aoc

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
    print(tile)
    tiles_switches.append(tile)

res1 = 0

for tile in set(tiles_switches):
    res1 += tiles_switches.count(tile) % 2

print(res1)