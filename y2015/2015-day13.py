import inputAoC as aoc
import my_utils
from itertools import permutations
from math import sqrt

# feeling = "Alice would gain 54 happiness units by sitting next to Bob."
texte = """Alice would gain 54 happiness units by sitting next to Bob.
Alice would lose 79 happiness units by sitting next to Carol.
Alice would lose 2 happiness units by sitting next to David.
Bob would gain 83 happiness units by sitting next to Alice.
Bob would lose 7 happiness units by sitting next to Carol.
Bob would lose 63 happiness units by sitting next to David.
Carol would lose 62 happiness units by sitting next to Alice.
Carol would gain 60 happiness units by sitting next to Bob.
Carol would gain 55 happiness units by sitting next to David.
David would gain 46 happiness units by sitting next to Alice.
David would lose 7 happiness units by sitting next to Bob.
David would gain 41 happiness units by sitting next to Carol."""

texte = aoc.get_input_file(13,2015)

texte = texte.replace(" would "," ").replace(".","")
texte = texte.replace(" gain ", " +").replace(" lose ", " -")
texte = texte.replace(" happiness units by sitting next to ", " ")
texte_split = [word.split(" ") for word in texte.split("\n")]

# my_utils.print_matrice(feelings)

n = int(sqrt(len(texte_split))) + 1
# len(texte_split) = k = (n-1)²

guests = [texte_split[0][0]] + [texte_split[i][-1] for i in range(n-1)]
# print(n, guests)

graph_feelings = [0]*n
for i in range(n):
    graph_feelings[i] = [0]*n

for feel in texte_split:
    guestI, feeling, guestJ = feel
    i, j = guests.index(guestI), guests.index(guestJ)
    graph_feelings[i][j] = int(feeling)
my_utils.print_matrice(graph_feelings)

graph_feelings_with_me = [0]*(n+1)
for i in range(n+1):
    if i == n:
        graph_feelings_with_me[i] = [0]*(n+1)
    else:
        graph_feelings_with_me[i] = graph_feelings[i] + [0]
my_utils.print_matrice(graph_feelings_with_me)


def max_happiness(graph_feelings):
    n = len(graph_feelings)
    perms = [[0] + list(perm) for perm in permutations(range(1,n))]
    happinesses = []
    for perm in perms:
        happiness = graph_feelings[perm[-1]][0] + graph_feelings[0][perm[-1]]
        guest1 = 0 #perm[0]
        for guest2 in perm:
            happiness += graph_feelings[guest1][guest2] + graph_feelings[guest2][guest1]
            guest1 = guest2
        happinesses.append(happiness)
    #print(happinesses)
    return max(happinesses)

res1 = max_happiness(graph_feelings)
print(res1)
res2 = max_happiness(graph_feelings_with_me)
print(res2)