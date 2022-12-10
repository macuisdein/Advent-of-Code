#!/usr/bin/env python3

knot_2_x = 0
knot_2_y = 0
knot_3_x = 0
knot_3_y = 0
knot_4_x = 0
knot_4_y = 0
knot_5_x = 0
knot_5_y = 0
knot_6_x = 0
knot_6_y = 0
knot_7_x = 0
knot_7_y = 0
knot_8_x = 0
knot_8_y = 0
knot_9_x = 0
knot_9_y = 0


head_position_x = 0
head_position_y = 0
tail_position_x = 0
tail_position_y = 0
tail_visited = [(0,0)]
head_position = (head_position_x,head_position_y)
tail_input = ""
file = open("input.txt")

def get_tail_action(difference, tail_position_x, tail_position_y):
    if difference == (2,0):
        tail_position_x = tail_position_x + 1
    elif difference == (0,2):
        tail_position_y = tail_position_y + 1
    elif difference == (1,2):
        tail_position_x = tail_position_x + 1
        tail_position_y = tail_position_y + 1
    elif difference == (2,1):
        tail_position_x = tail_position_x + 1
        tail_position_y = tail_position_y + 1
    elif difference == (-2,0):
        tail_position_x = tail_position_x - 1
    elif difference == (0,-2):
        tail_position_y = tail_position_y - 1
    elif difference == (-1,-2):
        tail_position_y = tail_position_y - 1
        tail_position_x = tail_position_x - 1
    elif difference == (-2,-1):
        tail_position_y = tail_position_y - 1
        tail_position_x = tail_position_x - 1
    elif difference == (-2,1):
        tail_position_y = tail_position_y + 1
        tail_position_x = tail_position_x - 1
    elif difference == (2,-1):
        tail_position_y = tail_position_y - 1
        tail_position_x = tail_position_x + 1
    elif difference == (1,1):
        pass
    elif difference == (0,0):
        pass
    elif difference == (1,0):
        pass
    elif difference == (0,1):
        pass
    elif difference == (-1,-1):
        pass
    elif difference == (0,-1):
        pass
    elif difference == (-1,0):
        pass
    elif difference == (1,-1):
        pass
    elif difference == (-1,1):
        pass
    elif difference == (2,2):
        tail_position_x = tail_position_x + 1
        tail_position_y = tail_position_y + 1
    elif difference == (-1,2):
        tail_position_x = tail_position_x - 1
        tail_position_y = tail_position_y + 1
    elif difference == (-2,2):
        tail_position_x = tail_position_x - 1
        tail_position_y = tail_position_y + 1
    elif difference == (1,-2):
        tail_position_x = tail_position_x + 1
        tail_position_y = tail_position_y - 1
    elif difference == (-2,-2):
        tail_position_x = tail_position_x - 1
        tail_position_y = tail_position_y - 1
    elif difference == (2,-2):
        tail_position_x = tail_position_x + 1
        tail_position_y = tail_position_y - 1
    else:
        print(f"We have a bad situation!! Difference = {difference}")
    return (tail_position_x, tail_position_y)

for line in file:
    line_split=line.split()
    direction = line_split[0]
    degree = int(line_split[1])
    if direction == "R":
        for motion in range(degree):
            head_position_x = head_position_x + 1
                        
            difference_x = head_position_x - knot_2_x
            difference_y = head_position_y - knot_2_y
            difference = (difference_x, difference_y)
            knot_2_x, knot_2_y = get_tail_action(difference, knot_2_x, knot_2_y)
            difference_x = knot_2_x - knot_3_x
            difference_y = knot_2_y - knot_3_y
            difference = (difference_x, difference_y)
            knot_3_x, knot_3_y = get_tail_action(difference, knot_3_x, knot_3_y)
            difference_x = knot_3_x - knot_4_x
            difference_y = knot_3_y - knot_4_y
            difference = (difference_x, difference_y)
            knot_4_x, knot_4_y = get_tail_action(difference, knot_4_x, knot_4_y)
            difference_x = knot_4_x - knot_5_x
            difference_y = knot_4_y - knot_5_y
            difference = (difference_x, difference_y)
            knot_5_x, knot_5_y = get_tail_action(difference, knot_5_x, knot_5_y)
            difference_x = knot_5_x - knot_6_x
            difference_y = knot_5_y - knot_6_y
            difference = (difference_x, difference_y)
            knot_6_x, knot_6_y = get_tail_action(difference, knot_6_x, knot_6_y)
            difference_x = knot_6_x - knot_7_x
            difference_y = knot_6_y - knot_7_y
            difference = (difference_x, difference_y)
            knot_7_x, knot_7_y = get_tail_action(difference, knot_7_x, knot_7_y)
            difference_x = knot_7_x - knot_8_x
            difference_y = knot_7_y - knot_8_y
            difference = (difference_x, difference_y)
            knot_8_x, knot_8_y = get_tail_action(difference, knot_8_x, knot_8_y)
            difference_x = knot_8_x - knot_9_x
            difference_y = knot_8_y - knot_9_y
            difference = (difference_x, difference_y)
            knot_9_x, knot_9_y = get_tail_action(difference, knot_9_x, knot_9_y)
            difference_x = knot_9_x - tail_position_x
            difference_y = knot_9_y - tail_position_y
            difference = (difference_x, difference_y)
            tail_position_x, tail_position_y = get_tail_action(difference, tail_position_x, tail_position_y)
            tail_visited.append((tail_position_x,tail_position_y))

    if direction == "L":
        for motion in range(degree):
            head_position_x = head_position_x - 1
                        
            difference_x = head_position_x - knot_2_x
            difference_y = head_position_y - knot_2_y
            difference = (difference_x, difference_y)
            knot_2_x, knot_2_y = get_tail_action(difference, knot_2_x, knot_2_y)
            difference_x = knot_2_x - knot_3_x
            difference_y = knot_2_y - knot_3_y
            difference = (difference_x, difference_y)
            knot_3_x, knot_3_y = get_tail_action(difference, knot_3_x, knot_3_y)
            difference_x = knot_3_x - knot_4_x
            difference_y = knot_3_y - knot_4_y
            difference = (difference_x, difference_y)
            knot_4_x, knot_4_y = get_tail_action(difference, knot_4_x, knot_4_y)
            difference_x = knot_4_x - knot_5_x
            difference_y = knot_4_y - knot_5_y
            difference = (difference_x, difference_y)
            knot_5_x, knot_5_y = get_tail_action(difference, knot_5_x, knot_5_y)
            difference_x = knot_5_x - knot_6_x
            difference_y = knot_5_y - knot_6_y
            difference = (difference_x, difference_y)
            knot_6_x, knot_6_y = get_tail_action(difference, knot_6_x, knot_6_y)
            difference_x = knot_6_x - knot_7_x
            difference_y = knot_6_y - knot_7_y
            difference = (difference_x, difference_y)
            knot_7_x, knot_7_y = get_tail_action(difference, knot_7_x, knot_7_y)
            difference_x = knot_7_x - knot_8_x
            difference_y = knot_7_y - knot_8_y
            difference = (difference_x, difference_y)
            knot_8_x, knot_8_y = get_tail_action(difference, knot_8_x, knot_8_y)
            difference_x = knot_8_x - knot_9_x
            difference_y = knot_8_y - knot_9_y
            difference = (difference_x, difference_y)
            knot_9_x, knot_9_y = get_tail_action(difference, knot_9_x, knot_9_y)
            difference_x = knot_9_x - tail_position_x
            difference_y = knot_9_y - tail_position_y
            difference = (difference_x, difference_y)
            tail_position_x, tail_position_y = get_tail_action(difference, tail_position_x, tail_position_y)
            tail_visited.append((tail_position_x,tail_position_y))

    if direction == "U":
        for motion in range(degree):
            head_position_y = head_position_y + 1
                        
            difference_x = head_position_x - knot_2_x
            difference_y = head_position_y - knot_2_y
            difference = (difference_x, difference_y)
            knot_2_x, knot_2_y = get_tail_action(difference, knot_2_x, knot_2_y)
            difference_x = knot_2_x - knot_3_x
            difference_y = knot_2_y - knot_3_y
            difference = (difference_x, difference_y)
            knot_3_x, knot_3_y = get_tail_action(difference, knot_3_x, knot_3_y)
            difference_x = knot_3_x - knot_4_x
            difference_y = knot_3_y - knot_4_y
            difference = (difference_x, difference_y)
            knot_4_x, knot_4_y = get_tail_action(difference, knot_4_x, knot_4_y)
            difference_x = knot_4_x - knot_5_x
            difference_y = knot_4_y - knot_5_y
            difference = (difference_x, difference_y)
            knot_5_x, knot_5_y = get_tail_action(difference, knot_5_x, knot_5_y)
            difference_x = knot_5_x - knot_6_x
            difference_y = knot_5_y - knot_6_y
            difference = (difference_x, difference_y)
            knot_6_x, knot_6_y = get_tail_action(difference, knot_6_x, knot_6_y)
            difference_x = knot_6_x - knot_7_x
            difference_y = knot_6_y - knot_7_y
            difference = (difference_x, difference_y)
            knot_7_x, knot_7_y = get_tail_action(difference, knot_7_x, knot_7_y)
            difference_x = knot_7_x - knot_8_x
            difference_y = knot_7_y - knot_8_y
            difference = (difference_x, difference_y)
            knot_8_x, knot_8_y = get_tail_action(difference, knot_8_x, knot_8_y)
            difference_x = knot_8_x - knot_9_x
            difference_y = knot_8_y - knot_9_y
            difference = (difference_x, difference_y)
            knot_9_x, knot_9_y = get_tail_action(difference, knot_9_x, knot_9_y)
            difference_x = knot_9_x - tail_position_x
            difference_y = knot_9_y - tail_position_y
            difference = (difference_x, difference_y)
            tail_position_x, tail_position_y = get_tail_action(difference, tail_position_x, tail_position_y)
            tail_visited.append((tail_position_x,tail_position_y))

    if direction == "D":
        for motion in range(degree):
            head_position_y = head_position_y -1
                        
            difference_x = head_position_x - knot_2_x
            difference_y = head_position_y - knot_2_y
            difference = (difference_x, difference_y)
            knot_2_x, knot_2_y = get_tail_action(difference, knot_2_x, knot_2_y)
            difference_x = knot_2_x - knot_3_x
            difference_y = knot_2_y - knot_3_y
            difference = (difference_x, difference_y)
            knot_3_x, knot_3_y = get_tail_action(difference, knot_3_x, knot_3_y)
            difference_x = knot_3_x - knot_4_x
            difference_y = knot_3_y - knot_4_y
            difference = (difference_x, difference_y)
            knot_4_x, knot_4_y = get_tail_action(difference, knot_4_x, knot_4_y)
            difference_x = knot_4_x - knot_5_x
            difference_y = knot_4_y - knot_5_y
            difference = (difference_x, difference_y)
            knot_5_x, knot_5_y = get_tail_action(difference, knot_5_x, knot_5_y)
            difference_x = knot_5_x - knot_6_x
            difference_y = knot_5_y - knot_6_y
            difference = (difference_x, difference_y)
            knot_6_x, knot_6_y = get_tail_action(difference, knot_6_x, knot_6_y)
            difference_x = knot_6_x - knot_7_x
            difference_y = knot_6_y - knot_7_y
            difference = (difference_x, difference_y)
            knot_7_x, knot_7_y = get_tail_action(difference, knot_7_x, knot_7_y)
            difference_x = knot_7_x - knot_8_x
            difference_y = knot_7_y - knot_8_y
            difference = (difference_x, difference_y)
            knot_8_x, knot_8_y = get_tail_action(difference, knot_8_x, knot_8_y)
            difference_x = knot_8_x - knot_9_x
            difference_y = knot_8_y - knot_9_y
            difference = (difference_x, difference_y)
            knot_9_x, knot_9_y = get_tail_action(difference, knot_9_x, knot_9_y)
            difference_x = knot_9_x - tail_position_x
            difference_y = knot_9_y - tail_position_y
            difference = (difference_x, difference_y)
            tail_position_x, tail_position_y = get_tail_action(difference, tail_position_x, tail_position_y)
            tail_visited.append((tail_position_x,tail_position_y))
    
    
    


print(f"Final Head Position X: {head_position_x}, Position Y: {head_position_y}")
print(f"Final Tail Position X: {tail_position_x}, Position Y: {tail_position_y}")

print(tail_visited)
print(len(tail_visited))

print(set(tail_visited))
print(len(set(tail_visited)))
