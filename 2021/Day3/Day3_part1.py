#!/usr/local/opt/python@3.10/bin/python3

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

# Each line should be a string five bits -- but in the "real" input it is 12!!

for line in f:
    first_bit_list.append(line[0])
    second_bit_list.append(line[1])
    third_bit_list.append(line[2])
    fourth_bit_list.append(line[3])
    fifth_bit_list.append(line[4])
    sixth_bit_list.append(line[5])
    seventh_bit_list.append(line[6])
    eightth_bit_list.append(line[7])
    ninth_bit_list.append(line[8])
    tenth_bit_list.append(line[9])
    eleventh_bit_list.append(line[10])
    twelth_bit_list.append(line[11])

# Find most common bit in each position
def most_frequent(List):
    return max(set(List), key = List.count)

most_frequent_bit_list = []

most_frequent_bit_list.append(most_frequent(first_bit_list))
most_frequent_bit_list.append(most_frequent(second_bit_list))
most_frequent_bit_list.append(most_frequent(third_bit_list))
most_frequent_bit_list.append(most_frequent(fourth_bit_list))
most_frequent_bit_list.append(most_frequent(fifth_bit_list))
most_frequent_bit_list.append(most_frequent(sixth_bit_list))
most_frequent_bit_list.append(most_frequent(seventh_bit_list))
most_frequent_bit_list.append(most_frequent(eightth_bit_list))
most_frequent_bit_list.append(most_frequent(ninth_bit_list))
most_frequent_bit_list.append(most_frequent(tenth_bit_list))
most_frequent_bit_list.append(most_frequent(eleventh_bit_list))
most_frequent_bit_list.append(most_frequent(twelth_bit_list))


# We can make a string of all the bits
most_frequent_bits_string = "".join(most_frequent_bit_list)

# Convert string to a number
gamma_rate = int(most_frequent_bits_string,base=2)

# Here's where we can use bitwise operations -- getting the inverse 
invert_string = "111111111111"
invert_int = int(invert_string, base=2)
epsilon_rate = gamma_rate ^ invert_int
power_consumption = gamma_rate * epsilon_rate

print("Submarine power consumption is " + str(abs(power_consumption)))
