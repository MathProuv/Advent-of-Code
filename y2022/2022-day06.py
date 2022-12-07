import inputAoC as aoc

input = """nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg"""
input = aoc.get_input_file(6,2022)

n = len(input)

def marker(input, n):
    for i in range(len(input)):
        if len(set(input[i:i+n])) == n: return i+n
    raise ModuleNotFoundError("no marker of size "+str(n)+" found")

res1, res2 = marker(input,4), marker(input,14)
print(res1,res2)