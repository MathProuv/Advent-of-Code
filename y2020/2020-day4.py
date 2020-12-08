import inputAoC as aoc

docs = aoc.get_input_file(4).split("\n\n")

res1 = 0
res2 = 0

def isnumeric(val):
    try:
        int(val)
        return True
    except ValueError:
        return False

def is_str_nb_in_interv(val, a, b, nbDigits = -1):
    if nbDigits >= 0 and len(val) != nbDigits and val.isdigit():
        return False
    return isnumeric(val) and a <= int(val) <= b

for doc in docs:
    doc = doc.replace('\n', ' ')
    doc = doc.split()
    dic = {}
    for elem in doc:
        champ, contenu = elem.split(":")
        dic[champ] = contenu
    if dic.keys() == {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid", "cid"} or dic.keys() == {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}:
        res1 += 1
        if not (is_str_nb_in_interv(dic["byr"], 1920, 2002, 4)):
            continue
        if not (is_str_nb_in_interv(dic["iyr"], 2010, 2020, 4)):
            continue
        if not (is_str_nb_in_interv(dic["eyr"], 2020, 2030, 4)):
            continue
        hgt = dic["hgt"]
        hgt_nb, hgt_unit = hgt[:-2], hgt[-2:]
        if not (hgt_unit == 'cm' and is_str_nb_in_interv(hgt_nb, 150, 193) or hgt_unit == "in" and is_str_nb_in_interv(hgt_nb, 59, 76)):
            continue
        hcl = dic["hcl"]
        hcl_regex = hcl[0] == "#"
        for c in hcl[1:]:
            if not ("0" <= c <= "9" or "a" <= c <= "f"):
                hcl_regex = False
        if not hcl_regex:
            continue
        if not (dic["ecl"] in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]):
            continue
        if not (is_str_nb_in_interv(dic["pid"], 0, 1e10, 9)):
            continue
        res2 += 1
        
print(res1, res2, sep="\n")