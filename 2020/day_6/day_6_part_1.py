#!/usr/local/bin/python3
f = open("input.txt")
count = 0
questionaires = [f.read().split("\n\n")]
for group in questionaires:
    answers=[]
    for person in group:
        answers.append(person)
    for answer in answers:
        answer = (answer.replace("\n", ""))
        print(len(sorted(set(answer))))
        count = count + len(sorted(set(answer)))
print(count)