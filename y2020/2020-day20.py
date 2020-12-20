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
    """Une tuile = une pièce du puzzle"""
    def __init__(self, tile: str):
        all_pixels = tile.splitlines()
        title = all_pixels.pop(0)
        self.number = re.search(r"Tile (\d+):", title).groups()[0]
        self.all_pixels = all_pixels

    def summary(self) -> None:
        """Initialise les bordures et les pixels du centre"""
        n, m = len(self.all_pixels), len(self.all_pixels[0])
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
    
    def get_borders_set(self) -> set(str):
        res = set()
        haut = self.all_pixels[0]
        res.add(haut)
        res.add(haut[::-1])
        bas = self.all_pixels[-1]
        res.add(bas)
        res.add(bas[::-1])
        gauche, droite = "", ""
        for line in self.all_pixels:
            gauche += line[0]
            droite += line[-1]
        res.add(gauche)
        res.add(gauche[::-1])
        res.add(droite)
        res.add(droite[::-1])
        return res

    def print(self):
        my_utils.print_list(self.all_pixels)
        # print(self.haut[0], "".join(self.haut[1:-1]), self.haut[-1], "\n")
        # for i in range(1, len(self.gauche)-1):
        #     print(self.gauche[i], "".join(self.pixels[i-1]), self.droite[i])
        # print("\n"+self.haut[0], "".join(self.haut[1:-1]), self.haut[-1])
    
    def flip(self):
        """symétrie selon l'axe vertical"""
        for i in range(len(self.all_pixels)):
            self.all_pixels[i] = self.all_pixels[i][::-1]
    def flop(self):
        """symetrie selon l'axe horizontal"""
        res = []
        for i in range(len(self.all_pixels))[::-1]:
            res.append(self.all_pixels[i])
        self.all_pixels = res
    def rotate90(self):
        """rotation d'un quart d'heure"""
        res = [""] * len(self.all_pixels)


class Jigsaw:
    def __init__(self, tiles: [Tile]):
        pass

    def coins(self)


res2 = 0
print(res2)