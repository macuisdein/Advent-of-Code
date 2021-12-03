#!/usr/local/opt/python@3.10/bin/python3

# Ah, so here in part 2 we see that our process is not going to be as worthwhile.

# We are being asked to look at binary outputs. Expecting bitwise operations, but didn't see a shortcut there yet.
# If we split into lists of strings, we can use a set

first_bit_list = []
second_bit_list = []
third_bit_list = []
fourth_bit_list = []
fifth_bit_list = []
sixth_bit_list = []
seventh_bit_list = []
eightth_bit_list = []
ninth_bit_list = []
tenth_bit_list = []
eleventh_bit_list = []
twelth_bit_list = []


# Open the File
f = open('2021/Day3/input.txt', 'r')

# This time we will store the input into a repeatable pattern
current_list = []
for line in f:
    current_list.append(line)
f.close

def most_frequent(List):
    return max(set(List), key = List.count)

most_frequent_bit_list = [0,0,0,0,0,0,0,0,0,0,0,0]
next_list = []
# Repeat until lenght of list is 1
print("Finding Max")
for index in range(12):
    if len(current_list) == 1:
        most_frequent_bit_list[index] = current_list[0][1]
        break
    # Find most frequent bit we care about
    bit_list = []
    for line in current_list:
        bit_list.append(line[index])
    most_frequent_bit_list[index] = most_frequent(bit_list)
    # Interpret as a number
    tempmask = most_frequent_bit_list[index]
    # Now we have to find only those items that match our bitmask
    for line in current_list:
        if line[index] == tempmask:
            next_list.append(line)
    # Now that we found all, it's time to keep only those that matched
    current_list = next_list
    next_list = []
print("Finding Min")
current_list = []
f = open('2021/Day3/input.txt', 'r')
for line in f:
    current_list.append(line)
f.close
least_frequent_bit_list = [0,0,0,0,0,0,0,0,0,0,0,0]
next_list = []
# Repeat until lenght of list is 1
for index in range(12):
    if len(current_list) == 1:
        least_frequent_bit_list = current_list[0]
        break
    # Find most frequent bit we care about
    bit_list = []
    for line in current_list:
        bit_list.append(line[index])
    least_frequent_bit_list[index] = str(1 ^ int(most_frequent(bit_list),2))
    # Interpret as a number
    tempmask = least_frequent_bit_list[index]
    # Now we have to find only those items that match our bitmask
    for line in current_list:
        if line[index] == tempmask:
            next_list.append(line)
    # Now that we found all, it's time to keep only those that matched
    current_list = next_list
    next_list = []


# Let's see our bits!
most_frequent_bits_string = "".join(most_frequent_bit_list)    
least_frequent_bits_string = "".join(least_frequent_bit_list) 
# Convert string to a number
oxygen_rate = int(most_frequent_bits_string,base=2)
co2_rate = int(least_frequent_bit_list,base=2)

# Here's where we can use bitwise operations -- getting the inverse 
# invert_string = "111111111111"
# invert_int = int(invert_string, base=2)
# epsilon_rate = gamma_rate ^ invert_int
# power_consumption = gamma_rate * epsilon_rate

print("Submarine oxygen consumption is " + str(abs(oxygen_rate)))
print("Submarine CO2 consumption is " + str(abs(co2_rate)))
print("Life support rating: " + str(abs(co2_rate) * abs(oxygen_rate)))