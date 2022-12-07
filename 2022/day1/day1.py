#!/usr/bin/env python3

class Elf(object):

    def __init__(self, id):
        self.id = id
        self.load = []
        self.calories = 0
        
    def load_item(self, item):
        self.load.append(item)

    def count_calories(self):
        for item in self.load:
            self.calories += int(item)
        return self.calories

elfcounter = 0
elflist = []
max_elf_calories = 0
max_elf_id = 0

with open("nput.txt") as file:
    elflist.append(Elf(elfcounter))
    for line in file:
        if line == '\n':
            elflist[elfcounter].count_calories()
            if elflist[elfcounter].calories > max_elf_calories:
                print(f"Elf {elflist[elfcounter].id} has the most calories so far at {elflist[elfcounter].calories}")
                max_elf_calories = elflist[elfcounter].calories
                max_elf_id = elflist[elfcounter].id
                elfcounter = elfcounter + 1
                elflist.append(Elf(elfcounter))
            else:
                (f"Elf {elflist[elfcounter].id} only had {elflist[elfcounter].calories} not more than {max_elf_calories}")
                elfcounter = elfcounter + 1
                elflist.append(Elf(elfcounter))
        else:
            elflist[elfcounter].load_item(line)

print(f"We have {len(elflist)} total elves")

# Part 2
calorie_list = []
for elf in elflist:
    calorie_list.append(elf.calories)
calorie_list.sort(reverse=True)
top3 = calorie_list[0] + calorie_list[1] + calorie_list[2]
print(f"Top three total calories: {top3}")
