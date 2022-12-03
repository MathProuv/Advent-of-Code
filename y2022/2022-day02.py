import inputAoC as aoc

input = """A Y
B X
C Z"""
input = aoc.get_input_file(2,2022)
games = input.split("\n")

cycle_x = ["X","Y","Z"]
cycle = ["A","B","C"]

def score1(game):
    res = (cycle_x.index(game[2]) - cycle.index(game[0]) + 1) % 3 * 3
    return res + cycle_x.index(game[2]) + 1

res1 = sum([score1(game) for game in games])
print(res1)

def score2(game):
    if game[2] == "X":
        return (cycle.index(game[0])+2)%3 + 1
    elif game[2] == "Y":
        return 3 + (cycle.index(game[0]))%3 + 1
    else: # game[2] == "Z":
        return 6 + (cycle.index(game[0])+1)%3 + 1
    # 1st approach
    res = {}
    res["A X"] = 3
    res["B X"] = 1
    res["C X"] = 2
    res["A Y"] = 1 + 3
    res["B Y"] = 2 + 3
    res["C Y"] = 3 + 3
    res["A Z"] = 2 + 6
    res["B Z"] = 3 + 6
    res["C Z"] = 1 + 6
    return res[game]

#for game in ["A X", "B X", "C X", "A Y", "B Y", "C Y", "A Z", "B Z", "C Z"]: print(game, score2(game))

res2 = sum([score2(game) for game in games])
print(res2)

