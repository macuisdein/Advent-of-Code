#!/usr/bin/env python3

sum = 0
digits = []

input = open("input2.txt", 'r')
lines = input.readlines()

numLines = len(lines)

for x in range(0,numLines):
    rowDigit = list(filter(str.isdigit, lines[x]))
    digits.append(rowDigit)
    firstDigit = rowDigit[0]
    lastDigit = rowDigit[-1]
    rowSum = (firstDigit)+ (lastDigit)
    sum = sum + int(rowSum)
    # print(f"Row {x} digits are: {rowDigit} with the first={firstDigit} and last={lastDigit}. Callibration value is {rowSum}")

print(f"Part 1 sum is {sum}")

# Part 2

part2sum = 0

def convertNum(row):
    length = len(row)
    new_row = row
    x = 0
    while x < length:
        if row[x] == 'o':
            if row[x+1] == 'n':
                if row[x+2] == 'e':
                    new_row = row[0:x+1] + '1' + row[x+2:length]
        elif row[x] == 't':
            if row[x+1] == 'w':
                if row[x+2] == 'o':
                    new_row = row[0:x+1] + '2' + row[x+2:length]
            elif row[x+1] == 'h':
                if row[x+2] == 'r':
                    if row[x+3] == 'e':
                        if row[x+4] == 'e':
                            new_row = row[0:x+1] + '3' + row[x+4:length]
        elif row[x] == 'f':
            if row[x+1] == 'o':
                if row[x+2] == 'u':
                    if row[x+3] == 'r':
                        new_row = row[0:x+1] + '4' + row[x+3:length]
            elif row[x+1] == 'i':
                if row[x+2] == 'v':
                    if row[x+3] == 'e':
                        new_row = row[0:x+1] + '5' + row[x+3:length]
        elif row[x] == 's':
            if row[x+1] == 'i':
                if row[x+2] == 'x':
                    new_row = row[0:x+1] + '6' + row[x+2:length]
            elif row[x+1] == 'e':
                if row[x+2] == 'v':
                    if row[x+3] == 'e':
                        if row[x+4] == 'n':
                            new_row = row[0:x+1] + '7' + row[x+4:length]
        elif row[x] == 'e':
            if row[x+1] == 'i':
                if row[x+2] == 'g':
                    if row[x+3] == 'h':
                        if row[x+4] == 't':
                            new_row = row[0:x+1] + '8' + row[x+4:length]
        elif row[x] == 'n':
            if row[x+1] == 'i':
                if row[x+2] == 'n':
                    if row[x+3] == 'e':
                        new_row = row[0:x+1] + '9' + row[x+3:length]
        x = x + 1
        row = new_row
        length = len(row)

    return new_row

for x in range(0,numLines):
    row = lines[x]
    # print(f"Row {x}: {row}")
    row = convertNum(row)
    # print(f"Row {x}: converted: {row}")
    rowDigit = list(filter(str.isdigit, row))
    digits.append(rowDigit)
    firstDigit = rowDigit[0]
    lastDigit = rowDigit[-1]
    rowSum = (firstDigit)+ (lastDigit)
    part2sum = part2sum + int(rowSum)
    # print(f"Row {x} digits are: {rowDigit} with the first={firstDigit} and last={lastDigit}. Callibration value is {rowSum}")
    # print("\n")

print(f"Part 2 sum is {part2sum}")
