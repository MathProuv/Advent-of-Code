import inputAoC

input = inputAoC.get_input_file(3).split("\n")
height,width = len(input),len(input[0])

res = 0

for i in range(height):
    res += input[i][(3*i)%width] == "#"

print(res)

ratios = ((1,1), (1,5), (1,7), (2,1))
#res = res # res(ratio=(1,3))

for ratio in ratios:
    res_ratio = 0
    for lig in range(0, height, ratio[0]):
        col = lig // ratio[0]
        res_ratio += input[lig][(ratio[1]*col)%width] == "#"
    #print(res_ratio)
    res *= res_ratio

print(res)