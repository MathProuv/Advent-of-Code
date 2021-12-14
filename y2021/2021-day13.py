import inputAoC as aoc

input = """6,10
0,14
9,10
0,3
10,4
4,11
6,0
6,12
4,1
0,13
10,12
3,4
3,0
8,4
1,10
2,14
8,10
9,0

fold along y=7
fold along x=5"""
input = aoc.get_input_file(13,2021)

def print_carte(carte):
    for lin in carte: print("".join(lin))

coords, folds = input.split('\n\n')
coords = [tuple(coord.split(',')) for coord in coords.splitlines()]
folds = folds.splitlines()
coords = list(map(lambda t:(int(t[0]),int(t[1])),coords))

def constr_carte_vide(X,Y):
    res = [''] * (Y)
    for lin in range(Y):
        res[lin] = [' '] * (X)
    return res

def constr_carte(coords):
    X,Y = max([coord[0] for coord in coords]), max([coord[1] for coord in coords])
    res = constr_carte_vide(X+1,Y+1)
    for coord in coords:
        res[coord[1]][coord[0]] = '#'
    return res

carte = constr_carte(coords)
#print_carte(carte)

def combine_carac(carac1,carac2):
    if carac1 == '#' or carac2 == '#': return '#'
    else: return ' '
def combine_lines(line1,line2):
    n = len(line1)
    assert(n==len(line2))
    res = ''
    for i in range(n):
        res += combine_carac(line1[i], line2[i])
    return res

def fold(carte, instr):
    axis, num =  instr[11], int(instr[13:])
    if axis == 'y':
        res = constr_carte_vide(len(carte[0]),num)
        for lin in range(num):
            res[lin] = combine_lines(carte[lin],carte[len(carte)-1-lin])
        return res
    elif axis == 'x':
        res = constr_carte_vide(num,len(carte))
        #je pourrais transposer, faire un fold sur y puis re transposer, mais mhin
        for col in range(num):
            for lin in range(len(carte)):
                res[lin][col] = combine_carac(carte[lin][col],carte[lin][len(carte[0])-1-col])
        return res
    else: print("problème d'axe")

def score(carte):
    res = 0
    for line in carte:
        for carac in line:
            if carac == '#': res += 1
    return res

after_fold1 = fold(carte,folds[0]) #fold along y=7
after_fold2 = fold(after_fold1,folds[1]) #fold along x=5
"""print_carte(after_fold1)
print()
print_carte(after_fold2)"""

res1 = score(after_fold1)
print(res1)

def n_folds(carte, folds):
    for instr in folds:
        carte = fold(carte,instr)
    print_carte(carte)

res2 = n_folds(carte,folds)