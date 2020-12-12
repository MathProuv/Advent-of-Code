import inputAoC as aoc

instrs = aoc.get_input_file(12,2020).split("\n")

class Ferry:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.angle = 90 #sens horaire
    
    def n(self, val): self.x += val
    
    def s(self, val): self.x -= val
    
    def e(self, val): self.y += val
    
    def w(self, val): self.y -= val
    
    def l(self, val):
        self.angle -= val
        self.angle %= 360
    
    def r(self, val):
        self.angle += val
        self.angle %= 360
    
    def f(self, val):
        if self.angle == 0: self.n(val)
        elif self.angle == 90: self.e(val)
        elif self.angle == 180: self.s(val)
        elif self.angle == 270: self.w(val)
    
    def distance(self):
        return abs(self.x) + abs(self.y)

    def simulation(self,instrs):
        fonctions = dict(N=self.n, S=self.s, E=self.e, W=self.w, L=self.l, R=self.r, F=self.f)
        for instr in instrs:
            fonction = fonctions[instr[0]]
            val = int(instr[1:])
            fonction(val)
            
    def get_pos(self):
        return (self.x, self.y, self.angle)

my_ferry = Ferry()
my_ferry.simulation(instrs)
res1 = my_ferry.distance()
print(res1)

class FerryWaypoint:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.dx = 10
        self.dy = 1
    
    def n(self, val): self.dy += val
    
    def s(self, val): self.n(-val)
    
    def e(self, val): self.dx += val
    
    def w(self, val): self.e(-val)

    def l90(self): self.dy, self.dx = self.dx, -self.dy
    def l(self, val): 
        for _ in range(90, val+90, 90): self.l90()
    
    def r90(self): self.dy, self.dx = -self.dx, self.dy
    def r(self, val):
        for _ in range(90, val+90, 90): self.r90()
    
    def f1(self): self.x, self.y = self.x+self.dx, self.y+self.dy
    def f(self, val):
        for _ in range(val): self.f1()
    
    def distance(self):
        return abs(self.x) + abs(self.y)

    def simulation(self,instrs):
        fonctions = dict(N=self.n, S=self.s, E=self.e, W=self.w, L=self.l, R=self.r, F=self.f)
        for instr in instrs:
            fonction = fonctions[instr[0]]
            val = int(instr[1:])
            fonction(val)

my_ferry_waypoint = FerryWaypoint()
my_ferry_waypoint.simulation(instrs)
res2 = my_ferry_waypoint.distance()
print(res2)