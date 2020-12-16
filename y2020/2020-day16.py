import inputAoC as aoc
import re
import my_utils

groups_instrs = aoc.get_input_file(16,2020).split("\n\n")

def constr_fields(groups_instrs) -> dict:
    fields = dict()

    for field in groups_instrs[0].splitlines():
        m = re.match(r"([a-z ]+): (\d+)-(\d+) or (\d+)-(\d+)", field)
        f, a1, b1, a2, b2 = m.groups()
        fields[f] = [(int(a1),int(b1)), (int(a2),int(b2))]

    #my_utils.print_dict(fields)
    return fields

def fields_ranges(fields:dict) -> [tuple]:
    ranges = []
    for v_field in fields.values():
        ranges.extend(v_field)
    return ranges

def ticket_score(ticket:str, fields:dict):
    ranges = fields_ranges(fields)
    score = 0
    for number in ticket.split(","):
        nb = int(number)
        for rang in ranges:
            if rang[0] <= nb <= rang[1]:
                nb = 0
        score += nb
    return score

def valid_tickets(tickets, fields):
    res = []
    for ticket in tickets:
        if not ticket_score(ticket, fields):
            res.append(ticket)
    return res

def scan_rate(tickets:[str], fields):
    rate = 0
    for ticket in tickets:
        rate += ticket_score(ticket, fields)
    return rate


fields = constr_fields(groups_instrs)
tickets = groups_instrs[2].splitlines()[1:]
good_tickets = valid_tickets(tickets, fields)
my_utils.print_matrice(good_tickets)

res1 = scan_rate(tickets, fields)
print(res1)


