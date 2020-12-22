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
        # on veut card1 > card2
        if card1 < card2:
            card1, card2 = card2, card1
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
# test_score()

class Combat:
    """Objet qui consiste en un jeu de Combat itératif"""

    def __init__(self, deck1, deck2):
        self.deck1 = Deck(deck1) if type(deck1) != Deck else deck1
        self.deck2 = Deck(deck2) if type(deck2) != Deck else deck1
    
    def game(self) -> int:
        while self.deck1.is_playable() and self.deck2.is_playable():
            card1 = self.deck1.play()
            card2 = self.deck2.play()
            gagnant = self.deck1 if card1 > card2 else self.deck2
            gagnant.win(card1, card2)
        
        gagnant = self.deck1 if not self.deck2.is_playable() else self.deck2
        score = gagnant.score()
        # print("Le jeu gagnant est :", winner, "et son score est", score)
        return score


this_game = Combat(deck1, deck2)
res1 = this_game.game()
print(res1)


class CombatRec:
    """Objet qui consiste en un jeu de Combat récursif"""

    def __init__(self, deck1, deck2):
        self.deck1 = Deck(deck1) if type(deck1) != Deck else deck1
        self.deck2 = Deck(deck2) if type(deck2) != Deck else deck1
        self.configs = []

    def game(self):
        jeu_infini = False
        while not jeu_infini and self.deck1.is_playable() and self.deck2.is_playable():
            card1 = self.deck1.play()
            card2 = self.deck2.play()

            gagnant, card1, card2 = self.sub_game(card1, card2, self.deck1, self.deck2)
            gagnant.win(card1, card2)

            config = (tuple(self.deck1.deck), tuple(self.deck2.deck))
            
            if config in self.configs:
                jeu_infini = True
                grand_gagnant = deck1
            self.configs.append(config)
        
        if not jeu_infini: #on n'est pas arrivé sur un jeu infini
            assert not self.deck1.is_playable() or not self.deck2.is_playable()
            grand_gagnant = self.deck1 if not self.deck2.is_playable() else self.deck2


        score = grand_gagnant.score()
        # print("Le jeu gagnant est :", winner, "et son score est", score)
        return score
    
    def sub_game(self, card1: int, card2: int, deck1: Deck, deck2: Deck) -> (Deck, int, int):
        if len(deck1.deck) >= card1 and len(deck2.deck) >= card2:
            print("Il faut un sous-game")

        gagnant = deck1 if card1 > card2 else deck2

        if gagnant != deck1: # on remet les cartes dans l'ordre
            card1, card2 = card2, card1
        
        return gagnant, card1, card2

this_game_rec = CombatRec(deck1, deck2)
res2 = this_game_rec.game()
print(res2)