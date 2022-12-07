import inputAoC as aoc

input = """$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k"""
input = aoc.get_input_file(7,2022)
#input = "".join([line for line in open(0)])
input = input.split('\n$ ')[1:]

global_dirs = {}

class my_file:
    def __init__(self,size,name=None) -> None:
        self.name = name
        self.size = int(size)
    def get_size(self) -> int: return self.size
    def __repr__(self) -> str:
        return str(self.name) + " (size:"+str(self.size)+")"

class my_dir:
    def __init__(self,name,adress=None) -> None:
        if not adress: adress = name
        else: adress = adress+"/"+name
        self.adress = adress
        self.name = name
        self.files = []
        self.dirs = []
        global_dirs[adress] = self
    def add_file(self,f): self.files.append(f)
    def add_dir(self,d): self.dirs.append(d)
    def get_size(self) -> int:
        res = 0
        for f in self.files+self.dirs: res += f.get_size()
        return res
    def __repr__(self) -> str:
        res = self.name + "\nfiles: "
        for f in self.files: res += str(f) + ", "
        res += "\ndirs: "
        for d in self.dirs: res += "[" + str(d) + "]"
        return res

adress = "root"
root = my_dir(adress)

for instr in input:
    lines = instr.splitlines()
    if lines[0] == "ls":
        for line in lines[1:]:
            size,name = line.split(" ")
            if size == "dir": global_dirs[adress].add_dir(my_dir(name,adress))
            else:             global_dirs[adress].add_file(my_file(size,name))
    else: #cd
        new_adress = lines[0][3:]
        if new_adress == "..": adress = "/".join(adress.split("/")[:-1])
        else:                  adress += "/" + new_adress

size_root = global_dirs["root"].get_size()
size_objective = size_root - 40000000
res1, res2 = 0, size_root
for dir in global_dirs.values():
    size = dir.get_size()
    if size <= 100000: res1 += size
    if size > size_objective: res2 = min(res2,size)
print(res1,res2)