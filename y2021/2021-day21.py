from collections import defaultdict
import inputAoC as aoc

input = """Player 1 starting position: 4
Player 2 starting position: 8"""
input = aoc.get_input_file(21,2021)

start1,start2 = map(lambda x: int(x[-2:]),input.splitlines())

class Dice:
    def __init__(self) -> None:
        self.last_throw = 0
        self.nb_throws = 0
    
    def rolls(self):
        total = 0
        for _ in range(3):
            self.nb_throws += 1
            self.last_throw = self.last_throw % 100 + 1
            total += self.last_throw
        return total

class Player:
    def __init__(self,start,name=0,score_init=0) -> None:
        self.pos = start
        self.score = score_init
        self.name = name
    
    def move(self, total):
        self.pos = (self.pos - 1 + total) % 10 + 1
        self.score += self.pos
    
    def has_won(self,winning_score):
        return self.score >= winning_score
    
    def __str__(self) -> str:
        return "Player " + str(self.name) + ": \tPosition: " + str(self.pos) + "; \tScore: " + str(self.score)

class Game:
    dice = Dice()
    def __init__(self,start1,start2,winning_score=1000,score1=0,score2=0) -> None:
        self.winning_score = winning_score
        self.player1 = Player(start1,1,score1)
        self.player2 = Player(start2,2,score2)
        self.next_player = self.player1.name
    
    def get_player(self,name):
        if name == self.player1.name: return self.player1
        if name == self.player2.name: return self.player2
        return None

    def __str__(self) -> str:
        return str(self.player1) + '\t' + str(self.player2)
    
    def copy(self):
        result = Game(self.player1.pos,self.player2.pos,self.winning_score,self.player1.score,self.player2.score)
        result.next_player = self.next_player
        return result

    def turn(self,total=None):
        if not total: total = self.dice.rolls()
        next_player = self.get_player(self.next_player)
        next_player.move(total)
        self.next_player = self.player1.name if self.next_player == self.player2.name else self.player2.name
        return not next_player.has_won(self.winning_score)

    def play(self):
        while self.turn(): pass
        loser = self.get_player(self.next_player)
        return loser.score * self.dice.nb_throws
    
    def player_win(self):
        if self.player1.has_won(self.winning_score): return self.player1.name
        if self.player2.has_won(self.winning_score): return self.player2.name
        return None

game = Game(start1,start2)
res1 = game.play()
print(res1)

class DiracDice:
    def __init__(self) -> None:
        self.totals = defaultdict(int)
        for i in range(1,4):
            for j in range(1,4):
                for k in range(1,4): self.totals[i+j+k] += 1

def score(state):
    score1,score2,pos1,pos2,next_player,occurrence = state
    return score1 + score2

def turn(score,pos,total):
    new_pos = (pos + total -1) %10 +1
    return score+new_pos, new_pos

def next_states(state):
    score1,score2,pos1,pos2,next_player,occurrence = state
    res = []
    dice = DiracDice()
    if next_player == 1:
        for throw, nb in dice.totals.items():
            new_score1,new_pos1 = turn(score1,pos1,throw)
            new_state = [new_score1,score2,new_pos1,pos2,2,occurrence*nb]
            res.append(new_state)
    else:
        for throw, nb in dice.totals.items():
            new_score2,new_pos2 = turn(score2,pos2,throw)
            new_state = [score1,new_score2,pos1,new_pos2,1,occurrence*nb]
            res.append(new_state)
    return res

def nb_victories(start1, start2):
    winning_score = 21
    victories = [0,0]
    # state = (score1,score2,pos1,pos2,1or2,occurrence)
    states = {0:[[0,0,start1,start2,1,1]]}
    for i in range(1,43): states[i] = []
    #print(states)
    for i in range(43):
        for state in states[i]:
            new_states = next_states(state)
            for new_state in new_states:
                if new_state[0] >= 21: victories[0] += new_state[-1]
                elif new_state[1] >= 21: victories[1] += new_state[-1]
                else:
                    new_score = score(new_state)
                    for s in states[new_score]:
                        if s[:-1] == new_state[:-1]:
                            s[-1] += new_state[-1]
                            break
                    else:
                        states[new_score].append(new_state)
    return victories

res2 = nb_victories(start1,start2)
print(res2)

exit()

###############################################################################
##############  A retravailler pour réussir en POO mais fuck it  ##############
###############################################################################

class PlayerAbstrait:
    def __init__(self,score,pos) -> None:
        self.score = score
        self.pos = pos
    def get_info(self):
        """return score, pos"""
        return self.score,self.pos
    def turn(self,total):
        """return info of self after a turn without changing self"""
        new_pos = (self.pos + total - 1) % 10 + 1
        new_score = self.score + new_pos
        return new_score, new_pos
    def has_won(self, winning_score):
        return self.score >= winning_score
    def __eq__(self, __o: object) -> bool:
        if not isinstance(__o,PlayerAbstrait): return False
        return self.get_info() == __o.get_info()
    def __str__(self) -> str:
        return "Score= " + str(self.score) + '\tPosition: ' + str(self.pos)

class State:
    dice = DiracDice()
    def __init__(self,player1:PlayerAbstrait,player2:PlayerAbstrait,next_player:int=1,occurrence:int=1) -> None:
        """State(self,score1,score2,pos1,pos2,next_player,occurrence):
            State(PlayerAbstrait(score1,pos1),PlayerAbstrait(score2,pos2),next_player,occurrence)"""
        self.player1 = player1
        self.player2 = player2
        self.next_player = next_player
        self.occurrence = occurrence

    def __eq__(self, __o: object) -> bool:
        if not isinstance(__o,State): return False
        return (self.player1 == __o.player1) and (self.player2 == __o.player2) and (self.next_player == __o.next_player)
    
    def __str__(self) -> str:
        return "Player1:\t" + str(self.player1) + '\nPlayer2:\t' + str(self.player2) + \
            "\nnext_player= " + str(self.next_player) + "\tNb d'occurrences= " + str(self.occurrence) + \
                ('\t\t\tno winner yet' if not self.has_win() else '\t\t\t Winner'+str(self.has_win()))

    def __key__(self) -> int:
        return self.player1.score + self.player2.score

    def next_states(self):
        res = []
        if self.next_player == 1:
            for throw,nb in self.dice.totals.items():
                score1,pos1 = self.player1.turn(throw)
                score2,pos2 = self.player2.get_info()
                res.append(State(PlayerAbstrait(score1,pos1), PlayerAbstrait(score2,pos2),2,self.occurrence*nb))
        elif self.next_player == 2:
            for throw,nb in self.dice.totals.items():
                score1,pos1 = self.player1.get_info()
                score2,pos2 = self.player2.turn(throw)
                res.append(State(PlayerAbstrait(score1,pos1), PlayerAbstrait(score2,pos2),1,self.occurrence*nb))
        return res

    def has_win(self,winning_score=21):
        if self.player1.has_won(winning_score): return 1
        elif self.player2.has_won(winning_score): return 2
        else: return 0
    
    def add_occurrence(self,new_occurrence):
        self.occurrence += new_occurrence

def count_universes(start1,start2):
    victories = [None,0,0]
    state_init = State(PlayerAbstrait(0,start1),PlayerAbstrait(0, start2))
    all_states = [state_init]
    turn = 0
    while all_states:
        turn += 1
        state = all_states.pop()
        new_states = state.next_states()
        if turn <= 3:
            print("new states")
            for new_state in new_states: print(new_state)
        for new_state in new_states:
            winner = new_state.has_win()
            if winner:
                victories[winner] += new_state.occurrence
            else:
                if new_state in all_states:
                    idx = all_states.index(new_state)
                    all_states[idx].add_occurrence(new_state.occurrence)
                else:
                    all_states.append(new_state)
        all_states.sort(key=lambda x:x.__key__(),reverse=True)
        if turn <= 3:
            print("all states")
            for state in all_states: print(state)
            print()
    return max(victories[1:])

def count_universes_dict(start1,start2):
    victories = [None,0,0]
    state_init = State(PlayerAbstrait(0,start1),PlayerAbstrait(0, start2))
    all_states = {0:[state_init]}
    for i in range(1,43): all_states[i] = []
    idx = 0
    while idx < 43:
        idx = min(all_states.keys())
        for state in all_states[idx]:
            new_states = state.next_states()
            if idx <= 2:
                print("new states")
                for new_state in new_states: print(new_state)
            for new_state in new_states:
                #print(new_state.__key__(),new_state)
                assert new_state.__key__() <= idx
                winner = new_state.has_win()
                if winner >= 1:
                    victories[winner] += new_state.occurrence
                else:
                    key = new_state.__key__()
                    if new_state in all_states[key]:
                        idx = all_states[key].index(new_state)
                        all_states[key][idx].add_occurrence(new_state.occurrence)
                    else:
                        all_states[key].append(new_state)
            if idx <= 2:
                print("all states")
                for state in all_states: print(state)
                print()
        del all_states[idx]
    return max(victories[1:])

res2 = count_universes_dict(start1,start2)
print(res2)

exit()

###  Modélisation interminable ###

class Universe:
    def __init__(self,game,occurrence) -> None:
        self.game = game
        self.occurrence = occurrence
    def __str__(self) -> str:
        return str(self.occurrence) + self.game.__str__()

class DiracGame:
    dice = DiracDice()
    def __init__(self,start1,start2,winning_score=21) -> None:
        game = Game(start1,start2,winning_score)
        universe_start = Universe(game,1)
        self.universes = [universe_start]
        self.victories = [0,0]
    
    def play(self):
        begin = 0
        while self.universes:
            universe = self.universes.pop()
            for throw,nb in self.dice.totals.items():
                game_temp = universe.game.copy()
                game_temp.turn(throw)
                winner = game_temp.player_win()
                if not winner:
                    self.universes.append(Universe(game_temp,universe.occurrence*nb))
                else: 
                    self.victories[winner-1] += universe.occurrence*nb
            if begin <= 2:
                print("Tour",begin+1)
                for univ in self.universes:
                    print(univ.game)
            begin += 1
            print(self.victories[0])
        return max(self.victories)

game2 = DiracGame(start1, start2,21)
res2 = game2.play()
print(res2)
