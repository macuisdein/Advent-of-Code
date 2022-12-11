#!/usr/bin/env python3

class Item(object):
    def __init__(self,worry) -> None:
        self.worry = worry
    def get_worry(self):
        return self.worry
    def set_worry(self,worry):
        self.worry = worry

class Monkey(object):
    def __init__(self,id,buddy1,buddy2,items) -> None:
        self.id = id
        self.buddy1 = buddy1
        self.buddy2 = buddy2
        self.items = items
        self.count = 0
    
    def receive(self,item):
        self.items.append(item)
    
    def take_turn(self):
        for item in self.items:
            self.count = self.count + 1
            self._do_damage(item)
            self._test_pass(item)
        self.items = []
    
    def get_count(self):
        return self.count

    def get_id(self):
        return self.id

    def set_buddies(self,list):
        buddy1 = self.buddy1
        self.buddy1 = list[buddy1]
        buddy2 = self.buddy2
        self.buddy2 = list[buddy2]


class Monkey0(Monkey):
    def __init__(self, id, buddy1, buddy2, items) -> None:
        super().__init__(id, buddy1, buddy2, items)

    def _do_damage(self,item):
        worry = item.get_worry()
        # print(f"New worry: {worry}")
        worry = worry * 13
        worry = worry % ( 19 * 3 * 11 * 17 * 5 * 2 * 13 * 7) 
        item.set_worry(worry)
        # print(f"New worry: {worry}")

    def _test_pass(self,item):
        if item.get_worry() % 19 == 0:
            self.buddy1.receive(item)
        else:
            self.buddy2.receive(item)
            
class Monkey1(Monkey):
    def __init__(self, id, buddy1, buddy2, items) -> None:
        super().__init__(id, buddy1, buddy2, items)

    def _do_damage(self,item):
        worry = item.get_worry()
        # print(f"New worry: {worry}")
        worry = worry + 2
        worry = worry % ( 19 * 3 * 11 * 17 * 5 * 2 * 13 * 7)
        item.set_worry(worry)
        # print(f"New worry: {worry}")

    def _test_pass(self,item):
        if item.get_worry() % 3 == 0:
            self.buddy1.receive(item)
        else:
            self.buddy2.receive(item)


class Monkey2(Monkey):
    def __init__(self, id, buddy1, buddy2, items) -> None:
        super().__init__(id, buddy1, buddy2, items)

    def _do_damage(self,item):
        worry = item.get_worry()
        # print(f"New worry: {worry}")
        worry = worry + 1
        worry = worry % ( 19 * 3 * 11 * 17 * 5 * 2 * 13 * 7)
        item.set_worry(worry)
        # print(f"New worry: {worry}")

    def _test_pass(self,item):
        if item.get_worry() % 11 == 0:
            self.buddy1.receive(item)
        else:
            self.buddy2.receive(item)

class Monkey3(Monkey):
    def __init__(self, id, buddy1, buddy2, items) -> None:
        super().__init__(id, buddy1, buddy2, items)

    def _do_damage(self,item):
        worry = item.get_worry()
        # print(f"New worry: {worry}")
        worry = worry + 8
        worry = worry % ( 19 * 3 * 11 * 17 * 5 * 2 * 13 * 7)
        item.set_worry(worry)
        # print(f"New worry: {worry}")

    def _test_pass(self,item):
        if item.get_worry() % 17 == 0:
            self.buddy1.receive(item)
        else:
            self.buddy2.receive(item)

class Monkey4(Monkey):
    def __init__(self, id, buddy1, buddy2, items) -> None:
        super().__init__(id, buddy1, buddy2, items)

    def _do_damage(self,item):
        worry = item.get_worry()
        # print(f"New worry: {worry}")
        worry = worry * worry
        worry = worry % ( 19 * 3 * 11 * 17 * 5 * 2 * 13 * 7)
        item.set_worry(worry)
        # print(f"New worry: {worry}")

    def _test_pass(self,item):
        if item.get_worry() % 5 == 0:
            self.buddy1.receive(item)
        else:
            self.buddy2.receive(item)

class Monkey5(Monkey):
    def __init__(self, id, buddy1, buddy2, items) -> None:
        super().__init__(id, buddy1, buddy2, items)

    def _do_damage(self,item):
        worry = item.get_worry()
        # print(f"New worry: {worry}")
        worry = worry + 4
        worry = worry % ( 19 * 3 * 11 * 17 * 5 * 2 * 13 * 7)
        item.set_worry(worry)
        # print(f"New worry: {worry}")

    def _test_pass(self,item):
        if item.get_worry() % 2 == 0:
            self.buddy1.receive(item)
        else:
            self.buddy2.receive(item)


class Monkey6(Monkey):
    def __init__(self, id, buddy1, buddy2, items) -> None:
        super().__init__(id, buddy1, buddy2, items)

    def _do_damage(self,item):
        worry = item.get_worry()
        # print(f"New worry: {worry}")
        worry = worry * 17
        worry = worry % ( 19 * 3 * 11 * 17 * 5 * 2 * 13 * 7)
        item.set_worry(worry)
        # print(f"New worry: {worry}")

    def _test_pass(self,item):
        if item.get_worry() % 13 == 0:
            self.buddy1.receive(item)
        else:
            self.buddy2.receive(item)


class Monkey7(Monkey):
    def __init__(self, id, buddy1, buddy2, items) -> None:
        super().__init__(id, buddy1, buddy2, items)

    def _do_damage(self,item):
        worry = item.get_worry()
        # print(f"New worry: {worry}")
        worry = worry + 5
        worry = worry % ( 19 * 3 * 11 * 17 * 5 * 2 * 13 * 7)
        item.set_worry(worry)
        # print(f"New worry: {worry}")

    def _test_pass(self,item):
        if item.get_worry() % 7 == 0:
            self.buddy1.receive(item)
        else:
            self.buddy2.receive(item)

# monkey0
start_item_list =[75, 75, 98, 97, 79, 97, 64]
item_list = []
for item in start_item_list:
    item_list.append(Item(item))
monkey0 = Monkey0(0,2,7,item_list)

# monkey1
start_item_list = [50, 99, 80, 84, 65, 95]
item_list = []
for item in start_item_list:
    item_list.append(Item(item))

monkey1 = Monkey1(1,4,5,item_list)

# monkey2
start_item_list = [96, 74, 68, 96, 56, 71, 75, 53]
item_list = []
for item in start_item_list:
    item_list.append(Item(item))

monkey2 = Monkey2(2,7,3,item_list)

# monkey3
start_item_list = [83, 96, 86, 58, 92]
item_list = []
for item in start_item_list:
    item_list.append(Item(item))

monkey3 = Monkey3(3,6,1,item_list)

# monkey4
start_item_list = [99]
item_list = []
for item in start_item_list:
    item_list.append(Item(item))

monkey4 = Monkey4(4,0,5,item_list)

# monkey5
start_item_list = [60, 54, 83]
item_list = []
for item in start_item_list:
    item_list.append(Item(item))

monkey5 = Monkey5(5,2,0,item_list)

# monkey6
start_item_list = [77, 67]
item_list = []
for item in start_item_list:
    item_list.append(Item(item))

monkey6 = Monkey6(6,4,1,item_list)


# monkey7
start_item_list = [95, 65, 58, 76]
item_list = []
for item in start_item_list:
    item_list.append(Item(item))

monkey7 = Monkey7(7,3,6,item_list)


monkey_list = [monkey0,monkey1,monkey2,monkey3,monkey4,monkey5,monkey6,monkey7]

for monkey in monkey_list:
    monkey.set_buddies(monkey_list)

for round in range(0,10000):
    for monkey in monkey_list:
        monkey.take_turn()
max_items = []
for monkey in monkey_list:
    print(f"Monkey {monkey.get_id()} has handled {monkey.get_count()} items.")
    max_items.append(monkey.get_count())

max_items.sort(reverse=True)

print(max_items[0] * max_items[1])