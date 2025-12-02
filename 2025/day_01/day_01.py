#!/usr/bin/env python3

# We have a lock where we need to check the count of the times we end up at 0
# Essentially we need to read input, split into R or L, go distance, check position
def process_instruction(instruction: str, old_offset: int, count_of_zero_position2: int):
    '''Take in an instruction and current_offset, return the new current_offset'''
    
    instruction, count_of_zero_position2 = split_instruction(instruction, count_of_zero_position2)
    current_offset = old_offset + instruction

    

    # We can't go outside our boundaries
    if current_offset < 0:
        current_offset = current_offset + 100
        if old_offset != 0:
            # If we were at 0, we already counted that
            count_of_zero_position2 = count_of_zero_position2 + 1
            print(f"We went below 0 to {current_offset}, add a count")
    elif current_offset > 99:
        current_offset = current_offset - 100
        if current_offset != 0:
            # If we go to zero, we will count that
            count_of_zero_position2 = count_of_zero_position2 + 1
            print(f"We went above 100 to {current_offset}, add a count")
    # elif current_offset ==  0 or current_offset == 100:
    #     # We went left and stopped at zero
    #     print(f"We stopped at {current_offset}, add a count")
    #     count_of_zero_position2 = count_of_zero_position2 + 1
    return current_offset, count_of_zero_position2


def split_instruction(instruction: str, count_of_zero_position2: int):
    '''Take in the instruction string and return mathematical value'''
    # The first character in the instruction should be the direction, 'R' or 'L'
    instruction_dir = instruction[0]
    # print(f'Instruction direction = {instruction_dir}')

    # Part 1 The remaining characters are the degree, if it's greater than two digits, we don't care
    instruction_degree = instruction[1:]
    instruction_degree = instruction_degree[-2:]
    # print(f'Instruction degree ={instruction_degree}')

    # Part 2
    # We now care about the other digits, but they should give us a good way to add
    instruction_degree2 = instruction[1:]
    if len(instruction_degree2) > 2:
        instruction_degree2 = instruction_degree2[:-2]
        instruction_degree2 = int(instruction_degree2)
        count_of_zero_position2 = count_of_zero_position2 + instruction_degree2
        print(f"We went {instruction_degree2} times around the dial")


    #should be treated as an integer
    instruction_degree = int(instruction_degree)
    
    # If we have 'L' we can multiply by negative 1
    if instruction_dir == 'L':
        instruction_degree = instruction_degree * -1
    # If there is not an 'L', it's positive
    print(f"Instruction {instruction} translated to {instruction_degree}")
    return instruction_degree, count_of_zero_position2


def increment_on_password(position: int, count_of_zero_position: int, count_of_zero_position2: int):
    if position == 0:
        print('We stopped on zero, add a count')
        count_of_zero_position = count_of_zero_position + 1
        count_of_zero_position2 = count_of_zero_position2 + 1
    return count_of_zero_position, count_of_zero_position2

# Starting positin is 50
current_position = 50

#  We start with zero '0'
count_of_zero_position = 0

# We need to store the instructions to process
instructions = []

# Part 2 we need a new count of zero
count_of_zero_position2 = 0

with open('input.txt', 'r') as f:
    instructions = f.readlines()
    for instruction in range(0, len(instructions)):
        instructions[instruction] = (instructions[instruction]).strip()
        
for instruction in instructions:
    print(f"Starting at {current_position}")
    current_position, count_of_zero_position2 = process_instruction(instruction, current_position, count_of_zero_position2)
    count_of_zero_position, count_of_zero_position2 = increment_on_password(current_position, count_of_zero_position, count_of_zero_position2)
    print(f"Count of position2 {count_of_zero_position2}")
    print(f"Current position: {current_position}")

print(f"PART 01: We found password of {count_of_zero_position}")

print(f"PART 02: We found password of {count_of_zero_position2}")

# For part 2, we need to count the number of times we either stopped at 0 or passed by 0. 
# It's easy enough to check if we went passed 0 in our checks in process_instruction()
# We also need to now care about multiple times of 100s in split_instruction()