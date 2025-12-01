#!/usr/local/bin/python3

f = open("input.txt")
input = f.readlines()

running25 = []
isValid = False

def testInput(running25,numberToCheck):
    isValid = False
    print(numberToCheck)
    for item in running25:
        for item2 in running25:
            sum = 0
            sum = item + item2
            print("Item1: " + str(item) + " Item2: " + str(item2) + " = " + str(item + item2))
            if (sum == int(numberToCheck)):
                print("I found it " + numberToCheck)
                isValid = True
                return(isValid)
                
            else:
                isValid = False
        if isValid:
            return(isValid)
        else:
            continue

    

for n in range(0,25):
    running25.append(int(input[n].strip("\n")))
    print("Loading: " + input[n].strip("\n"))
    # print (running25)

for n in range(25,len(input)):
    isValid = testInput(running25,input[n])
    if isValid:
        print("Del " + str(running25[0]))
        del running25[0]
        running25.append(int(input[n].strip("\n")))
        continue
    else:
        print("Last valid: " + str(input[n]))
        break

