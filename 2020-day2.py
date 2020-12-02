import inputAoC

x = inputAoC.get_input(2).split("\n")

res = 0

for instr in x:
    restriction, letter, password = tuple(instr.replace(":","").split())
    a,b = list(map(int, restriction.split("-")))
    if password.count(letter) in range(a,b+1):
        res += 1

print(res)

res = 0

for instr in x:
    restriction, letter, password = tuple(instr.replace(":","").split())
    a,b = list(map(int, restriction.split("-")))
    level = (password[a-1] == letter) + (password[b-1] == letter)
    if level == 1:
        res += 1

print(res)