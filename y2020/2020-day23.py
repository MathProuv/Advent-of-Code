import inputAoC as aoc


cups = [int(cup) for cup in aoc.get_input_file(23, 2020)]
cups_ex = [3, 8, 9, 1, 2, 5, 4, 6, 7]


class LinkedListNode:
    def __init__(self, val, prev=None, next=None):
        self.prev = prev
        self.next = next
        self.val = val
    
    def __repr__(self):
        res = "val: " + str(self.val)
        res += " prev: " + str(self.prev.val)
        res += " next: " + str(self.next.val)
        return res


class Cups:
    NB_PICKS = 3

    def __init__(self, cups, MAX=-1):
        self.cups = [int(cup) for cup in cups]
        self.MAX = max(cups)
        if MAX > 0:
            self.cups += list(range(self.MAX+1, MAX+1))
            self.MAX = MAX
        
        self.nodes = dict()
        
        val0 = self.cups[0]
        first_node = LinkedListNode(val0)
        self.nodes[val0] = first_node
        old_node = first_node

        for val in self.cups[1:]:
            new_node = LinkedListNode(val, old_node, None)
            self.nodes[val] = new_node

            old_node.next = new_node
            old_node = new_node

        last_node = old_node
        last_node.next = first_node
        first_node.prev = last_node
        self.node = first_node
    

    def __repr__(self):
        debut = self.node
        res = str(debut.val)
        temp = debut.next
        while temp != debut:
            res += "  <=>  " + str(temp.val)
            temp = temp.next
            if len(res) >= 200:
                break
        return res
    

    def move1(self):
        cup = self.node
        # picked_up = cup.next(.next)(.next)
        pick1 = cup.next
        pick2 = pick1.next
        pick3 = pick2.next

        # on enlève les picked_up après cup
        cup.next = pick3.next
        (pick3.next).prev = cup

        dest = cup.val - 1
        if dest == 0: dest = self.MAX
        while dest in [pick.val for pick in [pick1, pick2, pick3]]:
            dest -= 1
            if dest == 0:
                dest = self.MAX

        #i = index(dest)
        i = self.nodes[dest]
        # assert dest == i.val

        # on ajoute les picked_up après i
        (i.next).prev = pick3
        pick1.prev = i
        pick3.next = i.next
        i.next = pick1
        
        self.node = cup.next
        return "on a fait un tour"


    def moves(self, n, to_print=False):
        for turn in range(1, n+1):
            if to_print: print(turn, ":", self)
            self.move1()
        if to_print: print("final", self)

    
    def score(self):
        i = self.node
        while i.val != 1:
            i = i.next
        res = ""
        i = i.next
        while i.val != 1:
            res += str(i.val)
            i = i.next
        return res
    
    def score_2(self):
        i = self.node
        while i.val != 1:
            i = i.next
        return i.next.val * i.next.next.val

cups2_ex = Cups(cups_ex)
cups2_ex.moves(10, True)


cups1 = Cups(cups)
cups1.moves(100)
res1 = cups1.score()
print(res1)


cups2 = Cups(cups, 1000000)
cups2.moves(10000000)
res2 = cups2.score_2()
print(res2)