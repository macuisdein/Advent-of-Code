#!/usr/bin/env python3

class Rucksack(object):
    def __init__(self):
        self.number_of_compartments = 2
        self.compartment_list = []
        for x in range(0,self.number_of_compartments):
            self.compartment_list.append(Compartment(x))

    def fill_ruck(self,item_list):
        item_list_length = len(item_list)
        item_list_length_fill_size = item_list_length / self.number_of_compartments
        for compartment in self.compartment_list:
            for x in range(int(compartment.compartment_id * item_list_length_fill_size),int((compartment.compartment_id + 1) * item_list_length_fill_size)):
                compartment.compartment_storage_list.append(Items(item_list[x]))

    def find_common_item(self):
        self.common_item_value = 0
        for item in self.compartment_list[0].compartment_storage_list:
            for thing in self.compartment_list[1].compartment_storage_list:
                if item.id == thing.id:
                    # print(f"Common item is: {item.id} priority: {item.priority}")
                    self.common_item_value = item.priority

    def all_items(self):
        all_items = []
        for compartment in self.compartment_list:
            all_items.append(compartment.compartment_storage_list)
        return all_items

class Compartment(object):
    def __init__(self,compartment_id):
        self.compartment_id = compartment_id
        self.compartment_storage_list = []

class Items(object):
    def __init__(self,id):
        self.id = id
        priority_map = {"a":1,"b":2,"c":3,"d":4,"e":5,"f":6,"g":7,"h":8,"i":9,"j":10,"k":11,"l":12,"m":13,"n":14,"o":15,"p":16,"q":17,"r":18,"s":19,"t":20,"u":21,"v":22,"w":23,"x":24,"y":25,"z":26,"A":27,"B":28,"C":29,"D":30,"E":31,"F":32,"G":33,"H":34,"I":35,"J":36,"K":37,"L":38,"M":39,"N":40,"O":41,"P":42,"Q":43,"R":44,"S":45,"T":46,"U":47,"V":48,"W":49,"X":50,"Y":51,"Z":52}
        self.priority = priority_map[self.id]

rucksack_count = 0
rucksack_list = []  
common_item_sum = 0      
with open("input.txt") as file:
    for line in file:
        rucksack_list.append(Rucksack())
        rucksack_list[rucksack_count].fill_ruck(line.strip())
        rucksack_count = rucksack_count + 1

for rucksack in rucksack_list:
    rucksack.find_common_item()
    common_item_sum = common_item_sum + rucksack.common_item_value

print(f"Common item sum is: {common_item_sum}")


# Part 2
# This is where my approach went really bad -- I thougt we were going to be making more compartments
# print(rucksack_count)

badge_value = 0
for group in range(1,rucksack_count,3):
    # print(f"Group number: {group}")
    for items in rucksack_list[group - 1].all_items():
        for item in items:
            for things in rucksack_list[group].all_items():
                for thing in things:
                    for pieces in rucksack_list[group + 1].all_items():
                        for piece in pieces:
                            if item.id == thing.id == piece.id:
                                # print(f"Badge: {item.id} found for group {group} for {item.priority} priority value.")
                                badge_value = badge_value + item.priority
                                break
                        else:
                            continue
                        break
                    else:
                        continue
                    break
                else:
                    continue
                break
            else:
                continue
            break
print(f"Badge value is {badge_value}")
        