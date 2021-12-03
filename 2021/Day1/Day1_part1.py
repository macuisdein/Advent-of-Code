#!/usr/local/opt/python@3.10/bin/python3

import itertools

# We are reading depth values from an input file. 
# We are being asked to see how many increases and decreases there are.


# Open the file for reading
f = open('2021/Day1/input.txt', 'r')

# Let's create an empty list to store the values should we need to access again
list_of_values = []

# Store each value in our list
for line in f:
    list_of_values.append(int(line))


# Time to look at each value in our list and do our comparisons

# Let's have a count for each increase or decrease
number_of_increase = 0
number_of_decrease = 0

for a,b in itertools.pairwise(list_of_values):
    if a > b:
        number_of_decrease = number_of_decrease + 1
    elif b > a:
        number_of_increase = number_of_increase + 1
    else:
        next

print("Number of increase: " + str(number_of_increase))
print("Number of decrease: " + str(number_of_decrease))
