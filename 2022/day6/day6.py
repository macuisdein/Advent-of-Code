#!/bin/env python3
# I don't feel like doing OO today
file = open("input.txt")
message = file.read()
message_list = []
message_list.extend(message)
length_of_chars = len(message_list)

# Part 1
for x in range(0,length_of_chars - 3):
    try_list = []
    try_list = message_list[x:x+4]
    list_set = set(try_list)
    if len(list_set) == 4:
        print(f"First marker appeared at {x+4}")
        print(f"Items: {list_set}")
        break

# Part 2
for x in range(0,length_of_chars - 13):
    try_list = []
    try_list = message_list[x:x+15]
    list_set = set(try_list)
    if len(list_set) == 14:
        print(f"First marker appeared at {x+15}")
        print(f"Items: {list_set}")
        break