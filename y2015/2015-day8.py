import inputAoC as aoc

strings = aoc.get_input_file(8,2015).split("\n")

res1 = 0
for string in strings:
    i = 1
    decoded = []
    while i < len(string)-1:
        letter = string[i]
        if letter == "\\":
            i += 1
            letter += string[i]
            if letter == "\\x":
                letter += string[i+1:i+3]
                i += 2
        decoded.append(letter)
        i += 1
    #print(string, decoded)
    res1 += len(string) - len(decoded)
print(res1)

res2 = 0
for string in strings:
    encoded = ""
    for letter in string:
        if letter == "\"" or letter == "\\":
            letter = "\\" + letter
        encoded += letter
    encoded = "\"" +encoded+ "\""
    #print(string, encoded)
    res2 += len(encoded) - len(string)
print(res2)

### Méthode 2 :
""" # 1 boucle, 1 passage par mot
res1, res2 = 0,0
for string in strings:
    decoded = []
    encoded = "\"\\\""
    i = 1
    while i < len(string)-1:
        d_letter = string[i]
        e_letter = string[i]
        if d_letter == "\\":
            i += 1
            d_letter += string[i]
            if d_letter == "\\x":
                d_letter += string[i+1:i+3]
                i += 2
                e_letter = "\\" + d_letter
            else:
                e_letter = "\\\\" + d_letter
        decoded.append(d_letter)
        encoded += e_letter
        i += 1
    encoded += "\\\"\""
    #print(string, encoded, decoded)
    res1 += len(string) - len(decoded)
    res2 += len(encoded) - len(string)

print(res1)
print(res2)
"""

### Méthode 3
""" # 1 boucle
res1, res2 = int(), int()
for string in strings:
    encoded = ""
    i = 1
    decoded = []
    while i < len(string)-1:
        letter = string[i]
        if letter == "\\":
            i += 1
            letter += string[i]
            if letter == "\\x":
                letter += string[i+1:i+3]
                i += 2
        decoded.append(letter)
        i += 1
    for letter in string:
        if letter == "\"" or letter == "\\":
            letter = "\\" + letter
        encoded += letter
    encoded = "\"" +encoded+ "\""
    #print(string, encoded, decoded)
    res1 += len(string) - len(decoded)
    res2 += len(encoded) - len(string)
print(res1)
print(res2)
"""