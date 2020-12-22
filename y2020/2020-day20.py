import inputAoC as aoc
import my_utils
import re
from math import prod
import numpy as np

tiles_text = aoc.get_input_file(20, 2020).split("\n\n")

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
    assert len(res) == 4
    return res


res1 = prod(coins(tiles_text))
print(res1)


class Tile:
    """Une tuile = une pièce du puzzle"""
    def __init__(self, tile: str):
        all_pixels = tile.splitlines()
        title = all_pixels.pop(0)
        self.number = re.search(r"Tile (\d+):", title).groups()[0]
        self.all_pixels = all_pixels
        self.re_init_params()

    def re_init_params(self) -> None:
        """Initialise les bordures et les pixels du centre"""
        n, m = len(self.all_pixels), len(self.all_pixels[0])
        self.etat = True
        self.haut = self.all_pixels[0]
        self.bas = self.all_pixels[-1]
        gauche, droite = "", ""
        for ligne in self.all_pixels:
            gauche += ligne[0]
            droite += ligne[-1]
        self.gauche = gauche
        self.droite = droite
        self.pixels = [" "] * (n-2)
        for i in range(n-2):
            self.pixels[i] = [" "] * (m-2)
            for j in range(m-2):
                self.pixels[i][j] = self.all_pixels[i+1][j+1]
    
    def get_all_borders(self):
        res = []
        haut = self.all_pixels[0]
        res.append(haut)
        res.append(haut[::-1])
        bas = self.all_pixels[-1]
        res.append(bas)
        res.append(bas[::-1])
        gauche, droite = "", ""
        for line in self.all_pixels:
            gauche += line[0]
            droite += line[-1]
        res.append(gauche)
        res.append(gauche[::-1])
        res.append(droite)
        res.append(droite[::-1])
        return res
    
    def get_attribut(self, orientation):
        if orientation == "gauche": return self.gauche
        elif orientation == "droite": return self.droite
        elif orientation == "haut": return self.haut
        elif orientation == "bas": return self.bas
        else: raise TypeError

    def print(self):
        my_utils.print_list(self.all_pixels)
    
    def print_frontiere(self):
        """affiche la tuile avec une ligne ou colonne vide entre la tuile et ses frontières"""
        print(self.haut[0], "".join(self.haut[1:-1]), self.haut[-1], "\n")
        for i in range(1, len(self.gauche)-1):
            print(self.gauche[i], "".join(self.pixels[i-1]), self.droite[i])
        print("\n"+self.haut[0], "".join(self.haut[1:-1]), self.haut[-1])
    
    def flip(self):
        """symétrie selon l'axe vertical"""
        for i in range(len(self.all_pixels)):
            self.all_pixels[i] = self.all_pixels[i][::-1]
        self.re_init_params()
    def rotate90(self):
        """rotation d'un quart d'heure"""
        res = [""] * len(self.all_pixels)
        for i in range(len(res)):
            res[i] = "".join([line[i] for line in self.all_pixels])[::-1]
        self.all_pixels = res
        self.re_init_params()
    
    def near_frontiere(self, tile2):
        """Retourne la frontière en commun ou None"""
        borders_2 = tile2.get_all_borders()
        for bord in [self.haut, self.bas, self.gauche, self.droite]:
            if bord in borders_2:
                return bord
        return None

    def orientate(self, frontiere, orientation="gauche"):
        assert frontiere in self.get_all_borders()
        for i in range(16):
            if frontiere == self.get_attribut(orientation):
                break
            elif i==4 or i==12: self.flip()
            self.rotate90()
            if i==8: self.flip()
        assert frontiere == self.get_attribut(orientation)



class Jigsaw:
    def __init__(self, tiles: [Tile]):
        self.tiles = tiles
        self.all_frontieres = []
        self.numbers = []
        for tile in self.tiles:
            self.all_frontieres.extend(tile.get_all_borders())
            self.numbers.append(tile.number)
    
    def get_tile(self, number) -> Tile:
        for tile in self.tiles:
            if tile[number] == number:
                return tile


    def coins(self) -> [Tile]:
        res = []
        for tile in self.tiles:
            compt = 0
            bords = [tile.haut, tile.bas, tile.gauche, tile.droite]
            for bord in bords:
                if self.all_frontieres.count(bord) == 1:
                    compt += 1
            if compt == 2:
                res.append(tile)
        return res
    
    def bordures(self) -> [Tile]:
        res = []
        for tile in self.tiles:
            compt = 0
            bords = [tile.haut, tile.bas, tile.gauche, tile.droite]
            for bord in bords:
                if self.all_frontieres.count(bord) == 1:
                    res.append(tile)
                    break
        return res

    def constr(self):
        all_coins = self.coins()
        res = []
        ligne = []

        tuile = all_coins.pop()
        self.tiles.remove(tuile)
        while self.all_frontieres.count(tuile.droite) <= 1 or self.all_frontieres.count(tuile.bas) <= 1:
            tuile.rotate90()

        common_frontiere = tuile.droite
        orientation = "gauche"
        ligne.append(tuile)
        
        while self.tiles:
            # trouver la tuile suivante (qui partage la frontière)
            voisin = self.find_good_voisin(tuile, common_frontiere)
            # print(tuile.number, orientation)

            # S'il n'y a pas de tuile voisine, on est en fin de ligne
            # En fonction de cela, on doit
            # determiner la piece dont il faudra trouver le voisin
            # en connaissant sa frontière et son orientation

            if not voisin:
                # fin_de_ligne = True

                tuile = ligne[0]
                common_frontiere = tuile.bas
                orientation = "haut"
                res.append(ligne)
                ligne = []

            else:
                # fin_de_ligne = False
                voisin.orientate(common_frontiere, orientation)
                ligne.append(voisin)
                
                tuile = voisin
                common_frontiere = tuile.droite
                orientation = "gauche"
                
                #en fin de ligne, on l'avait déjà enlevé
                self.tiles.remove(voisin)
        
            
        # coller toutes les pièces
        # retourner le résultat
        self.raw_image = res
        return res


    def find_good_voisin(self, tile: Tile, front: str) -> Tile:
        for tile2 in self.tiles:
            if front in tile2.get_all_borders():
                return tile2


    def count_roughness(self):
        pass
        # tant qu'on a 0 monstre:
        #     ré-orienter
        # 
        # faire une copie de l'image avec des 0 pour chaque '.' et des 1 pour chaque "#"
        # pour chaque endroit qui peut être le coin sup gauche du monstre:
        #    tester si c'est le monstre
        #       si c'est le monstre:
        #           à chaque case du monstre, mettre 0 dans la copie
        # retourner la somme de la copie




tiles = [Tile(tile) for tile in tiles_text]
puzzle = Jigsaw(tiles)
puzzle.constr()


def test1():
    this_tile = tiles[0]
    voisins = []
    for tile in tiles[1:]:
        if tile.near_frontiere(this_tile):
            voisins.append(tile)
    for tile in voisins:
        if this_tile.bas in tile.get_all_borders():
            tile_bas = tile
    for tile in voisins:
        if this_tile.haut in tile.get_all_borders():
            tile_haut = tile

    tile_haut.orientate(this_tile.haut, "bas")
    tile_haut.print()

    this_tile.print()
    tile_bas.orientate(this_tile.bas, "haut")
    tile_bas.print()
# test1()

res2 = 0
print(res2)