#!/usr/local/bin/python3

f = open("instructions.txt")
input = f.readlines()

currentLineNum = 0
accum = 0
nextLineNum = 0
runalready = []

def run(currentLineNum):
    global runalready,accum
    if currentLineNum not in runalready:
        nextLineNum, accum = decode(currentLineNum,accum)
        print (nextLineNum, accum)
        print(runalready)
        return nextLineNum
    else:
        return -1

def decode(currentLineNum,accum):
    nextLineNum = 0
    currentLine= input[currentLineNum]
    interpretted = currentLine.split(" ")
    if interpretted[0].startswith('nop'):
        execute = "none"
        accum = accum
        nextLineNum = currentLineNum + 1
    elif interpretted[0].startswith('acc'):
        execute = "Accumulator"
        accum = accum + int(interpretted[1])
        nextLineNum = currentLineNum + 1
    elif interpretted[0].startswith('jmp'):
        execute = "Jump Instruction"
        accum = accum
        nextLineNum = currentLineNum + int(interpretted[1])
    else:
        print("Error")
    
    global runalready
    runalready.append(currentLineNum)
    
    return (nextLineNum,accum)



while True:
    currentLineNum = run(currentLineNum)
    if currentLineNum == -1:
        break
print(accum)