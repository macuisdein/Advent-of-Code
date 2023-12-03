# /usr/bin/env python3

# Code this time was LONG -- and I saw later that someone did it in 12 lines.
# Oh well. I had trouble with part2. I thought my test cases accounted properly, but it
# wasn't until I saw https://www.reddit.com/r/adventofcode/comments/189rn81/comment/kbt0ry0/ that
# I realized that the test case not considered:
# .8.
# .*.
# 100
# Should be 800 -- I wasn't even "seeing" a gear there.


symbols_we_care = [
    "!",
    "@",
    "#",
    "$",
    "%",
    "^",
    "&",
    "(",
    ")",
    ",",
    "/",
    "|",
    "\\",
    "+",
    "-",
    "=",
]

potential_gear = ["*"]


def check_chars(lines):
    symbol_count = 0
    digit_count = 0
    symbol_location = []
    potential_gear_location = []
    numLines = len(lines)

    for y in range(numLines):
        numCols = len(lines[y])
        row = lines[y]
        for x in range(numCols):
            if row[x] in symbols_we_care:
                symbol_count = symbol_count + 1
                symbol_location.append((y, x))
            elif row[x] in potential_gear:
                symbol_count = symbol_count + 1
                symbol_location.append((y, x))
                potential_gear_location.append((y, x))
            elif row[x].isnumeric():
                digit_count = digit_count + 1
            elif row[x] == ".":
                pass
            elif row[x] == "\n":
                pass
            else:
                print(f"Found strange: {row[x]}")
    print(f"Found {digit_count} digits and {symbol_count} symbols")
    return symbol_location, potential_gear_location


def check_up_left(lines, y, x):
    try:
        if lines[y - 1][x - 1].isnumeric():
            # print(f"Found number {lines[y - 1][x - 1]} above row left from {y,x}")
            return (y - 1, x - 1)
        else:
            return (-1, -1)
    except IndexError:
        return (-1, -1)


def check_up_center(lines, y, x):
    try:
        if lines[y - 1][x].isnumeric():
            # print(f"Found number {lines[y - 1][x]} above row center from {y,x}")
            return (y - 1, x)
        else:
            return (-1, -1)
    except IndexError:
        return (-1, -1)


def check_up_right(lines, y, x):
    try:
        if lines[y - 1][x + 1].isnumeric():
            # print(f"Found number {lines[y - 1][x + 1]} above row right from {y,x}")
            return (y - 1, x + 1)
        else:
            return (-1, -1)
    except IndexError:
        return (-1, -1)


def check_left(lines, y, x):
    try:
        if lines[y][x - 1].isnumeric():
            # print(f"Found number {lines[y][x - 1]} same row left from {y,x}")
            return (y, x - 1)
        else:
            return (-1, -1)
    except IndexError:
        return (-1, -1)


def check_right(lines, y, x):
    try:
        if lines[y][x + 1].isnumeric():
            # print(f"Found number {lines[y][x + 1]} same row right from {y,x}")
            return (y, x + 1)
        else:
            return (-1, -1)
    except IndexError:
        return (-1, -1)


def check_down_left(lines, y, x):
    try:
        if lines[y + 1][x - 1].isnumeric():
            # print(f"Found number {lines[y + 1][x - 1]} below row left from {y,x}")
            return (y + 1, x - 1)
        else:
            return (-1, -1)
    except IndexError:
        return (-1, -1)


def check_down_center(lines, y, x):
    try:
        if lines[y + 1][x].isnumeric():
            # print(f"Found number {lines[y + 1][x]} below row center from {y,x}")
            return (y + 1, x)
        else:
            return (-1, -1)
    except IndexError:
        return (-1, -1)


def check_down_right(lines, y, x):
    try:
        if lines[y + 1][x + 1].isnumeric():
            # print(f"Found number {lines[y + 1][x + 1]} below row right from {y,x}")
            return (y + 1, x + 1)
        else:
            return (-1, -1)
    except IndexError:
        return (-1, -1)


def check_already_found(location, already_found):
    if location in already_found:
        return already_found
    else:
        already_found.append(location)
        return already_found


def find_num_near_symbol(symbol_location, lines):
    already_found = [(-1, -1)]
    for coord in symbol_location:
        y = coord[0]
        x = coord[1]
        uL = check_up_left(lines, y, x)
        already_found = check_already_found(uL, already_found)
        uC = check_up_center(lines, y, x)
        already_found = check_already_found(uC, already_found)
        uR = check_up_right(lines, y, x)
        already_found = check_already_found(uR, already_found)
        l = check_left(lines, y, x)
        already_found = check_already_found(l, already_found)
        r = check_right(lines, y, x)
        already_found = check_already_found(r, already_found)
        dL = check_down_left(lines, y, x)
        already_found = check_already_found(dL, already_found)
        dC = check_down_center(lines, y, x)
        already_found = check_already_found(dC, already_found)
        dR = check_down_right(lines, y, x)
        already_found = check_already_found(dR, already_found)

    # print(already_found)
    return already_found


def check_left_number_extent(lines, y, x):
    while check_left(lines, y, x) != (-1, -1):
        x = x - 1
        # print(f"Changed x value to {x}")
    return x


def check_right_number_extent(lines, y, x):
    while check_right(lines, y, x) != (-1, -1):
        x = x + 1
        # print(f"Changed x value to {x}")
    return x + 1


def find_num_near_gear(symbol_location, lines):
    already_found = []
    # print(symbol_location)
    y = symbol_location[0]
    x = symbol_location[1]
    uL = check_up_left(lines, y, x)
    already_found = check_already_found(uL, already_found)
    uC = check_up_center(lines, y, x)
    already_found = check_already_found(uC, already_found)
    uR = check_up_right(lines, y, x)
    already_found = check_already_found(uR, already_found)
    l = check_left(lines, y, x)
    already_found = check_already_found(l, already_found)
    r = check_right(lines, y, x)
    already_found = check_already_found(r, already_found)
    dL = check_down_left(lines, y, x)
    already_found = check_already_found(dL, already_found)
    dC = check_down_center(lines, y, x)
    already_found = check_already_found(dC, already_found)
    dR = check_down_right(lines, y, x)
    already_found = check_already_found(dR, already_found)
    if (-1, -1) in already_found:
        already_found.remove((-1, -1))
    # print(already_found)

    for pair in already_found:
        if ((pair[0], pair[1] + 1)) in already_found:
            # print(f"Removing {(pair[0], pair[1] + 1)}")
            already_found.remove((pair[0], pair[1] + 1))
            # print(already_found)
            if ((pair[0], pair[1] + 2)) in already_found:
                # print(f"Removing {(pair[0], pair[1] + 2)}")
                already_found.remove((pair[0], pair[1] + 2))
                # print(already_found)

    return already_found


def main():
    input = open("input.txt", "r")
    lines = input.readlines()
    sum_of_schematic = 0

    # Find all the symbols
    symbol_location, potential_gear_location = check_chars(lines)
    # print(f"Location of symbols: {symbol_location}")

    # Find all the numbers that are near a symbol
    numbers_found_at = set(find_num_near_symbol(symbol_location, lines))

    number_range_covered = {}

    # Now that we found all the numbers, we need to know the left/right extant for each
    for location in numbers_found_at:
        y = location[0]
        x = location[1]
        # print(f"Searching Y={y} X={x}")
        if y == -1:
            pass
        elif y in number_range_covered.keys():
            if x in number_range_covered[y]:
                # print(f"Already found {x} in {number_range_covered[y]}")
                # print("\n")
                pass
            else:
                left_most = check_left_number_extent(lines, y, x)
                right_most = check_right_number_extent(lines, y, x)
                # print(f"Row {y} Left={left_most} Right={right_most}")
                # print(lines[y][left_most:right_most])
                number = int(lines[y][left_most:right_most])
                sum_of_schematic = sum_of_schematic + number
                number_range_covered[y] = number_range_covered[y] + list(
                    range(left_most, right_most)
                )
                # print("\n")

        else:
            left_most = check_left_number_extent(lines, y, x)
            right_most = check_right_number_extent(lines, y, x)
            # print(f"Row {y} Left={left_most} Right={right_most}")
            # print(lines[y][left_most:right_most])
            number = int(lines[y][left_most:right_most])
            sum_of_schematic = sum_of_schematic + number
            number_range_covered[y] = list(range(left_most, right_most))
            # print("\n")

    print(f"Sum of schematic = {sum_of_schematic}")
    gear_ration_sum = 0
    for location in potential_gear_location:
        number_near_potential_gear = find_num_near_gear(location, lines)
        # print(f"Testing gear location {location} has length {len(number_near_potential_gear)}")
        if len(number_near_potential_gear) == 2:
            # print(f"We found a gear at {location} with {number_near_potential_gear}")
            numbers = []
            for location in number_near_potential_gear:
                y = location[0]
                x = location[1]
                # print(f"Searching Y={y} X={x}")

                left_most = check_left_number_extent(lines, y, x)
                right_most = check_right_number_extent(lines, y, x)
                # print(f"Row {y} Left={left_most} Right={right_most}")
                # print(lines[y][left_most:right_most])
                number = int(lines[y][left_most:right_most])
                numbers.append(number)
            # print(numbers)
            ratio = numbers[0] * numbers[1]
            gear_ration_sum = gear_ration_sum + ratio

    print(f"Gear ration sum = {gear_ration_sum}")


if __name__ == "__main__":
    main()
