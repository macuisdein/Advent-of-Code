#!/usr/local/bin/python3
treemap = [line.rstrip('\n') for line in open('input')]
maxY = len(treemap)
maxX = len(treemap[0])
print("Max X value is: " + str(maxX))
print("Max Y value is: " + str(maxY))

xcoord = 0
ycoord = 0
countTree = 0

def slopeForward():
    # right three
    global xcoord
    global ycoord
    xcoord += 3

    if (xcoord >= maxX ):
        xcoord = xcoord - maxX

    # down one
    ycoord += 1
    return xcoord, ycoord

def checkIfTree(treemap, xcoord, ycoord):
    istree = False
    print ("Ycoord is " + str(ycoord) + " Xcoord is " + str(xcoord) + " Map says: "+ (treemap[ycoord][xcoord]))
    if (treemap[ycoord][xcoord] == '#'):
        istree = True
        print("Found a tree!")
        return bool(istree)
    elif (treemap[ycoord][xcoord] == '.'):
        istree = False
        return bool(istree)
    else:
        raise Exception('We have an undefined object on map!')


for entry in treemap:
    if checkIfTree(treemap, xcoord, ycoord):
        countTree += 1
    if (ycoord < maxY):
        slopeForward()
    
print("We found " + str(countTree) + " trees")