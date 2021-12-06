import inputAoC as aoc

input = """3,4,3,1,2"""
input = aoc.get_input_file(6,2021)
input = list(map(int,input.split(',')))

#print(input)

def nb_poissons(input0,days):
    timers = [0]*9 #[0 for _ in range(0,9)]
    for time in input0:
        timers[time] += 1
    for day in range(days):
        t0 = timers.pop(0)
        timers.append(t0)
        timers[6] += t0
    return sum(timers)

res1 = nb_poissons(input,80)
res2 = nb_poissons(input,256)
print(res1, res2)