#!/usr/bin/env python3

head_position_x = 0
head_position_y = 0
tail_position_x = 0
tail_position_y = 0
tail_visited = [(0,0)]
head_position = (head_position_x,head_position_y)
tail_input = ""
file = open("input_test.txt")

for line in file:
    line_split=line.split()
    direction = line_split[0]
    degree = int(line_split[1])
    if direction == "R":
        for motion in range(degree):
            head_position_x = head_position_x + 1
            print(f"Difference: ({head_position_x - tail_position_x}, {head_position_y - tail_position_y})")
            if head_position_y == tail_position_y:
                if abs(head_position_x - tail_position_x) == 2:
                    tail_position_x = tail_position_x + 1
            else:
                if abs(head_position_x - tail_position_x) == 2:
                    if head_position_y > tail_position_y:
                        tail_position_x = tail_position_x + 1
                        tail_position_y = tail_position_y + 1
                    elif head_position_y < tail_position_y:
                        tail_position_x = tail_position_x + 1
                        tail_position_y = tail_position_y - 1

            tail_visited.append((tail_position_x,tail_position_y))
            print(f"Result: ({head_position_x - tail_position_x}, {head_position_y - tail_position_y})")
            # print(head_position_x,head_position_y,tail_position_x,tail_position_y)

    if direction == "L":
        for motion in range(degree):
            head_position_x = head_position_x - 1
            print(f"Difference: ({head_position_x - tail_position_x}, {head_position_y - tail_position_y})")
            if head_position_y == tail_position_y:
                if abs(head_position_x - tail_position_x) == 2:
                    tail_position_x = tail_position_x - 1
            else:
                if abs(head_position_x - tail_position_x) == 2:
                    if head_position_y > tail_position_y:
                        tail_position_x = tail_position_x - 1
                        tail_position_y = tail_position_y + 1
                    elif head_position_y < tail_position_y:
                        tail_position_x = tail_position_x - 1
                        tail_position_y = tail_position_y - 1
            print(f"Result: ({head_position_x - tail_position_x}, {head_position_y - tail_position_y})")
            tail_visited.append((tail_position_x,tail_position_y))
            # print(head_position_x,head_position_y,tail_position_x,tail_position_y)

    if direction == "U":
        for motion in range(degree):
            head_position_y = head_position_y + 1
            print(f"Difference: ({head_position_x - tail_position_x}, {head_position_y - tail_position_y})")
            if head_position_x == tail_position_x:
                if abs(head_position_y - tail_position_y) == 2:
                    tail_position_y = tail_position_y + 1
            else:
                if abs(head_position_y - tail_position_y) == 2:
                    if head_position_x > tail_position_x:
                        tail_position_x = tail_position_x + 1
                        tail_position_y = tail_position_y + 1
                    elif head_position_x < tail_position_x:
                        tail_position_x = tail_position_x - 1
                        tail_position_y = tail_position_y + 1
            print(f"Result: ({head_position_x - tail_position_x}, {head_position_y - tail_position_y})")
            tail_visited.append((tail_position_x,tail_position_y))
            # print(head_position_x,head_position_y,tail_position_x,tail_position_y)

    if direction == "D":
        for motion in range(degree):
            head_position_y = head_position_y -1
            print(f"Difference: ({head_position_x - tail_position_x}, {head_position_y - tail_position_y})")
            if head_position_x == tail_position_x:
                if abs(head_position_y - tail_position_y) == 2:
                    tail_position_y = tail_position_y - 1
            else:
                if abs(head_position_y - tail_position_y) == 2:
                    if head_position_x > tail_position_x:
                        tail_position_x = tail_position_x + 1
                        tail_position_y = tail_position_y - 1
                    elif head_position_y < tail_position_y:
                        tail_position_x = tail_position_x - 1
                        tail_position_y = tail_position_y - 1
            print(f"Result: ({head_position_x - tail_position_x}, {head_position_y - tail_position_y})")
            tail_visited.append((tail_position_x,tail_position_y))
            # print(head_position_x,head_position_y,tail_position_x,tail_position_y)


print(f"Final Head Position X: {head_position_x}, Position Y: {head_position_y}")
# print(tail_visited)
print(len(tail_visited))

# print(set(tail_visited))
print(len(set(tail_visited)))
