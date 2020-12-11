import inputAoC as aoc
import json

doc = aoc.get_input_file(12,2015)

res1 = 0
temp = 0

for carac in doc:
    if carac == '-':
        temp = float("-inf")
    elif carac.isdigit():
        if temp >= 0:
            temp = 10*temp + int(carac)
        elif temp == float("-inf"):
            temp = - int(carac)
        else:
            temp = 10*temp - int(carac)
    else:
        res1 += temp
        temp = 0
    
print(res1)

def somme_nombres(obj):
    if type(obj) == int:
        return obj
    elif type(obj) == dict and "red" not in obj.values(): #:
        return sum([somme_nombres(val) for val in obj.values()])
    elif type(obj) == list:
        return sum([somme_nombres(val) for val in obj])
    else:
        return 0

res2 = somme_nombres(json.loads(doc))
print(res2)


