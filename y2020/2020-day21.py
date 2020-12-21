import inputAoC as aoc
import my_utils
import re

foods = aoc.get_input_file(21, 2020).splitlines()

all_ingredients = []
all_allergenes = set()
allergenes = dict()

# construire les allergenes
for food in foods:
    line = re.match(r"(.*) \(contains (.*)\)$", food)
    if line:
        groupes = line.groups()
        this_ingredients = groupes[0].split()
        this_allergenes = groupes[1].split(', ')
        all_allergenes |= set(this_allergenes)
    else:
        this_ingredients = food.split()
        this_allergenes = []
    all_ingredients.extend(this_ingredients)

    for aller in this_allergenes:
        if aller in allergenes:
            allergenes[aller] &= set(this_ingredients)
        else:
            allergenes[aller] = set(this_ingredients)

# permettre de ne garder qu'un ingredient par allergene
repeat = True
while repeat:
    repeat = False
    keys = set()
    ingr_to_remove = set()
    for key, val in allergenes.items():
        if len(val) != 1:
            repeat = True
        else:
            ingr = val.pop()
            val.add(ingr)
            ingr_to_remove.add(ingr)
            keys.add(key)
    for key in allergenes.keys():
        if key not in keys:
            for ingr in ingr_to_remove:
                if ingr in allergenes[key]:
                    allergenes[key].remove(ingr)

for key in allergenes:
    assert type(allergenes[key]) == set
    assert len(allergenes[key]) == 1
    allergenes[key] = allergenes[key].pop()

#my_utils.print_dict(allergenes)

# compter les bons ingredients
res1 = len(all_ingredients)
for aller in allergenes.values():
    res1 -= all_ingredients.count(aller)
print(res1)



allergenes_keys = sorted(allergenes.keys())
ingredients = [allergenes[key] for key in allergenes_keys]
res2 = ",".join(ingredients)
print(res2)