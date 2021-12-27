import inputAoC as aoc

input = """Player 1 starting position: 4
Player 2 starting position: 8"""
#input = aoc.get_input_file(21,2021)
input = input.splitlines()

start1 = int(input[0][-2:]) #-1 compte pas les 10
start2 = int(input[1][-2:])

class Dice:
    def __init__(self) -> None:
        self.last_throw = 0
        self.nb_throws = 0
    
    def rolls(self):
        self.nb_throws += 1
        if self.last_throw == 100: self.last_throw = 1
        else: self.last_throw += 1
        return self.last_throw

class Player:
    def __init__(self,start,name,winning_score, score_init=0) -> None:
        self.pos = start
        self.score = score_init
        self.name = name
        self.winning_score = winning_score
    
    def move(self, total):
        self.pos = (self.pos - 1 + total) % 10 + 1
        self.score += self.pos
    
    def is_win(self):
        return self.score >= self.winning_score
    
    def __str__(self) -> str:
        return "Player " + str(self.name) + ": \tPosition: " + str(self.pos) + "; \tScore: " + str(self.score)

class Game:
    def __init__(self,start1,start2,winning_score=1000) -> None:
        self.winning_score = winning_score
        self.player1 = Player(start1,1,winning_score)
        self.player2 = Player(start2,2,winning_score)
        self.dice = Dice()
        self.next_player = self.player1.name
    
    def get_player(self,name):
        if name == self.player1.name: return self.player1
        if name == self.player2.name: return self.player2
        else: return None
    
    def play(self):
        next_turn = True
        while next_turn:
            player = self.get_player(self.next_player)
            total = 0
            for _ in range(3):
                total += self.dice.rolls()
            player.move(total)
            next_turn = not player.is_win()
            self.next_player = 1 if self.next_player == 2 else 2 
                             # self.next_player % 2 + 1 
                             # 3 - self.next_player
        loser = self.get_player(self.next_player)
        return loser.score * self.dice.nb_throws


game = Game(start1,start2)
res1 = game.play()
print(res1)
