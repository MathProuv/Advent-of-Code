import inputAoC as aoc

ex = """7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

22 13 17 11  0
 8  2 23  4 24
21  9 14 16  7
 6 10  3 18  5
 1 12 20 15 19

 3 15  0  2 22
 9 18 13 17  5
19  8  7 25 23
20 11 10 24  4
14 21 16 12  6

14 21 17 24  4
10 16 15  9 19
18  8 23 26 20
22 11 13  6  5
 2  0 12  3  7"""
input = ex
input = aoc.get_input_file(4,2021)
input = input.split('\n\n')

### Récolte et mise en forme des données

numbers = list(map(int,input[0].split(',')))
boards = input[1:]

for x in range(len(boards)):
    board = boards[x].split('\n')
    for i in range(len(board)):
        row = board[i].strip().replace("  ", " ").split(" ")
        board[i] = list(map(int,row))
    boards[x] = board
#print(numbers)
for board in boards:
    for row in board:
        print(row)
    print()

### Calcul du score

def score(board_win,nb_coups_win):
    marked_numbers = numbers[:nb_coups_win]
    somme_unmarked = 0
    for row in board_win:
        for nb in row:
            if nb not in marked_numbers: somme_unmarked += nb
    return somme_unmarked * marked_numbers[-1]

### Condition de victoire

def check_in(line, numbers): 
    """check si chaque nb de line est dans numbers"""
    for nb in line:
        if nb not in numbers: return False
    return True

def is_win(board, numbers):
    """check si la board gagne après le tirage des nb de numbers"""
    #check rows
    for i in range(len(board)):
        line = board[i]
        if check_in(line,numbers): return True
    #check cols
    for j in range(len(board[0])):
        line = []
        for i in range(len(board)):
            line.append(board[i][j])
        if check_in(line,numbers): return True
    return False

### Recherche 1ère gagnante et dernière gagnante

# tant qu'on n'a pas de victoire, on ajoute un nombre
i=0
victoire = False
while not(victoire):
    i += 1
    for board in boards:
        if is_win(board,numbers[:i]): #on commence à gagner
            board_win = board
            nb_coups_win = i
            victoire=True
#print(board_win,"gagne en",nb_coups_win,"coups")
res1 = score(board_win,nb_coups_win)
print(res1)

# tant qu'on a des victoires, on enlève un nombre
i=len(numbers)
victoire = True
while victoire:
    i -= 1
    for board in boards:
        if not(is_win(board,numbers[:i])): #on ne gagne plus
            board_lost = board #la derniere board gagnante
            nb_coups_lost = i+1 #le nb de coups pour gagner la dernière partie
            victoire=False
#print(board_lost,"gagne en",nb_coups_lost,"coups")
res2 = score(board_lost,nb_coups_lost)
print(res2)