import inputAoC as aoc

ex = """L.LL.LL.LL
LLLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLLL
L.LLLLLL.L
L.LLLLL.LL"""

def print_matrice(matrice):
    for line in matrice:
        print(line)
    print()
    
def nb_voisins1(matrice,i,j):
    res = -(matrice[i][j] == "#")
    for I in range(i-1,i+2):
        for J in range(j-1,j+2):
            if 0 <= I < len(matrice) and 0 <= J < len(matrice[I]):
                res += matrice[I][J] == "#"
    return res

def nb_voisins2(matrice,i,j):
    res = 0
    def see_occupied_direction(direction):
        di,dj = direction
        I, J = i + di, j + dj
        while 0 <= I < len(matrice) and 0 <= J < len(matrice[I]):
            case = matrice[I][J]
            if case != ".":
                return case == "#"
            else:
                I, J = I + di, J + dj
        return False
    directions = [(1,1),(1,0),(1,-1),(0,1),(0,-1),(-1,1),(-1,0),(-1,-1)]
    for direction in directions:
        res += see_occupied_direction(direction)
    return res


def matr_voisins(matrice, fct_voisins):
    res = [0]*len(matrice)
    for i in range(len(matrice)):
        res[i] = [0]*len(range(len(matrice[i])))
        for j in range(len(matrice[i])):
            res[i][j] = fct_voisins(matrice,i,j)
    return res

def round(layout, tour):
    fct_voisins = [nb_voisins1, nb_voisins2]
    nb_to_empty = [4,5]
    voisins = matr_voisins(layout,fct_voisins[tour-1])
    change = False
    for i in range(len(layout)):
        for j in range(len(layout[i])):
            case = layout[i][j]
            if case == "L" and voisins[i][j] == 0:
                layout[i][j] = "#"
                change = True
            elif case == "#" and voisins[i][j] >= nb_to_empty[tour-1]:
                layout[i][j] = "L"
                change = True
    return change

def simulate(layout, tour):
    while round(layout, tour):
        #print_matrice(layout)
        pass

def count_occupied(layout):
    return sum([line.count("#") for line in layout])


#layout = [list(line) for line in ex.split("\n")]
layout = [list(line) for line in aoc.get_input_file(11,2020).split("\n")]
simulate(layout, 1)
res1 = count_occupied(layout)
print(res1)

#layout = [list(line) for line in ex.split("\n")]
layout = [list(line) for line in aoc.get_input_file(11,2020).split("\n")]
simulate(layout, 2)
res2 = count_occupied(layout)
print(res2)