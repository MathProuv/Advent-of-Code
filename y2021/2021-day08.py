import inputAoC as aoc

input = """be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe
edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc
fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg
fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb
aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea
fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb
dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe
bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef
egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb
gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce"""
#input = "be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe"
input = aoc.get_input_file(8,2021)
entries = input.splitlines()

for i in range(len(entries)):
    entry = entries[i]
    patterns, values = entry.split(" | ")
    patterns = patterns.split(' ')
    values = values.split(' ')
    entries[i] = [patterns, values]

#print(entries)

def nb_of_1478(entries):
    nbs = [0] * 10
    for entry in entries:
        values = entry[1]
        for val in values:
            if len(val) == 2: nbs[1] += 1
            elif len(val) == 3: nbs[7] += 1
            elif len(val) == 4: nbs[4] += 1
            elif len(val) == 7: nbs[8] += 1
    return nbs[1] + nbs[4] + nbs[7] + nbs[8]

res1 = nb_of_1478(entries)
print(res1)


def alpha_sort(string): return "".join(sorted(string))


def get1(patterns):
    for nb in patterns:
        if len(nb) == 2: return alpha_sort(nb)
def get7(patterns):
    for nb in patterns:
        if len(nb) == 3: return alpha_sort(nb)
def get4(patterns):
    for nb in patterns:
        if len(nb) == 4: return alpha_sort(nb)
def get8(patterns):
    for nb in patterns:
        if len(nb) == 7: return alpha_sort(nb)
def get9(patterns):
    b,c,d,f = get4(patterns)
    for nb in patterns:
        if len(nb) == 6 and b in nb and c in nb and d in nb and f in nb: return alpha_sort(nb)
def get0(patterns):
    c,f = get1(patterns)
    n9 = get9(patterns)
    for nb in patterns:
        if len(nb) == 6 and c in nb and f in nb and alpha_sort(nb) != n9: return alpha_sort(nb)
def get6(patterns):
    n0 = get0(patterns)
    n9 = get9(patterns)
    for nb in patterns:
        nb = alpha_sort(nb)
        if len(nb) == 6 and nb != n0 and nb != n9: return alpha_sort(nb)
def get3(patterns):
    c,f = get1(patterns)
    for nb in patterns:
        if len(nb) == 5 and c in nb and f in nb: return alpha_sort(nb)
def get2(patterns):
    n6 = get6(patterns)
    n3 = get3(patterns)
    for nb in patterns:
        nb = alpha_sort(nb)
        if len(nb) == 5 and nb != n3: 
            diff = 0
            for l in n6: 
                if l not in nb: diff += 1
            if diff == 2: return alpha_sort(nb)
def get5(patterns):
    n6 = get6(patterns)
    n3 = get3(patterns)
    for nb in patterns:
        nb = alpha_sort(nb)
        if len(nb) == 5 and nb != n3: 
            diff = 0
            for l in n6: 
                if l not in nb: diff += 1
            if diff == 1: return alpha_sort(nb)

def get_numbers(p):
    return [get0(p),get1(p),get2(p),get3(p),get4(p),get5(p),get6(p),get7(p),get8(p),get9(p)]

def get_values(entry):
    patterns = entry[0]
    numbers = get_numbers(patterns)
    #print(numbers)
    res = 0
    for value in entry[1]:
        value = alpha_sort(value)
        #print(value)
        res *= 10
        res += numbers.index(value)
    return res


res2 = sum([get_values(entry) for entry in entries])
print(res2)