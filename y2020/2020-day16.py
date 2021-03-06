import inputAoC as aoc
import re
import my_utils

def constr_fields(instrs: str) -> dict:
    fields = dict()

    for field in instrs:
        m = re.match(r"([a-z ]+): (\d+)-(\d+) or (\d+)-(\d+)", field)
        f, a1, b1, a2, b2 = m.groups()
        fields[f] = [(int(a1),int(b1)), (int(a2),int(b2))]

    #my_utils.print_dict(fields)
    return fields

def fields_ranges(fields: dict) -> [tuple]:
    ranges = []
    for v_field in fields.values():
        ranges.extend(v_field)
    return ranges

def ticket_score(ticket: [int], fields: dict) -> int:
    ranges = fields_ranges(fields)
    score = 0
    for nb in ticket:
        for rang in ranges:
            if rang[0] <= nb <= rang[1]:
                nb = 0
        score += nb
    return score

def get_valid_tickets(tickets: [[int]], fields: dict) -> [[int]]:
    res = []
    for ticket in tickets:
        if not ticket_score(ticket, fields):
            res.append(ticket)
    return res

def scan_rate(tickets: [[int]], fields: dict) -> int:
    rate = 0
    for ticket in tickets:
        rate += ticket_score(ticket, fields)
    return rate


def get_real_fields(valid_tickets: [[int]], fields: dict) -> [str]:
    ## get_possible_fields
    possible = []
    for col in range(len(good_tickets[0])):
        values = [line[col] for line in good_tickets]
        possibs = set(fields.keys())
        for val in values:
            posses = set()
            for poss in possibs:
                ranges = fields[poss]
                if ranges[0][0] <= val <= ranges[0][1] or ranges[1][0] <= val <= ranges[1][1]:
                    posses.add(poss)
            possibs &= posses
            if len(possibs) <= 1:
                break
        possible.append(possibs)
    possible = list(enumerate(possible))
    # my_utils.print_matrice(possible)

    ## get_real_fields
    res = [str()] * len(possible)
    repeat = True
    while repeat:
        repeat = False
        for possibility in possible:
            if len(possibility[1]) == 1:
                poss_index = possibility[0]
                real_poss = possibility[1].pop()
                res[poss_index] = real_poss
                for _, thing in possible:
                    if real_poss in thing:
                        thing.remove(real_poss)
                repeat = True
    return res


groups_instrs = aoc.get_input_file(16,2020).split("\n\n")
fields = constr_fields(groups_instrs[0].splitlines())
my_ticket = [int(nb) for nb in groups_instrs[1].splitlines()[1].split(",")]
tickets = groups_instrs[2].splitlines()[1:]
tickets = [[int(nb) for nb in ticket.split(",")] for ticket in tickets]

good_tickets = get_valid_tickets(tickets, fields)
# my_utils.print_matrice(good_tickets)

res1 = scan_rate(tickets, fields)
print(res1)

real_fields = get_real_fields(good_tickets, fields)

res2 = 1
for i, elem in enumerate(real_fields):
    if "departure" in elem:
        res2 *= my_ticket[i]

print(res2)

