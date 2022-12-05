#!/bin/env python3
import string
class Stack(object):
    def __init__(self,id):
        self.id = id
        self.contents = []

    def push(self,item):
        self.contents.append(item)
    
    def pop(self):
        item = self.contents.pop()
        return item

    def peek(self):
        item = self.contents[-1]
        return item

class Crates(object):
    def __init__(self,id):
        self.id = id

NUMBER_OF_STACKS = 9

stack_list = []

for x in range (0,NUMBER_OF_STACKS + 1):
    stack_list.append(Stack(x))

# Giving up on trying to identify formula
# stack 1 = line[1]
# stack 2 = line[5]
# stack 3 = line[9]
# stack 4 = line[13]
# stack 5 = line[17]
# stack 6 = line[21]
# stack 7 = line[25]
# stack 8 = line[29]
# stack 9 = line[33]

stack_identity = {1:1,5:2,9:3,13:4,17:5,21:6,25:7,29:8,33:9}

# First read the file backwards to get the starting position
preload_file = open("input.txt")
lines = preload_file.readlines()
for line in reversed(lines):
    if "[" in line:
        for x in range(0,len(line)):
            if line[x] in list(string.ascii_uppercase):
                stack_list[stack_identity[x]].push(line[x]) 
preload_file.close()

# Now read the file forwards to move the items
file = open("input.txt")
lines = file.readlines()

for line in lines:
    if "move" in line:
        command = [int(i) for i in line.split() if i.isdigit()]
        how_many = command[0]
        from_stack = command[1]
        to_stack = command[2]
        for x in range(0,how_many):
            item=stack_list[from_stack].pop()
            stack_list[to_stack].push(item)
file.close()
message = []
for x in range(1, NUMBER_OF_STACKS + 1):
    message.append(stack_list[x].peek())

print(f"First message: {''.join(message)}")


# Part 2
# First read the file backwards to get the starting position

print("WARNING!! Memory leak in this code!")
for x in range (0,NUMBER_OF_STACKS + 1):
    stack_list.append(Stack(x))
preload_file = open("input.txt")
lines = preload_file.readlines()
for line in reversed(lines):
    if "[" in line:
        for x in range(0,len(line)):
            if line[x] in list(string.ascii_uppercase):
                stack_list[stack_identity[x]].push(line[x]) 
preload_file.close()

file = open("input.txt")
lines = file.readlines()

for line in lines:
    if "move" in line:
        command = [int(i) for i in line.split() if i.isdigit()]
        how_many = command[0]
        from_stack = command[1]
        to_stack = command[2]
        item_to_move = []
        
        for x in range(0,how_many):
            item_to_move.append(stack_list[from_stack].pop())
        item_to_move.reverse()
        
        for item in item_to_move:
            stack_list[to_stack].push(item)
file.close()
message = []
for x in range(1, NUMBER_OF_STACKS + 1):
    message.append(stack_list[x].peek())

print(f"Second message: {''.join(message)}")
