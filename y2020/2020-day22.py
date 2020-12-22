import inputAoC as aoc
from collections import deque

initial_decks = aoc.get_input_file(22, 2020).split("\n\n")
deck1 = [int(card) for card in initial_decks[0].splitlines()[1:]]
deck2 = [int(card) for card in initial_decks[1].splitlines()[1:]]

class Deck:
    """Objet qui représente une p(f)ile de cartes"""
    def __init__(self, initial_deck: [int]) -> Deck:
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
    
    def __repr__(self):
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
    
    def game(self):
        while self.deck1.is_playable() and self.deck2.is_playable():
            card1 = self.deck1.play()
            card2 = self.deck2.play()
            gagnant = self.deck1 if card1 > card2 else self.deck2
            gagnant.win(card1, card2)
        return self.resultat()
    
    def resultat(self):
        assert not self.deck1.is_playable() or not self.deck2.is_playable()
        gagnant = self.deck1 if not self.deck2.is_playable() else self.deck2
        # print("Le jeu gagnant est :", gagnant)
        score = gagnant.score()
        # print("Le score est :", score)
        return score


this_game = Combat(deck1, deck2)
res1 = this_game.game()
print(res1)

