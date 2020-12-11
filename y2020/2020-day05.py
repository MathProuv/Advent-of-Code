import inputAoC as aoc

seats = aoc.get_input_file(5).split("\n")

ids = []
for seat in seats:
    id = int(seat.replace("B","1").replace("F","0").replace("R","1").replace("L","0"), 2)
    ids.append(id)

res1 = max(ids)
print(res1)

missing_ids = [i for i in range(min(ids),res1) if i not in ids]

if len(missing_ids) == 1:
    res2 = missing_ids[0]
else:
    for i in missing_ids:
        if i-1 in ids and i+1 in ids:
            res2 = i

print(res2)