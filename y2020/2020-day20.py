import inputAoC as aoc
import my_utils
import re

tiles = aoc.get_input_file(20, 2020).split("\n\n")

tile_ex = """Tile 2797:
.#...#...#
##........
#...#.....
#.#..#...#
##..#.....
#.....#..#
..#......#
..........
#......#..
...######."""

def get_borders(tile):
    pixels = tile.splitlines()
    title = pixels.pop(0)
    number = re.search(r"Tile (\d+):", title).groups()[0]
    res = dict(number=number)
    res["haut"] = pixels[0]
    res["bas"] = pixels[-1]
    gauche, droite = "", ""
    for ligne in pixels:
        gauche += ligne[0]
        droite += ligne[-1]
    res["gauche"] = gauche
    res["droite"] = droite
    return res

my_utils.print_dict(get_borders(tile_ex))


res1 = 0
print(res1)

res2 = 0
print(res2)