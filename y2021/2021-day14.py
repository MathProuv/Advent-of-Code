import inputAoC as aoc

input = """NNCB

CH -> B
HH -> N
CB -> H
NH -> C
HB -> C
HC -> B
HN -> C
NN -> C
BH -> H
NC -> B
NB -> B
BN -> B
BB -> N
BC -> B
CC -> N
CN -> C"""
input = aoc.get_input_file(14,2021)
deb, inserts = input.split('\n\n')

inserts = dict([insert.split(' -> ') for insert in inserts.splitlines()])

def step(deb, inserts=inserts):
    res = deb[0]
    for i in range(len(deb)-1):
        if deb[i:i+2] in inserts:
            res += inserts[deb[i:i+2]]
        res += deb[i+1]
    return res
def n_steps(N, deb=deb, inserts=inserts):
    for n in range(N):
        print(n, deb[:min(100,len(deb))])
        deb = step(deb,inserts)
        score(deb)
        print()
    #print(n+1,len(deb))
    return deb

def score(deb):
    res = dict()
    for l in deb:
        if l in res: res[l] += 1
        else: res[l] = 1
    m, M = '', ''
    m_val, M_val = len(deb),0
    print(res)
    for l in res:
        if m_val > res[l]: m = l
        if M_val < res[l]: M = l
        m_val,M_val = min(m_val,res[l]), max(M_val,res[l])
    print(m,m_val, M, M_val)
    return M_val - m_val

deb10 = n_steps(10)
res1 = score(deb10)
#print(res1)

res2 = score(n_steps(40))
#print(res2)