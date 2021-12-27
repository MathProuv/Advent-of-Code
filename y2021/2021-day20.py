import inputAoC as aoc

input = """..#.#..#####.#.#.#.###.##.....###.##.#..###.####..#####..#....#..#..##..##
#..######.###...####..#..#####..##..#.#####...##.#.#..#.##..#.#......#.###
.######.###.####...#.##.##..#..#..#####.....#.#....###..#.##......#.....#.
.#..#..##..#...##.######.####.####.#.#...#.......#..#.#.#...####.##.#.....
.#..#...##.#.##..#...##.#.##..###.#......#.#.......#.#.#.####.###.##...#..
...####.#..#..#.##.#....##..#.####....##...##..#...#......#.#.......#.....
..##..####..#...#.#.#...##..#.#..###..#####........#..####......#..#

#..#.
#....
##..#
..#..
..###"""
input = aoc.get_input_file(20,2021)

enhancement_algorithm, image = input.split('\n\n')

enhancement_algorithm = enhancement_algorithm.replace('\n','')
image = image.splitlines()

assert(len(enhancement_algorithm) == 512)


def print_image(image:list):
    for line in image: print(line)
    print()

def extend_image(image:list,by_n_lines=2):
    m = len(image[0])
    for _ in range(by_n_lines):
        image.append('.'*m)
        image.insert(0,'.'*m)
    for i in range(len(image)):
        image[i] = '.'*by_n_lines + image[i] + '.'*by_n_lines
def restrict_image(image:list,by_n_lines=2):
    m = len(image[0])
    for _ in range(by_n_lines):
        image.pop()
        image.pop(0)
    for i in range(len(image)):
        image[i] = image[i][by_n_lines:-by_n_lines]

def neigh_to_index(neighbours:str):
    return int(neighbours.replace('.','0').replace('#','1'),2)

def get_neigh(image,i,j):
    res = ''
    for x in range(i-1,i+2):
        for y in range(j-1,j+2):
            if 0 <= x < len(image) and 0 <= y < len(image[0]):
                res += image[x][y]
            else:
                res+= '.'
    return res

def algo(image, enhancement):
    extend_image(image)
    new_image = image[:]
    n,m = len(image), len(image[0])
    for i in range(len(image)): new_image[i] = list(new_image[i])
    for i in range(n):
        for j in range(m):
            new_image[i][j] = enhancement[neigh_to_index(get_neigh(image,i,j))]
    for i in range(len(image)): new_image[i] = "".join(new_image[i])
    return new_image

extend_image(image,8)
#print_image(image)
image = algo(image,enhancement_algorithm)
#print_image(image)
image = algo(image,enhancement_algorithm)
restrict_image(image,8)
#print_image(image)

res1 = "".join(image).count('#')
print(res1)

def algo_n_times(image,enhancement,n):
    extend_image(image,3*n)
    for _ in range(n):
        image = algo(image,enhancement)
    restrict_image(image,3*n)
    return image

image = algo_n_times(image,enhancement_algorithm,48)
res2 = "".join(image).count('#')
print(res2)