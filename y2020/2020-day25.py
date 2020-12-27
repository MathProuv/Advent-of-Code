import inputAoC as aoc


SUBJECT_NUMBER = 7
card, door = [int(nb) for nb in aoc.get_input_file(25,2020).splitlines()]


def handshake(loop_size, subject_nb=SUBJECT_NUMBER):
    value = 1
    for _ in range(loop_size):
        value *= subject_nb
        value %= 20201227
    return value

assert handshake(8) == 5764801
assert handshake(11) == 17807724
assert handshake(8, handshake(11)) == 14897079
assert handshake(11, handshake(8)) == 14897079


def get_loopsize(value, subject_nb=SUBJECT_NUMBER):
    val = 1
    loop_size = 0
    while val != value:
        loop_size += 1
        val *= subject_nb
        val %= 20201227
    return loop_size

assert get_loopsize(5764801) == 8
assert get_loopsize(17807724) == 11

def encryption_key(card, door):
    loop_size_card = get_loopsize(card)
    return handshake(loop_size_card, door)

assert encryption_key(5764801, 17807724) == 14897079


res1 = encryption_key(card, door)
print(res1)
