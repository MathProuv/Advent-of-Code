import inputAoC as aoc

previous_password = aoc.get_input_file(11,2015)

def plusplus(letter):
    if letter == "z": 
        return "a"
    return chr(ord(letter)+1)
    
def increase(word):
    letters = [letter for letter in word]    
    last = letters.pop()
    comptZ = 0
    while letters and last == "z":
        comptZ += 1
        last = letters.pop()
    last = plusplus(last)
    letters.append(last)
    res = "".join(letters) + "a"*comptZ
    return res

def tests_increase():
    assert increase("xx") == "xy"
    assert increase("xz") == "ya"
    assert increase("xx") == "xy"
    assert increase("zz") == "aa"
    assert increase("abc") == "abd"
    assert increase("abzzz") == "acaaa"
#tests_increase()

def is_valid(password):
    if "i" in password or "j" in password or "l" in password:
        return False
    
    pair = int(password[1] == password[0])
    for i in range(2, len(password)):
        if password[i] == password[i-1] and password[i-2] != password[i]:
            pair += 1
    if pair < 2:
        return False
    
    ALPHABET = "abcdefghijklmnopqrstuvwxyz"
    suite = False
    for i in range(len(ALPHABET)-2):
        if ALPHABET[i:i+3] in password:
            suite = True
    if not suite:
        return False
        
    return True

def next_password(password):
    res = increase(password)
    while not is_valid(res):
        res = increase(res)
    return res

#print(previous_password)

res1 = next_password(previous_password)
print(res1)

res2 = next_password(res1)
print(res2)