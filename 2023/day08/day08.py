file = open("input.txt", "r")
inputs = file.readlines()
instructions = ''
map_details = {}
for line in inputs:
    if '=' in line:
        # print(f"We have map: {line.strip()}")
        destination = (line.split('=')[0]).strip()
        option1 = (line.split('=')[1].strip().split(',')[0].split('(')[1]).strip()
        option2 = (line.split('=')[1].strip().split(',')[1].split(')')[0]).strip()
        # print(f"We have a map with destination: {destination}, option1: {option1}, and option2: {option2}")
        map_details[destination] = (option1, option2)
    elif line == '\n':
        # print(f"We have a blank line:")
        pass
    else:
        # print(f"We have instructions: {line.strip()}")
        instructions = line.strip()

instructions_translated=[]

for instruction in instructions:
    if instruction == 'L':
        instructions_translated.append(0)
    elif instruction == 'R':
        instructions_translated.append(1)    
# print(f"Instructions translated = {instructions_translated}")

# part1
current_location = map_details["AAA"]
taken_direction = ''
step_count = 0
# print(f"We are at AAA and our options are: {current_location}")
while taken_direction != 'ZZZ':
    for instruction in instructions_translated:
        taken_direction = current_location[instruction]
        # print(taken_direction)
        current_location = map_details[taken_direction]
        # print(current_location)
        step_count = step_count + 1

print(f"We reached Part 1 location: {taken_direction} in {step_count} steps")

# Part 2
starting_locations = []
for key in map_details.keys():
    if key[2] == 'A':
        # print(f"We have a starting location: {key}")
        starting_locations.append(key)

print(f"Part 2 starting locations: {starting_locations}")

current_locations ={}
ending_locations = []
not_each_ending_location = True
step_count = 0
for count in range(len(starting_locations)):
    current_locations[count] = starting_locations[count]
taken_directions = {}
reached_end={}
for count in range(len(starting_locations)):
    reached_end[count] = False
map_count = 0

reached_end_step_count = {}
while not_each_ending_location:
    

    for step in instructions_translated:
        # print(f"Map direction is {step}")
        step_count = step_count + 1
        for x in range(len(starting_locations)):
            
            # print(f"Options: Start {x} are {map_details[current_locations[x]]}")
            taken_directions[x] = map_details[current_locations[x]][step]
            # print(f"Start {x} took direction {taken_directions[x]}")
            if taken_directions[x][2] == 'Z':
                reached_end[x] = True
                reached_end_step_count[x] = step_count
                # print(f"Start {x} reached end {reached_end[x]} at {taken_directions[x]}")
            # else:
                # reached_end[x] = False
            current_locations[x] = taken_directions[x]
        if set(reached_end.values()) == {True}:
            print(f"We reached an end for all paths. Time to take LCM")
            not_each_ending_location = False
            break
import math
print(list(reached_end_step_count.values()))
print(math.lcm(*list(reached_end_step_count.values())))
