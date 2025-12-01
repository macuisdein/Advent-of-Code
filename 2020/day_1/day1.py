#!/usr/local/bin/python3
lineList = [line.rstrip('\n') for line in open('input')]
intList =[]
for string in lineList:
    intList.append(int(string))

answer = 0
for number in intList:
    for number2 in intList:
        if (number + number2 == 2020):
            answer = number * number2 
print(answer)
