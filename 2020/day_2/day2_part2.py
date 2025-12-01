#!/usr/local/bin/python3
lineList = [line.rstrip('\n') for line in open('day_input')]
validPassword = 0
for line in lineList:
    numberRange, character, password = line.split(' ')
    character = character.strip(':')
    password = password.strip()

    number1, number2 = numberRange.split('-')
    number1=int(number1) - 1
    number2=int(number2) - 1

    count = 0
    def charcheck(word):
        return [char for char in word]

    passwordList = charcheck(password)
    if (passwordList[number1] == character) or (passwordList[number2] == character):
        if (passwordList[number1] != passwordList[number2]):
            validPassword += 1
            print("Password: " + password + " is valid .")
    else:
        print("Password: " + password + " is not valid.")
print (validPassword)



