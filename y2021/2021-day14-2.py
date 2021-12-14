import inputAoC as aoc
from collections import defaultdict

input = aoc.get_input_file(14,2021)
deb, inserts = input.split('\n\n')

inserts = dict([insert.split(' -> ') for insert in inserts.splitlines()])

class Molecule:
    """
    :type couples: defaultdict(int)  
    :type l_debut,l_fin: '',''
    """
    def __init__(self, depart) -> None:
        """:param depart: string de la molécule initiale"""
        self.couples = defaultdict(int)
        if depart:
            self.l_debut,self.l_fin = depart[0],depart[-1]
        for i in range(len(depart)-1):
            voisin = depart[i:i+2]
            self.couples[voisin] += 1
    
    def step(self, inserts):
        res = Molecule('')
        res.l_debut,res.l_fin = self.l_debut,self.l_fin
        for couple in self.couples:
            if couple in inserts:
                # AB -> C   <==>
                # voisins += AC,CB
                A,B = couple
                C = inserts[couple]
                nb = self.couples[couple]
                res.couples[A+C] += nb
                res.couples[C+B] += nb
            else:
                res.couples[couple] += self.couples[couple]
        return res
    
    def n_steps(self, N, inserts):
        res = self
        for n in range(N):
            res = res.step(inserts)
        return res
    
    def score(self):
        occurrences = defaultdict(int)
        occurrences[self.l_debut] = occurrences[self.l_fin] = 1
        for couple in self.couples:
            A,B = couple
            nb = self.couples[couple]
            occurrences[A] += nb
            occurrences[B] += nb
        # on a tout compté en double
        return int((max(occurrences.values()) - min(occurrences.values()))/2)

molecule = Molecule(deb)

res1 = molecule.n_steps(10,inserts).score()
print(res1)
res2 = molecule.n_steps(40,inserts).score()
print(res2)