import inputAoC as aoc
from math import sqrt #, factorial
from itertools import permutations

pairs = [pair.split() for pair in aoc.get_input_file(9,2015).split("\n")]
n = int((1 + sqrt(1+8*len(pairs)))/2) 
#n = len(locations) car len(pairs) = k = n(n-1)/2

locations = [pairs[0][0]] + [pairs[i][2] for i in range(n-1)]
#print(locations)

distances = [0]*n
for i in range(n): distances[i] = [0]*n

for pair in pairs:
    depart, arrivee, distance = pair[0], pair[2], pair[4]
    i, j = locations.index(depart), locations.index(arrivee)
    distances[i][j] = distances[j][i] = int(distance)
#for line in distances: print(line)

# A partir d'ici, puisque n = 8, je peux me permettre de faire un code en n!
# Attention : ce n'est pas une bonne complexité, j'en suis consciente

perms = permutations(range(n))
dists = []
#for line in perms: print(line)
#print("len(perms) =", factorial(n))

for perm in perms:
    dist = 0
    depart = perm[0]
    for arrivee in perm[1:]:
        dist += distances[depart][arrivee]
        depart = arrivee
    dists.append(dist)

res1 = min(dists)
print(res1)

res2 = max(dists)
print(res2)