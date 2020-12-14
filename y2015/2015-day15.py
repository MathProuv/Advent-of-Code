import inputAoC as aoc
from math import prod

ex = """Butterscotch: capacity -1, durability -2, flavor 6, texture 3, calories 8
Cinnamon: capacity 2, durability 3, flavor -2, texture -1, calories 3"""

instrs = aoc.get_input_file(15,2015).split("\n")
instrs_ex = ex.split("\n")

class Ingredient:
    def __init__(self, instr: str):
        instr = instr.replace(": ",", ")
        props = [prop.split() for prop in instr.split(", ")]
        self.name = props[0][0]
        self.capacity = int(props[1][1])
        self.durability = int(props[2][1])
        self.flavor = int(props[3][1])
        self.texture = int(props[4][1])
        self.calories = int(props[5][1])

    def get_proprietes(self) -> [int]:
        proprietes = []
        proprietes.append(self.capacity)
        proprietes.append(self.durability)
        proprietes.append(self.flavor)
        proprietes.append(self.texture)
        proprietes.append(self.calories)
        return proprietes

    def print(self) -> str:
        string = self.name + ": "
        string += "capacity " + str(self.capacity) + ", "
        string += "durability " + str(self.durability) + ", "
        string += "flavor " + str(self.flavor) + ", "
        string += "texture " + str(self.texture) + ", "
        string += "calories " + str(self.calories)
        print(string)
        return string

class Cookie:
    def __init__(self, ingredients: [Ingredient], quantites:[int]):
        n = len(ingredients)
        if n != len(quantites):
            raise Exception("Il doit y avoir autant de quantités que d'ingredients")
        self.n = n
        self.ingredients = ingredients
        self.quantites = quantites
        proprietes = [0] * 5
        for i in range(self.n):
            ingredient = self.ingredients[i]
            quantite = self.quantites[i]
            prop = ingredient.get_proprietes()
            for i in range(5):
                proprietes[i] += quantite * prop[i]
        self.capacity = max(0, proprietes[0])
        self.durability = max(0, proprietes[1])
        self.flavor = max(0, proprietes[2])
        self.texture = max(0, proprietes[3])
        self.calories = max(0, proprietes[4])

    def print(self) -> str:
        string = ""
        for i in range(self.n):
            string += str(self.quantites[i]) + " "
            string += self.ingredients[i].name + " "
            string += str(self.ingredients[i].get_proprietes()) + "\n"
        print(string[:-1])
        print(self.get_proprietes(), self.score())
        print("\n")
        return string

    def score(self) -> int:
        proprietes = self.get_proprietes()
        proprietes.pop() # sans les calories
        return prod(proprietes)
    
    def get_proprietes(self) -> [int]:
        proprietes = []
        proprietes.append(self.capacity)
        proprietes.append(self.durability)
        proprietes.append(self.flavor)
        proprietes.append(self.texture)
        proprietes.append(self.calories)
        return proprietes


TOTAL = 100

ingredient_ex = [Ingredient(instr) for instr in instrs_ex]

res1_ex = 0
res2_ex = 0
best_qtt = [0,0]
best_qtt2 = [0,0]
for x1 in range(TOTAL+1):
    quantites = [x1, TOTAL-x1]
    cook = Cookie(ingredient_ex, quantites)
    # cook.print()
    if cook.score() >= res1_ex:
        best_qtt = quantites
        res1_ex = cook.score()
    if cook.calories == 500:
        if cook.score() >= res1_ex:
            best_qtt2 = quantites
            res2_ex = cook.score()

print(res1_ex, best_qtt)
print(res2_ex, best_qtt2)


ingredients = [Ingredient(instr) for instr in instrs]

res1 = 0
res2 = 0
qtt = []
for x1 in range(1,TOTAL+1): 
    #start=1 car on sait qu'il y a des Sprinkles pour une capacité != 0
    SOUS_TOTAL = TOTAL - x1
    for x2 in range(TOTAL+1):
        SOUS_SOUS_TOTAL = SOUS_TOTAL - x2
        if SOUS_SOUS_TOTAL < 0:
            continue
        for x3 in range(TOTAL+1):
            x4 = SOUS_SOUS_TOTAL - x3
            if x4 < 0:
                continue
            quantites = [x1,x2,x3,x4]
            cook = Cookie(ingredients, quantites)
            score = cook.score()
            res1 = max(res1, score)
            if cook.calories == 500:
                res2 = max(res2, score)

print(res1)
print(res2)