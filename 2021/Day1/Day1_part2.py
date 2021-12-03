#!/usr/local/opt/python@3.10/bin/python3

import itertools

# We are reading depth values from an input file, but in groups of three. 
# We are then being asked to sum each group and see if there is an increase or decease.
# We can keep our Part 1 code, but process the groups first.

# Open the file for reading
f = open('2021/Day1/input.txt', 'r')

# Let's create an empty list to store the values should we need to access again
list_of_values = []
list_of_sums = []

# Store each value in our list
for line in f:
    list_of_values.append(int(line))

# Read three items from list and store to the new list
# We'll start our index at the third element and increment by 1 until we cannot
index = 2
while index < len(list_of_values):
    sum = list_of_values[index - 2] + list_of_values[index -1 ] + list_of_values[index]
    list_of_sums.append(sum)
    index = index + 1

# Time to look at each value in our list and do our comparisons

# Let's have a count for each increase or decrease
number_of_increase = 0
number_of_decrease = 0

for a,b in itertools.pairwise(list_of_sums):
    if a > b:
        number_of_decrease = number_of_decrease + 1
    elif b > a:
        number_of_increase = number_of_increase + 1
    else:
        next

print("Number of increase: " + str(number_of_increase))
print("Number of decrease: " + str(number_of_decrease))
