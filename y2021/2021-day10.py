import inputAoC as aoc

input = """[({(<(())[]>[[{[]{<()<>>
[(()[<>])]({[<{<<[]>>(
{([(<{}[<>[]}>{[]{[(<()>
(((({<>}<{<{<>}{[]{[]{}
[[<[([]))<([[{}[[()]]]
[{[{({}]{}}([{[{{{}}([]
{<[[]]>}<{[{[{[]{()[[[]
[<(<(<(<{}))><([]([]()
<{([([[(<>()){}]>(<<{{
<{([{{}}[<[[[<>{}]]]>[]]"""
input = aoc.get_input_file(10,2021)
input = input.splitlines()

#print(input)
def print_list(list):
    for line in list: print(line)

def remove_empty(line):
    while '<>' in line or '{}' in line or '[]' in line or '()' in line:
        line = line.replace('<>','').replace('{}','').replace('[]','').replace('()','')
    return line

def score_corrupted(line):
    line = remove_empty(line)
    idx = len(line)
    for i in range(len(line)-1,-1,-1):
        if line[i] in '>}])': idx = i
    if idx == len(line): return 0
    dict_scores = {'>':25137, '}':1197, ']':57, ')':3}
    return dict_scores[line[idx]]

def scores_corrupted(input):
    scores = [score_corrupted(line) for line in input]
    return sum(scores)

res1 = scores_corrupted(input)
print(res1)

def score_incomplete(line):
    if score_corrupted(line): return 0
    line = list(remove_empty(line))
    dict_scores = {'<':'4', '{':'3', '[':'2', '(':'1'}
    res = int("".join([dict_scores[carac] for carac in line[::-1]]),5)
    return res
    res = 0
    dict_scores = {'<':4, '{':3, '[':2, '(':1}
    for carac in line[::-1]:
        res *= 5
        res += dict_scores[carac]
        #res = 5*res + dict_scores[carac]
    return res

def scores_incomplete(input):
    scores = [score_incomplete(line) for line in input]
    scores = sorted(scores)[::-1]
    if 0 in scores:
        scores = scores[:scores.index(0)]
    #scores = scores[::-1] #remettre dans l'ordre n'est pas nécessaire
    return scores[len(scores)//2]
    scores = []
    for line in input:
        score = score_incomplete(line)
        if score: scores.append(score)
    scores = sorted(scores)[::-1]
    return scores[len(scores)//2]

res2 = scores_incomplete(input)
print(res2)
