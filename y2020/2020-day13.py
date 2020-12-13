import inputAoC as aoc

ex = """939
7,13,x,x,59,x,31,19"""

timestamp, all_buses = ex.split('\n')
timestamp, all_buses = aoc.get_input_file(13,2020).split('\n')

timestamp = int(timestamp)
buses = [int(bus) for bus in all_buses.replace(",x","").split(",")]
buses_index = [all_buses.split(",").index(str(bus)) for bus in buses]

print(all_buses)
print(buses)
print(buses_index)

min_attente = float("inf")
bus_attente = 0

for bus in buses:
    attente = bus - timestamp % bus
    if attente < min_attente:
        bus_attente = bus
        min_attente = attente

res1 = min_attente * bus_attente
print(res1)

res2 = 210612924879242
# voir 2020-day13-restes_chinois.txt
print(res2)