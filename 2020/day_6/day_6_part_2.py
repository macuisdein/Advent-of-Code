#!/usr/local/bin/python3
from collections import Counter
f = open("input.txt")
count = 0
questionaires = [f.read().split("\n\n")]
groupCount=0
personCount = 0

total_answersTrue = 0

for groups in questionaires:
    answers=[]
    #groupCount += 1
    #print("Group count is: " + str(groupCount))
    personCount = 0
    for group in groups:
        groupCount += 1
        group = group.split("\n")
        print("Group is " + str(group))
        groupList = []
        for answer in group:
            for item in answer:
                groupList.append(item)
        print("Group list is: " + str(groupList))
        groupSet = set(groupList)
        for item in groupSet:
            if groupList.count(item) == len(group):
                total_answersTrue = total_answersTrue + 1
                print("Added: to the total")
        #print(z)
        print("Group count is: " + str(len(group)))
        print("\n")
        personCount = 0
        #for person in group:
        #    personCount += 1
        #    print("Person " + str(personCount) +" is " + person)
print (total_answersTrue)