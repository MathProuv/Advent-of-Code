import inputAoC as aoc
from collections import deque

initial_decks = aoc.get_input_file(22, 2020).split("\n\n")
deck1 = [int(card) for card in initial_decks[0].splitlines()[1:]]
deck2 = [int(card) for card in initial_decks[1].splitlines()[1:]]

class Deck:
    """Objet qui représente une p(f)ile de cartes"""
    def __init__(self, initial_deck: [int]):
        self.deck = deque(initial_deck)
    
    def play(self) -> int:
        assert self.is_playable()
        return self.deck.popleft()
    
    def is_playable(self) -> bool:
        return len(self.deck) > 0

    def win(self, card1, card2) -> None:
        # on a card1 = carte_gagnante
        """if card1 < card2:
            card1, card2 = card2, card1"""
        self.deck.append(card1)
        self.deck.append(card2)
    
    def score(self, indice=1, init=0) -> int:
        if len(self.deck) == 0: return init
        last_card = self.deck.pop()
        return self.score(indice + 1, init + last_card * indice)
    
    def __repr__(self) -> str:
        return str(self.deck)

def test_score():
    ex = Deck([3, 2, 10, 6, 8, 5, 9, 4, 7, 1])
    assert ex.score() == 306
    ex2 = Deck([7, 5, 6, 2, 4, 1, 10, 8, 9, 3])
    assert ex2.score() == 291
test_score()


class Combat:
    """Objet qui consiste en un jeu de Combat itératif"""

    def __init__(self, deck1, deck2):
        self.deck1 = Deck(deck1) if type(deck1) != Deck else deck1
        self.deck2 = Deck(deck2) if type(deck2) != Deck else deck1
    
    def game(self) -> Deck:
        while self.deck1.is_playable() and self.deck2.is_playable():
            card1 = self.deck1.play()
            card2 = self.deck2.play()
            gagnant = self.deck1 if card1 > card2 else self.deck2
            if gagnant != self.deck1:
                card1, card2 = card2, card1
            gagnant.win(card1, card2)
        
        gagnant = self.deck1 if not self.deck2.is_playable() else self.deck2
        return gagnant
    
    def resultat(self) -> int:
        gagnant = self.game()
        # print("Le jeu gagnant est :", gagnant)
        score = gagnant.score()
        # print("et son score est", score)
        return score

def test1():
    deck1_1 = [9, 2, 6, 3, 1]
    deck2_1 = [5, 8, 4, 7, 10]
    ex1 = Combat(Deck(deck1_1), deck2_1).resultat()
    assert ex1 == 306
test1()


this_game = Combat(deck1, deck2)
res1 = this_game.resultat()
print(res1)



class CombatRec:
    """Objet qui consiste en un jeu de Combat récursif"""

    def __init__(self, deck1, deck2, is_sous_game=False):
        self.deck1 = Deck(deck1) if type(deck1) != Deck else deck1
        self.deck2 = Deck(deck2) if type(deck2) != Deck else deck1
        self.configs = []
        self.is_sous_game = is_sous_game


    def game(self) -> str:
        jeu_infini = False
        while not jeu_infini and self.deck1.is_playable() and self.deck2.is_playable():
            # print(self.deck1, self.deck2)
            card1 = self.deck1.play()
            card2 = self.deck2.play()

            gagnant, card1, card2 = self.sub_game(card1, card2, self.deck1, self.deck2)
            gagnant.win(card1, card2)

            config = (tuple(self.deck1.deck), tuple(self.deck2.deck))
            if config in self.configs:
                jeu_infini = True
                grand_gagnant = "deck1"
            self.configs.append(config)
        
        if not jeu_infini: #on n'est pas arrivé sur un jeu infini
            assert not self.deck1.is_playable() or not self.deck2.is_playable()
            if not self.deck2.is_playable():
                grand_gagnant = "deck1"
            else:
                grand_gagnant = "deck2"

        return grand_gagnant

    
    def sub_game(self, card1: int, card2: int, deck1: Deck, deck2: Deck) -> (Deck, int, int):
        """Retourne le deck gagnant, la carte gagnante et la carte perdante"""

        if len(deck1.deck) >= card1 and len(deck2.deck) >= card2:
            # print("Il faut un sous-game ici. On est déja dans un sous-game :", self.is_sous_game)
            sous_gagnant = CombatRec(list(self.deck1.deck)[:card1], list(self.deck2.deck)[:card2], True).game()
            gagnant = self.deck1 if sous_gagnant == "deck1" else self.deck2
            # print("on sort de la sous-game")
        else:
            gagnant = deck1 if card1 > card2 else deck2

        if gagnant != deck1: # on remet les cartes dans l'ordre
            card1, card2 = card2, card1

        return gagnant, card1, card2
    
    def resultat(self) -> int:
        gagnant = self.game()
        deck_gagnant = self.deck1 if gagnant == "deck1" else self.deck2
        # print("Le jeu gagnant est :", deck_gagnant)
        score = deck_gagnant.score()
        # print("et son score est", score)
        return score

def test_2():
    deck1_2 = [9, 2, 6, 3, 1]
    deck2_2 = [5, 8, 4, 7, 10]
    ex2 = CombatRec(deck1_2, deck2_2).resultat()
    assert ex2 == 291
test_2()

def test_infini():
    deck1_3 = [43, 19]
    deck2_3 = [2, 29, 14]
    ex3 = CombatRec(deck1_3, deck2_3).resultat()
    # le test est réussi si la fonction est finie
    # (car on est sorti d'un jeu infini)
test_infini()



this_game_rec = CombatRec(deck1, deck2)
res2 = this_game_rec.resultat()
print(res2)
