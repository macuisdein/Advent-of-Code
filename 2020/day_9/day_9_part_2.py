#!/usr/local/bin/python3

f = open("test_input.txt")
input = f.readlines()

running25 = []
isValid = False
invalid = 0
invalidPlace = 0

def testInput(running25,numberToCheck):
    isValid = False
    # print(numberToCheck)
    for item in running25:
        for item2 in running25:
            sum = 0
            sum = int(item) + int(item2)
            # print("Item1: " + str(item) + " Item2: " + str(item2) + " = " + str(item + item2))
            if (sum == int(numberToCheck)):
                # print("I found it " + numberToCheck)
                isValid = True
                return(isValid)
                
            else:
                isValid = False
        if isValid:
            return(isValid)
        else:
            continue

    

for n in range(0,5):
    running25.append(int(input[n].strip("\n")))
    print("Loading: " + input[n].strip("\n"))
    # print (running25)

for n in range(5,len(input)):
    isValid = testInput(running25,input[n])
    if isValid:
        # print("Del " + str(running25[0]))
        del running25[0]
        running25.append(int(input[n].strip("\n")))
        continue
    else:
        print("First invalid: " + str(input[n]))
        invalid = input[n]
        invalidPlace = n
        break

sum = 0
first = 0
last = 0
for number in range(0, invalidPlace):
    sum = 0
    sum = sum + int(input[number])
    while (sum < int(invalid) and (last < invalidPlace)):
        first = number
        last = last + 1
        sum = sum + int(input[last])
        print(sum)
        if sum == int(invalid):
            print(input[first],input[last])
            print("Sum: " + str(int(input[first]) + int(input[last])))
            break
        else:
            continue
