#!/usr/local/bin/python3
import re

 
# byr (Birth Year)
# iyr (Issue Year)
# eyr (Expiration Year)
# hgt (Height)
# hcl (Hair Color)
# ecl (Eye Color)
# pid (Passport ID)
# cid (Country ID)] 

numberValid = 0
numbshort = 0
numberFailedKey = 0
numberFailedValue = 0

def checkKey(dict, key):
    if key in dict.keys(): 
        return True
    else:
        # print("Failed to find mandatory key: " + key)
        return False

def checkValue(dict, key):
    checkDict = dict
    constraints = {'byr':'[1][9][2-9][0-9]|[2][0][0][0-2]','iyr':'[2][0][1][0-9]|[2][0][2][0]','eyr':'[2][0][2][0-9]|[2][0][3][0]','hgt':'([5][9]|[6][0-9]|[7][0-6])in|([1][5-8][0-9]|[1][9][0-3])cm','hcl':'#[0-9a-f]{6}$','ecl':'amb|blu|brn|gry|grn|hzl|oth','pid':'\d{9}$'}
    value = checkDict.get(key)
    constraint = constraints.get(key)
    if (re.match(constraint,value)):
        # print("Value: " + value + " found valid within " + constraint)
        return True
    else: 
        # print ("Failed validation! " + value + " not within " + key + " " + constraint)
        return False

def checkFields(dict):
    checkfield = dict
    mandatoryFields = ['byr','iyr','eyr','hgt','hcl','ecl','pid']
    for key in mandatoryFields:
        validKey = checkKey(checkfield, key)
        if validKey:
            # print("Checking value of key: " + key)
            validValue = checkValue(checkfield, key)
            if validValue:
                pass
            else:
                global numberFailedValue
                numberFailedValue += 1
                return False
        else:
            global numberFailedKey
            numberFailedKey += 1
            return False
    return True



def checkLegnth(dict):
    checkpass = dict
    if len(checkpass.keys()) < 7:
        # print("Failed! Too short!")
        global numbshort
        numbshort += 1
        return False
    else:
        validFields = checkFields(checkpass)
        if validFields:
            return True
        else:
            return False



def checkValid(dict):
    passport_to_check = dict
    checking = checkLegnth(passport_to_check)
    if checking:
        return True
    return False


with open('input') as f:
    passports = f.read().split("\n\n")
    print("We have " + str(len(passports)) + " passports")
    oneLine = []
    for passport in passports:
        passport = passport.replace("\n", " ")
        passport = passport.split(" ")
        split = []
        for each in passport:
            each = each.split(":")
            split.append(each)
        dictionary = dict(split)
        oneLine.append(dictionary)
        # Finally created a list of dictionaries!!!
    
    i = 0

    for line in oneLine:
        # print("Checking passport # " + str(i))
        isValid = checkValid(line)
        if (isValid == True):
            numberValid += 1
            # print("Counted as valid!")
        i += 1
    
    print("Number short: " + str(numbshort))
    print("Number failed key: " + str(numberFailedKey))
    print("Number failed value: " + str(numberFailedValue))

    print("Sum Failed: " + str(numberFailedKey + numberFailedValue + numbshort))
    print("Valid: " + str(numberValid))
    print("Grand Total: " + str(numberFailedKey + numberFailedValue + numbshort +numberValid))