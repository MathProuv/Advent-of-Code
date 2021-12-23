import inputAoC as aoc
from math import sqrt

input = "target area: x=20..30, y=-10..-5"
input = aoc.get_input_file(17,2021)
#target area: x=155..215, y=-132..-72

def get_target(input):
    #re.format("target area: x={x1}..{x2}, y={y1}..{y2}") #??
    xs, ys = input[len('target area: x='):].split(', y=')
    xs = sorted(map(int, xs.split('..')))
    ys = sorted(map(int, ys.split('..')))
    return xs,ys

target = get_target(input)
print(target)

def is_in_target(x,y, target):
    xs, ys = target
    return xs[0] <= x <= xs[1] and ys[0] <= y <= ys[1]

def launch(vx,vy,target):
    """returns a boolean indicating if it has reached"""
    assert(not is_in_target(0,0,target)) #else not borned
    x,y = 0,0
    trajectory = [(x,y)]
    while y >= target[1][0] and not is_in_target(x,y,target):
        x += vx
        y += vy
        vx -= 1 if vx > 0 else -1 if vx < 0 else 0
        vy -= 1
        #trajectory.append((x,y))
    #print(trajectory)
    return is_in_target(x,y, target)


#print(launch(6,9, target))
#print(launch(29,-6, target))

My = target[1][0]
res1 = My*(My+1)//2
print(res1)

def test_interval(target):
    mx = 0
    Mx = target[0][1]
    my = target[1][0]
    My = -my
    compt = 0
    for vx in range(mx,Mx+1):
        for vy in range(my,My+1):
            if launch(vx,vy,target):
                #print(vx,vy)
                compt += 1
    return compt

res2 = test_interval(target)
print(res2)