import inputAoC as aoc
import my_utils
import re

foods = aoc.get_input_file(21, 2020).splitlines()

just_ingredients = []
all_ingredients = set()
all_allergenes = set()
allergenes = dict()

def constr_allergenes(foods):
    global all_ingredients
    global all_allergenes
    global allergenes
    global just_ingredients

    for food in foods:
        line = re.match(r"(.*) \(contains (.*)\)$", food)
        if line:
            groupes = line.groups()
            this_ingredients = groupes[0].split()
            this_allergenes = groupes[1].split(', ')
            all_ingredients |= set(this_ingredients)
            all_allergenes |= set(this_allergenes)
        else:
            this_ingredients = food.split()
            this_allergenes = []
        just_ingredients.extend(this_ingredients)

        for aller in this_allergenes:
            if aller in allergenes:
                allergenes[aller] &= set(this_ingredients)
            else:
                allergenes[aller] = set(this_ingredients)
    
    #my_utils.print_dict(allergenes)
    sudoku(allergenes)
    #my_utils.print_dict(allergenes)
    return allergenes

def sudoku(allergenes: dict):
    """permet de ne garder qu'un élement par key"""
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

def count_good(just_ingredients, allergenes):
    res = len(just_ingredients)
    for aller in allergenes.values():
        res -= just_ingredients.count(aller)
    return res

def canonical_dangerous(allergenes):
    allergenes_keys = sorted(allergenes.keys())
    ingredients = [allergenes[key] for key in allergenes_keys]
    return ",".join(ingredients)



constr_allergenes(foods)
#my_utils.print_dict(allergenes)
res1 = count_good(just_ingredients, allergenes)
print(res1)
res2 = canonical_dangerous(allergenes)
print(res2)