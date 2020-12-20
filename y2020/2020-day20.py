import inputAoC as aoc
import my_utils
import re
from math import prod
import numpy as np

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

def flip(tile):
    pixels = tile.splitlines()
    title = pixels.pop(0)
    res_pixels = []
    for line in pixels:
        res_pixels.append(line[::-1])
    res = [title]
    res.extend(res_pixels)
    return "\n".join(res)

def rotate180(tile):
    pixels = tile.splitlines()
    title = pixels.pop(0)
    res_pixels = []
    for line in pixels[::-1]:
        res_pixels.append(line[::-1])
    res = [title]
    res.extend(res_pixels)
    return "\n".join(res)


def summary(tile: str) -> dict:
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
#my_utils.print_dict(summary(tile_ex))

def get_borders(tile: str) -> set:
    sommaire = summary(tile)
    res = []
    for field, val in sommaire.items():
        if field != "number":
            res.append(val)
    return res

def bords(tiles):
    frontieres = []
    res = []
    for tile in tiles:
        bordures = get_borders(tile)
        for bord in bordures:
            frontieres.append(bord)
            frontieres.append(bord[::-1])
    for tile in tiles:
        sommaire = summary(tile)
        for field in ["haut", "bas", "gauche", "droite"]:
            if frontieres.count(sommaire[field]) == 1:
                res.append(int(sommaire["number"]))
                break
    print(len(res))
    return res

def coins(tiles):
    frontieres = []
    res = []
    for tile in tiles:
        bordures = get_borders(tile)
        for bord in bordures:
            frontieres.append(bord)
            frontieres.append(bord[::-1])
    for tile in tiles:
        sommaire = summary(tile)
        compt = 0
        for field in ["haut", "bas", "gauche", "droite"]:
            if frontieres.count(sommaire[field]) == 1:
                compt += 1
        if compt == 2:
            res.append(int(sommaire["number"]))
    print(len(res))
    return res

bords(tiles)
res1 = prod(coins(tiles))
print(res1)


class Tile:
    def __init__(self, tile: str):
        all_pixels = tile.splitlines()
        title = all_pixels.pop(0)
        n, m = len(all_pixels), len(all_pixels[0])
        self.number = re.search(r"Tile (\d+):", title).groups()[0]
        self.haut = all_pixels[0]
        self.bas = all_pixels[-1]
        gauche, droite = "", ""
        for ligne in all_pixels:
            gauche += ligne[0]
            droite += ligne[-1]
        self.gauche = gauche
        self.droite = droite
        self.pixels = [" "] * (n-2)
        for i in range(n-2):
            self.pixels[i] = [" "] * (m-2)
            for j in range(m-2):
                self.pixels[i][j] = all_pixels[i+1][j+1]
        
    def print(self):
        print(self.haut[0], "".join(self.haut[1:-1]), self.haut[-1], "\n")
        for i in range(len(self.gauche)):
            print(self.gauche[i], "".join(self.pixels[i]), self.droite[i])
        print(self.haut[0], "".join(self.haut[1:-1]), self.haut[-1], "\n")

tile_obj_ex = Tile(tile_ex)
tile_obj_ex.print()

res2 = 0
print(res2)