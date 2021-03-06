import inputAoC as aoc

rules = aoc.get_input_file(7,2020).split("\n")
n = len(rules)

bags = []
contains = []

for rule in rules:
    index_bag = rule.index(" bags ")
    bag = rule[:index_bag]
    bags.append(bag)
    index_contain = index_bag + len(" bags contain ")
    contain = rule[index_contain:].replace(" bag, ", "\n").replace(" bags, ","\n").replace(" bag.","").replace(" bags.","").split("\n")
    if contain[0] == "no other":
        contain = []
    else:
        for i in range(len(contain)):
            elem = contain[i]
            index_fin_nb = elem.index(" ")
            contain[i] = (int(elem[:index_fin_nb]), elem[index_fin_nb+1:])
    contains.append(contain)

def see_is_in_bag(to_see,seen):
    """Fonction récursive pour compter combien de sacs peuvent contenir to_see"""
    seen_here = set()
    if not to_see:
        return len(seen)
    for bag in bags:
        containing = contains[bags.index(bag)]
        for n,b in containing:
            if b in to_see:
                seen_here.add(bag)
    seen |= seen_here
    to_see = list(seen_here)
    return see_is_in_bag(to_see, seen)

res1 = see_is_in_bag(["shiny gold"], set())
print(res1)

def see_in_bag(bag):
    """Fonction récursive pour compter combien de sacs contient bag"""
    if not bag:
        return 0
    res = 0
    containing = contains[bags.index(bag)]
    for n,b in containing:
        res += n + n * see_in_bag(b)
    return res

res2 = see_in_bag("shiny gold")
print(res2)

""" #matrice d'adjacence
matrice = [0]*n
for i in range(n):
    matrice[i] = [0]*n

for i in range(n):
    bag = bags[i]
    for n,b in contains[i]:
        j = bags.index(b)
        matrice[i][j] = n
"""
