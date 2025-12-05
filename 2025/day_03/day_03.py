#!/usr/bin/env python3

def max_max2_line(line):
    max_line = 0
    second_max_line = 0
    for char in line:
        if int(char) > int(max_line):
            if int(max_line) > int(second_max_line):
                second_max_line = max_line
            max_line = char
        elif int(char) > int(second_max_line):
            second_max_line = char
    return max_line, second_max_line


with open('input','r') as f:
    lines=f.readlines()

total_combinations = []

for line in lines:
    line = line.strip()
    max_line_combinations = []


    max_line, second_max_line = max_max2_line(line)
    
    if line.index(str(max_line)) < len(line) - 1:
        # We can use the max to find biggest combo
        new_line = line[line.index(str(max_line))+1:]
        max_line2, second_max_line2 = max_max2_line(new_line)
        first_combo = max_line + max_line2
    else:
        # We can use the second_max to find biggest combo
        new_line = line[line.index(str(second_max_line))+1:]
        max_line2, second_max_line2 = max_max2_line(new_line)
        first_combo = second_max_line + max_line2
    total_combinations.append(first_combo)
    


print(total_combinations)
total = 0
for combination in total_combinations:
    total = int(combination) + total
print(f"Total is {total}")


# Part 2:
total_combinations = []
with open('input','r') as f:
    lines=f.readlines()



def largest_k_digits(line, k=12):
    result = []
    start = 0
    n = len(line)

    for i in range(k):
        # remaining digits needed after choosing this digit
        remaining_needed = k - (i + 1)

        # window ends such that enough digits remain after
        window_end = n - remaining_needed

        # find max digit between start and window_end (exclusive)
        window = line[start:window_end]
        max_digit = max(window)

        # append that digit
        result.append(max_digit)

        # update start index to the position AFTER the chosen digit
        start = line.index(max_digit, start) + 1

    return "".join(result)


for line in lines:
    line = line.strip()
    max_line_combinations = []

    top_12  = largest_k_digits(line, k=12)
    # print(f'Line {line}')
    # print(f'Top 12: {top_12}')
    total_combinations.append(top_12)



# print(total_combinations)
total = 0
for combination in total_combinations:
    total = int(combination) + total
print(f"Total is {total}")


# Alternate Part 1:
total_combinations = []
with open('input','r') as f:
    lines=f.readlines()

    for line in lines:
        line = line.strip()
        max_line_combinations = []

        top_12  = largest_k_digits(line, k=2)
        # print(f'Line {line}')
        # print(f'Top 12: {top_12}')
        total_combinations.append(top_12)

# print(total_combinations)
total = 0
for combination in total_combinations:
    total = int(combination) + total
print(f"Alternate Total 1 is {total}")