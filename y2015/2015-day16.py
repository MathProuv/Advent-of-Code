import inputAoC as aoc
from json import loads
import my_utils

sues = aoc.get_input_file(16,2015)

# chaque ligne sera au format: 
#    Sue nn: "fieldA": a, "fieldB": b, "fieldC": c
sues = sues.replace('children', '"children"')
sues = sues.replace('cats', '"cats"')
sues = sues.replace('samoyeds', '"samoyeds"')
sues = sues.replace('pomeranians', '"pomeranians"')
sues = sues.replace('akitas', '"akitas"')
sues = sues.replace('vizslas', '"vizslas"')
sues = sues.replace('goldfish', '"goldfish"')
sues = sues.replace('trees', '"trees"')
sues = sues.replace('cars', '"cars"')
sues = sues.replace('perfumes', '"perfumes"').splitlines()


sues_dict = dict()

for sue in sues:
    index = sue.index(':')
    nb = int(sue[4:index]) #len('Sue ')
    sue_json = sue[index+2:] #len(': ')
    this_sue = loads("{" + sue_json + "}")
    sues_dict[nb] = this_sue


def is_good1(sue, good_sue) -> bool:
    for field, n in sue.items():
        if good_sue[field] != n:
            return False
    return True

def is_good2(sue, good_sue) -> bool:
    for field, n in sue.items():
        if field == "cats" or field == "trees": 
            if good_sue[field] >= n:
                return False
        elif field == "pomeranians" or field == "goldfish":
            if good_sue[field] <= n:
                return False
        elif good_sue[field] != n:
            return False
    return True

def find_sue(sues_dict: dict, good_sue: dict, is_good) -> int:
    """ Renvoit la première sue de sues_dict qui est valide
    
    :param sues_dict: dict(int: dict(field:int))
    :param good_sue: dict(field:int) 
    :param is_good: dict(field:int),dict(field:int) -> bool"""
    for nb, sue in sues_dict.items():
        if is_good(sue, good_sue):
            return nb
    

good_sue = dict(children=3, cats=7, samoyeds=2, pomeranians=3, akitas=0, \
    vizslas=0, goldfish=5, trees=3, cars=2, perfumes=1)

res1 = find_sue(sues_dict, good_sue, is_good1)
print(res1)

res2 = find_sue(sues_dict, good_sue, is_good2)
print(res2)