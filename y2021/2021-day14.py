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
    return max(res.values()) - min(res.values())
    m, M = '', ''
    m_val, M_val = len(deb),0
    print(res)
    for l in res:
        if m_val > res[l]: m = l
        if M_val < res[l]: M = l
        m_val,M_val = min(m_val,res[l]), max(M_val,res[l])
    print(m,m_val, M, M_val)
    return M_val - m_val

#deb10 = n_steps(10)
#res1 = score(deb10)
#print(res1)

#res2 = score(n_steps(40))
#print(res2)

class Molecule:
    occurrences = dict()
    couples = dict()
    l_debut,l_fin = '',''

    def __init__(self, depart) -> None:
        self.occurrences = dict()
        self.couples = dict()
        if depart:
            self.l_debut,self.l_fin = depart[0],depart[-1]
        for l in depart:
            if l in self.occurrences: self.occurrences[l] += 1
            else: self.occurrences[l] = 1
        for i in range(len(depart)-1):
            voisin = depart[i:i+2]
            if voisin in self.couples: self.couples[voisin] += 1
            else : self.couples[voisin] = 1
    
    def __str__(self) -> str:
        return str(self.occurrences) + '\n' + str(self.couples)
    
    def step(self, inserts):
        res = Molecule('')
        res.l_debut,res.l_fin = self.l_debut,self.l_fin

        for couple in self.couples:
            if couple in inserts:
                # AB -> C   <==>
                # voisins += AC,CB & occurences += C,A/2,B/2 
                # (A et B seront comptés 2 fois sauf si début et fin)
                A,B,C = couple, inserts[couple]
                nb = self.couples[couple]
                #print(A,B,C,nb)
                #res.occurrences[C] += nb
                if C in res.occurrences: res.occurrences[C] += nb
                else: res.occurrences[C] = nb
                #res.occurrences[B] += nb/2
                if B in res.occurrences: res.occurrences[B] += nb/2
                else: res.occurrences[B] = nb/2
                #res.occurrences[A] += nb/2
                if A in res.occurrences: res.occurrences[A] += nb/2
                else: res.occurrences[A] = nb/2
                #res.couples[A+C] += nb
                if A+C in res.couples: res.couples[A+C] += nb
                else: res.couples[A+C] = nb
                #res.couples[C+B] += nb
                if C+B in res.couples: res.couples[C+B] += nb
                else: res.couples[C+B] = nb
            else:
                if couple in res.couples: res.couples[couple] += self.couples[couple]
                else: res.couples[couple] = self.couples[couple]
        res.occurrences[self.l_debut] += 1/2
        res.occurrences[self.l_fin] += 1/2
        for l in res.occurrences: res.occurrences[l] = int(res.occurrences[l])
        return res
    
    def n_steps(self, N, inserts):
        res = self
        for n in range(N):
            res = res.step(inserts)
        return res
    
    def score(self):
        return max(self.occurrences.values()) - min(self.occurrences.values())

    
molecule = Molecule(deb)

"""print(molecule)
print(molecule.n_steps(1,inserts))
print(molecule.n_steps(2,inserts))
print(molecule)"""

res1 = molecule.n_steps(10,inserts).score()
print(res1)
res2 = molecule.n_steps(40,inserts).score()
print(res2)