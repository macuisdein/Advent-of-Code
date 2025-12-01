#!/usr/local/bin/python3

import re

f = open("rules.txt")
input = [f.read().split("\n")]



class Bag:
    def __init__(self,rule):
        self.color = rule.split("bags contain")[0]
        self.name = self.color
        self.contents = ((rule.split("bags contain")[1:]))
        self.contents1 = "Default"
        self.contents2 = "Default"
        self.number1 = 0
        self.number2 = 0
        self.bag1 = ""
        self.bag2 = ""
        # if(len(rule.split)):

        #     self.contents1 = ((rule.split("bags")[1]).split("contain")[1]).split(",")[0]
        #     self.contents2 = ((rule.split("bags")[1]).split("contain")[1]).split(",")[1] 

 
    def processBag(self,contents):
        # print(contents[0].strip())
        contents1=contents[0].strip()
        if "no other" in contents1:
            self.contents1 = "None"
            self.contents2 = "None"
        elif "," in contents1:
            contents2 = contents1.split(",")[1]
            # print(contents1, contents2)
            contents1 = contents1.split(",")[0]
            self.contents1 = contents1
            self.contents2 = contents2[1:]
        else:
            self.contents1 = contents1

    def processContents(self,contents):
        if "None" in self.contents1:
            self.number1 = 0
            self.number2 = 0
        else:
            self.number1 = int(self.contents1.split(" ")[0])
            bag1 = self.contents1.split(" ")[1:3]
            self.bag1 = " "
            self.bag1 = self.bag1.join(bag1)
            # print(self.number1)
            # print(self.bag1)
            if self.contents2 != "Default":
                # print(self.contents2)
                self.number2 = int(self.contents2.split(" ")[0])
                bag2 = self.contents2.split(" ")[1:3]
                self.bag2 = " "
                self.bag2 = self.bag2.join(bag2)
                # print(self.number2)
                # print(self.bag2)
bagList = []
    
for rules in input:
    for rule in rules:
        # print("Evaluating rule: " + rule)
        newBag = Bag(rule)
        if newBag in bagList:
            pass
        else:
            bagList.append(newBag)
        newBag.processBag(newBag.contents)
        newBag.processContents(newBag.contents)
        # print("Contents 1: " + str(newBag.contents1))
        # print("Contents 2: " + str(newBag.contents2))
        totalContents = newBag.number1 + newBag.number2
        # print("Bag: " + newBag.color + " contains: " + str(totalContents) + " bags: "+ str(newBag.number1) + " " + newBag.bag1 + " " + str(newBag.number2) + " " + newBag.bag2)
# print("Bag list = " + str(bagList))

findColor = "shiny gold"

bagDictionary = {}

colorMatches = []
allcolorsMatch = []

for bag in bagList:
    bagDictionary[str(bag.color) + "1"]= bag.bag1
    bagDictionary[str(bag.color) + "2"]= bag.bag2

# print (bagDictionary)
numberColorsMatch = 0
#Find Direct
for key,value in bagDictionary.items():
    if value == findColor:
        numberColorsMatch +=1
        colorMatches.append(key)
        allcolorsMatch.append(key)
# print((allcolorsMatch))
# print(len((allcolorsMatch)))
# print(colorMatches)

# Find parents
while True:
    # print(len(allcolorsMatch))
    # print(allcolorsMatch)
    print(colorMatches)
    for color in colorMatches:
        for key,value in bagDictionary.items():
            if value == color[:-2]:
                print(key)
                numberColorsMatch +=1
                if color[:-2] not in allcolorsMatch:
                    colorMatches.append(key)
                    
                allcolorsMatch.append(key)
                

        colorMatches.remove(color)
    # print(len((colorMatches)))
    # print((colorMatches))

    if len(colorMatches) == 0:
        break
finalColorMatch = []
print((allcolorsMatch))
print(len(set(allcolorsMatch)))
for color in allcolorsMatch:
    finalColorMatch.append(color[:-2])

print(finalColorMatch)
print(len(finalColorMatch))
print(set((finalColorMatch)))
print(len(set(finalColorMatch)))
print(numberColorsMatch)