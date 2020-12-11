import inputAoC

x = inputAoC.get_input(2).split("\n")

res = 0
for instr in x:
    restr, letter, password = instr.replace(":","").split()
    a,b = [int(i) for i in restr.split("-")]
    res += (a <= password.count(letter) <= b)
print(res)

res = 0
for instr in x:
    restr, letter, password = instr.replace(":","").split()
    a,b = [int(i) for i in restr.split("-")]
    res += 1 == (password[a-1] == letter) + (password[b-1] == letter)
print(res)