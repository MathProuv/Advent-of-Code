import inputAoC as aoc
import json

doc = aoc.get_input_file(12,2015)

res = 0
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
        res += temp
        temp = 0
    
print(res)

dict_doc = json.loads(doc)



