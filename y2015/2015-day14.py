import inputAoC as aoc
import my_utils

class Reindeer:
    def __init__(self, name, speed, fly_time, rest_time):
        self.name = name
        self.speed = speed
        self.fly_time = fly_time
        self.rest_time = rest_time
    
    def distance(self, time):
        period = self.fly_time + self.rest_time
        nb_periods = time // period

        distance_1period = self.speed * self.fly_time
        duree_end = min(time%period, self.fly_time)
        distance_end = self.speed * duree_end

        return nb_periods * distance_1period + distance_end

    def print(self):
        print(self.name, self.speed, self.fly_time, self.rest_time)

reindeer_texte = aoc.get_input_file(14,2015).split("\n")

reindeers = []

# Vixen can fly 8 km/s for 8 seconds, but then must rest for 53 seconds.

for phrase in reindeer_texte:
    phrase = phrase.replace(" can fly "," ")
    phrase = phrase.replace(" km/s for ", " ")
    phrase = phrase.replace(" seconds, but then must rest for ", " ")
    phrase = phrase.replace(" seconds.", "")
    args = phrase.split()
    name, speed, fly_time, rest_time = args[0], int(args[1]), int(args[2]), int(args[3])
    reindeers.append(Reindeer(name, speed, fly_time, rest_time))

# for reindeer in reindeers: reindeer.print()
res1 = 0
for reindeer in reindeers:
    res1 = max(res1, reindeer.distance(2503))

print(res1)

n = len(reindeers)
points = [-1] * n
print(points)

for t in range(2503):
    dists = [reindeer.distance(t) for reindeer in reindeers]
    dist_lead = max(dists)
    for i in range(n):
        if dists[i] == dist_lead :
            points[i] += 1
    print(dists, points)

res2 = max(points)
print(res2)