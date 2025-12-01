#!/usr/local/bin/python3
treemap = [line.rstrip('\n') for line in open('input')]
maxY = len(treemap)
maxX = len(treemap[0])
print("Max X value is: " + str(maxX))
print("Max Y value is: " + str(maxY))

treeProduct = 1

slopeRight = [1,3,5,7,1]
slopeDown = [1,1,1,1,2]
slopes = len(slopeRight)

xcoord = 0
ycoord = 0
countTree = 0

def slopeForward(Right,Down):
    # right three
    global xcoord
    global ycoord
    xcoord += int(Right)

    if (xcoord >= maxX ):
        xcoord = xcoord - maxX

    # down one
    ycoord += int(Down)
    return xcoord, ycoord

def checkIfTree(treemap, xcoord, ycoord):
    istree = False
    #print ("Ycoord is " + str(ycoord) + " Xcoord is " + str(xcoord) + " Map says: "+ (treemap[ycoord][xcoord]))
    if (treemap[ycoord][xcoord] == '#'):
        istree = True
        #print("Found a tree!")
        return bool(istree)
    elif (treemap[ycoord][xcoord] == '.'):
        istree = False
        return bool(istree)
    else:
        raise Exception('We have an undefined object on map!')

for i in range(slopes):
    print ("Iteration: " + str(i))
    Right = slopeRight[i]
    Down = slopeDown[i]
    
    for entry in treemap:
        if checkIfTree(treemap, xcoord, ycoord):
            countTree += 1

        if (ycoord < maxY - Down ):
            slopeForward(Right, Down)
        
    print("We found " + str(countTree) + " trees")
    # Reset to start coords
    xcoord = 0
    ycoord = 0
    treeProduct = treeProduct * countTree
    countTree = 0
print("Product of trees: " + str(treeProduct))