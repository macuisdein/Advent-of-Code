#!/usr/local/bin/python3

 
# byr (Birth Year)
# iyr (Issue Year)
# eyr (Expiration Year)
# hgt (Height)
# hcl (Hair Color)
# ecl (Eye Color)
# pid (Passport ID)
# cid (Country ID)] 

numberValid = 0

def checkKey(dict, key):
    if key in dict.keys(): 
        return True
    else:
        print("Failed to find mandatory key: " + key)
        return False

def checkFields(dict):
    checkfield = dict
    mandatoryFields = ['byr','iyr','eyr','hgt','hcl','ecl','pid']
    for key in mandatoryFields:
        validKey = checkKey(checkfield, key)
        if not validKey:
            return False
    return True



def checkLegnth(dict):
    checkpass = dict
    if len(checkpass.keys()) < 7:
        print("Failed! Too short!")
        return False
    else:
        validFields = checkFields(checkpass)
        if not validFields:
            return False
        return True



def checkValid(dict):
    passport_to_check = dict
    checking = checkLegnth(passport_to_check)
    if not checking:
        return False
    return True


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

    for line in oneLine:
        isValid = checkValid(line)
        if (isValid == True):
            print("Looks valid!")
            numberValid += 1
    print(numberValid)

