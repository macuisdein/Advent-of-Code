#!/usr/local/bin/python3
lineList = [line.rstrip('\n') for line in open('day_input')]
validPassword = 0
for line in lineList:
    numberRange, character, password = line.split(' ')
    character = character.strip(':')
    password = password.strip()

    number1, number2 = numberRange.split('-')
    number1=int(number1)
    number2=int(number2)

    count = 0
    for letter in password:
        if (letter == character):
            count += 1
    print("Character: " + character + " found " + str(count) + " times." )
    if (number1 <= count <= number2):
        validPassword += 1
        print("Password: " + password + " is valid because .")
    else:
        print("Password: " + password + " is not valid.")
print (validPassword)



