import inputAoC as aoc

strings = aoc.get_input_file(8,2015).split("\n")

res1 = int()
for encoded in strings:
    decoded = ""
    i = 1
    decoded = []
    while i < len(encoded)-1:
        letter = encoded[i]
        if letter == "\\":
            i += 1
            letter += encoded[i]
            if letter == "\\x":
                letter += encoded[i+1:i+3]
                i += 2
        decoded.append(letter)
        i += 1
    #print(encoded, decoded)
    res1 += len(encoded) - len(decoded)
print(res1)

res2 = 0
for decoded in strings:
    encoded = ""
    for letter in decoded:
        if letter == "\"" or letter == "\\":
            letter = "\\" + letter
        encoded += letter
    encoded = "\"" +encoded+ "\""
    #print(decoded, encoded)
    res2 += len(encoded) - len(decoded)
print(res2)