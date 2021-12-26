import inputAoC as aoc

def isnumber(string):
    for c in string:
        if not('0' <= c <= '9'): return False
    return True

input1 = "[[[[4,3],4],4],[7,[[8,4],9]]]\n[1,1]"
input2 = """[1,1]
[2,2]
[3,3]
[4,4]"""
input3 = """[1,1]
[2,2]
[3,3]
[4,4]
[5,5]"""
input4 = """[1,1]
[2,2]
[3,3]
[4,4]
[5,5]
[6,6]"""
input5 = """[[[0,[4,5]],[0,0]],[[[4,5],[2,6]],[9,5]]]
[7,[[[3,7],[4,3]],[[6,3],[8,8]]]]
[[2,[[0,8],[3,4]]],[[[6,7],1],[7,[1,6]]]]
[[[[2,4],7],[6,[0,5]]],[[[6,8],[2,8]],[[2,1],[4,5]]]]
[7,[5,[[3,8],[1,4]]]]
[[2,[2,2]],[8,[8,1]]]
[2,9]
[1,[[[9,3],9],[[9,0],[0,7]]]]
[[[5,[7,4]],7],1]
[[[[4,2],2],6],[8,7]]"""
input6 = """[[[0,[5,8]],[[1,7],[9,6]]],[[4,[1,2]],[[1,4],2]]]
[[[5,[2,8]],4],[5,[[9,9],0]]]
[6,[[[6,2],[5,6]],[[7,6],[4,7]]]]
[[[6,[0,7]],[0,9]],[4,[9,[9,0]]]]
[[[7,[6,4]],[3,[1,3]]],[[[5,5],1],9]]
[[6,[[7,3],[3,2]]],[[[3,8],[5,7]],4]]
[[[[5,4],[7,7]],8],[[8,3],8]]
[[9,3],[[9,9],[6,[4,9]]]]
[[2,[[7,7],7]],[[5,8],[[9,3],[0,2]]]]
[[[[5,2],5],[8,[3,7]]],[[5,[7,5]],[4,4]]]"""
input = aoc.get_input_file(18,2021)


def decompose(number_str):
    if isnumber(number_str): return int(number_str)
    indexes = []
    rang = 0
    for i in range(len(number_str)):
        c = number_str[i]
        if c == '[': rang += 1
        elif c == ']': rang -= 1
        if rang == 1: #on cherche la virgule séparatrice des 2 parties du nombre
            indexes.append(i)
    #indexes = indexes[1:-1] #On peut enlever les crochets du début et de la fin
    for i in indexes:
        if number_str[i] == ',': idx = i
    n1,n2 = number_str[1:idx],number_str[idx+1:-1]
    return (decompose(n1),decompose(n2))  # () or []
def recompose(number_ints):
    return str(number_ints).replace('(','[').replace(')',']').replace(' ','')
assert(recompose(decompose("[[[[[9,8],1],2],3],4]")) == "[[[[[9,8],1],2],3],4]")

def sum_numbers(number1,number2):
    number_str = '[' + number1 + ',' + number2 + ']'
    #reduce_number(number_str):
    change = True
    while change:
        #print(number_str)
        exploded = explode(number_str)
        if exploded != number_str: number_str = exploded
        else:
            splited = split(number_str)
            if splited != number_str: number_str = splited
            else: change = False
    #print()
    return number_str

def explode(number_str):
    nb = 0
    idx_deb = -1 #index of 5th [ (nested)
    for i in range(len(number_str)):
        c = number_str[i]
        if c == '[': nb += 1
        elif c == ']': nb -= 1
        if nb == 5:
            idx_deb = i
            break
    if idx_deb == -1: return number_str

    to_explode = ""
    idx_fin = idx_deb #index of ]
    while number_str[idx_fin] != ']':
        to_explode += number_str[idx_fin]
        idx_fin += 1
    to_explode += number_str[idx_fin] #]
    replace_that = list(map(int,to_explode[1:-1].split(',')))

    # increase the most right number    
    idx_right_deb = idx_fin + 1
    while idx_right_deb < len(number_str)-1 and not isnumber(number_str[idx_right_deb]):
        idx_right_deb += 1
    if idx_right_deb < len(number_str)-1:
        idx_right_fin = idx_right_deb + 1
        while isnumber(number_str[idx_right_fin]):
            idx_right_fin += 1
        replace_with_right = int(number_str[idx_right_deb:idx_right_fin])
        number_str = number_str[:idx_right_deb] + str(replace_with_right + replace_that[1]) + number_str[idx_right_fin:]

    # replace the exploding pair with 0
    number_str = number_str[:idx_deb] + '0' + number_str[idx_fin+1:]

    # increase the most left number 
    idx_left_fin = idx_deb - 1
    while idx_left_fin > 0 and not isnumber(number_str[idx_left_fin]):
        idx_left_fin -= 1
    if idx_left_fin > 0:
        idx_left_deb = idx_left_fin - 1
        while isnumber(number_str[idx_left_deb]):
            idx_left_deb -= 1
        replace_with_left = int(number_str[idx_left_deb+1:idx_left_fin+1])
        number_str = number_str[:idx_left_deb+1] + str(replace_with_left + replace_that[0]) + number_str[idx_left_fin+1:]
    return number_str

assert (explode("[7,[6,[5,[4,[3,2]]]]]") == "[7,[6,[5,[7,0]]]]")
assert (explode("[[[[[9,8],1],2],3],4]") == "[[[[0,9],2],3],4]")
assert (explode("[[6,[5,[4,[3,2]]]],1]") == "[[6,[5,[7,0]]],3]")
assert (explode("[[3,[2,[1,[7,3]]]],[6,[5,[4,[3,2]]]]]") == "[[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]]")
assert (explode("[[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]]") == "[[3,[2,[8,0]]],[9,[5,[7,0]]]]")

def split(number_str):
    for i in range(len(number_str)-1):
        if isnumber(number_str[i:i+2]):
            to_split = number_str[i:i+2]
            to_split_int = int(to_split)
            first = to_split_int//2
            second = (to_split_int+1)//2
            replace_with = '[' + str(first) + ',' + str(second) + ']'
            return number_str[:i] + replace_with + number_str[i+2:]
    return number_str


def magnitude_rec(number_ints):
    if isinstance(number_ints,int): return number_ints
    n1,n2 = number_ints
    return 3*magnitude_rec(n1) + 2*magnitude_rec(n2)

def magnitude(number_str):
    number_str = decompose(number_str)
    return magnitude_rec(number_str)

assert magnitude("[[9,1],[1,9]]") == 129
assert magnitude("[[[[5,0],[7,4]],[5,5]],[6,6]]") == 1137
assert magnitude("[[[[8,7],[7,7]],[[8,6],[7,7]]],[[[0,7],[6,6]],[8,7]]]") == 3488

def sum_input(input):
    numbers = input.splitlines()
    acc = numbers[0]
    for number in numbers[1:]:
        acc = sum_numbers(acc,number)
    return acc

assert(sum_input(input1) == "[[[[0,7],4],[[7,8],[6,0]]],[8,1]]")
assert(sum_input(input2) == "[[[[1,1],[2,2]],[3,3]],[4,4]]")
assert(sum_input(input3) == "[[[[3,0],[5,3]],[4,4]],[5,5]]")
assert(sum_input(input4) == "[[[[5,0],[7,4]],[5,5]],[6,6]]")
assert(sum_input(input5) == "[[[[8,7],[7,7]],[[8,6],[7,7]]],[[[0,7],[6,6]],[8,7]]]")

total_sum = sum_input(input)
res1 = magnitude(total_sum)
print(res1)
#print(total_sum)

def max_magnitudes(input):
    numbers = input.splitlines()
    n = len(numbers)
    assert len(set(numbers)) == n
    maxi = 0
    for number1 in numbers:
        for number2 in numbers:
            if number1 != number2:
                current_magnitude = magnitude(sum_numbers(number1,number2))
                maxi = max(maxi,current_magnitude)
    return maxi

assert (max_magnitudes(input6) == 3993)

res2 = max_magnitudes(input)
print(res2)
