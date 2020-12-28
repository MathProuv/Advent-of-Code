import inputAoC as aoc
import my_utils
import re
from math import prod

tiles_text = aoc.get_input_file(20, 2020).split("\n\n")

tile_ex = """Tile:
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



class Tile:
    """Une tuile = une pièce du puzzle"""
    def __init__(self, tile: str):
        all_pixels = tile.splitlines()
        title = all_pixels.pop(0)
        number_match = re.search(r"Tile (\d+):", title)
        if number_match: self.number = int(number_match.groups()[0])
        else: self.number = int() #0
        self.all_pixels = all_pixels
        self._init_params()

    def _init_params(self) -> None:
        """Initialise les bordures et les pixels"""
        n, m = len(self.all_pixels), len(self.all_pixels[0])
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
            self.pixels[i] = "".join(self.pixels[i])
    
    def get_all_borders(self) -> [str]:
        """Retourne une liste des 8 frontières de la tuile (4 * 2 côtés)"""
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
    
    def get_attribut(self, attribut: str):
        """Retourne l'attribut de la tuile"""
        if attribut == "gauche": return self.gauche
        elif attribut == "droite": return self.droite
        elif attribut == "haut": return self.haut
        elif attribut == "bas": return self.bas
        elif attribut == "all_pixels": return self.all_pixels
        elif attribut == "pixels": return self.pixels
        elif attribut == "number": return self.number
        else: 
            error = "'Tile' object has no attribute '" + attribut + "'"
            raise AttributeError(error)

    def print(self) -> None:
        """affiche les pixels de la tuile"""
        my_utils.print_list(self.all_pixels)
    
    def print_frontiere(self) -> None:
        """affiche la tuile avec une ligne ou colonne vide entre la tuile et ses frontières"""
        print(self.haut[0], "".join(self.haut[1:-1]), self.haut[-1], "\n")
        for i in range(1, len(self.gauche)-1):
            print(self.gauche[i], "".join(self.pixels[i-1]), self.droite[i])
        print("\n"+self.haut[0], "".join(self.haut[1:-1]), self.haut[-1])
    
    def flip(self) -> None:
        """symétrie selon l'axe vertical"""
        for i in range(len(self.all_pixels)):
            self.all_pixels[i] = self.all_pixels[i][::-1]
        self._init_params()
    def rotate90(self) -> None:
        """rotation d'un quart d'heure"""
        res = [""] * len(self.all_pixels)
        for i in range(len(res)):
            res[i] = "".join([line[i] for line in self.all_pixels])[::-1]
        self.all_pixels = res
        self._init_params()
    
    def near_frontiere(self, tile2) -> str:
        """Retourne la frontière en commun (ou "" s'il n'y en a pas)"""
        borders_2 = tile2.get_all_borders()
        for bord in [self.haut, self.bas, self.gauche, self.droite]:
            if bord in borders_2:
                return bord
        return str() #""

    def orientate(self, frontiere, orientation="gauche") -> None:
        """Oriente la tuile pour que frontiere soit au côté orientation"""
        assert frontiere in self.get_all_borders()
        for i in range(16):
            if frontiere == self.get_attribut(orientation):
                break
            elif i==4 or i==12: self.flip()
            self.rotate90()
            if i==8: self.flip()
        assert frontiere == self.get_attribut(orientation)



class Jigsaw:
    """Classe d'un puzzle
    
        Attributes:
        -----------
    tiles
    all_frontieres
    numbers
    raw_image
    decoded_image
    
        Methods:
        --------
    __init__
    get_tile_by_number
    coins
    bordures
    constr
    find_good_voisin
    decode_image
    print
    __repr__
    count_roughness"""

    def __init__(self, tiles: [ Tile ] ):
        """tiles est une liste de Tile"""
        self.tiles = tiles
        self.all_frontieres = []
        self.numbers = []
        for tile in self.tiles:
            self.all_frontieres.extend(tile.get_all_borders())
            self.numbers.append(tile.number)
        self.constr()
    
    def get_tile_by_number(self, number) -> Tile:
        for tile in self.tiles:
            if tile.number == number:
                return tile


    def coins(self) -> [ Tile ] :
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
    
    def bordures(self) -> [ Tile ] :
        """Fonction inutile (dans mon code) qui retourne une liste des tuiles en bordure"""
        res = []
        for tile in self.tiles:
            compt = 0
            bords = [tile.haut, tile.bas, tile.gauche, tile.droite]
            for bord in bords:
                if self.all_frontieres.count(bord) == 1:
                    res.append(tile)
                    break
        return res

    def constr(self) -> list( [ Tile ] ):
        """Retourne une raw_image (un tableau de tuiles)"""
        all_coins = self.coins()
        res = []
        ligne = []
        tiles_backup = []

        tuile = all_coins.pop()
        tiles_backup.append(tuile)
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

            if not voisin: # fin_de_ligne = True
                tuile = ligne[0]
                common_frontiere = tuile.bas
                orientation = "haut"
                res.append(ligne)
                ligne = []

            else: # fin_de_ligne = False
                voisin.orientate(common_frontiere, orientation)
                ligne.append(voisin)
                
                tuile = voisin
                common_frontiere = tuile.droite
                orientation = "gauche"
                
                #en fin de ligne, on l'avait déjà enlevé
                self.tiles.remove(voisin)
                tiles_backup.append(voisin)

        self.tiles = tiles_backup
        self.raw_image = res
        self.decoded_image = self.decode_image() #sans les frontières
        return res


    def find_good_voisin(self, tile: Tile, front: str) -> Tile:
        for tile2 in self.tiles:
            if front in tile2.get_all_borders():
                return tile2


    def decode_image(self, with_frontiere=False) -> [str]:
        res = [""]
        attribut = "pixels" if not with_frontiere else "all_pixels"

        for big_line in self.raw_image: # big_line:  [ Tile ] 
            for i in range(len(big_line[0].get_attribut(attribut))):
                little_line = ""

                for tuile in big_line:
                    little_line += tuile.get_attribut(attribut)[i]
                    if with_frontiere: little_line += "  "
                        
                res.append(little_line)
            if with_frontiere: res.append(" ")

        return res

    def print(self, with_frontiere=False) -> None:
        my_utils.print_list(self.decode_image(with_frontiere))
    
    def __repr__(self) -> str:
        return "\n".join(self.decoded_image)

    def count_roughness(self) -> int:
        # tant qu'on a 0 monstre:
        #     ré-orienter
        # 
        # faire une copie de l'image avec des 0 pour chaque '.' et des 1 pour chaque "#"
        # pour chaque endroit qui peut être le coin sup gauche du monstre:
        #    tester si c'est le monstre
        #       si c'est le monstre:
        #           à chaque case du monstre, mettre 0 dans la copie
        # retourner la somme de la copie

        return 0


tile_ex = Tile(tile_ex)

tiles = [Tile(tile) for tile in tiles_text]
puzzle = Jigsaw(tiles)
#puzzle.print(True)
#my_utils.print_list(puzzle.decoded_image) # puzzle.print(False) # print(puzzle)

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

res1 = prod([int(coin.number) for coin in puzzle.coins()])
print(res1)

res2 = puzzle.count_roughness()
print(res2)