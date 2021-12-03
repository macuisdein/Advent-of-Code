#!/usr/local/opt/python@3.10/bin/python3

# We are piloting our submarine and have directions 'forward' 'down' and 'up' - 
# let's add 'backward' just in case.

# For part 2, all we had to do was add the item "aim" and change what the commands do.


class Submarine(object):
    depth = 0
    horizontal = 0
    aim = 0
    position = [horizontal,depth,aim]


    def __init__(self, horizontal, depth, aim):
        Submarine.horizontal = horizontal
        Submarine.depth = depth
        Submarine.aim = aim
        Submarine.position = [self.horizontal,self.depth]
    
    def forward(self,value):
        Submarine.horizontal = Submarine.horizontal + value
        Submarine.depth = (value * Submarine.aim) + Submarine.depth
        Submarine.position = [Submarine.horizontal,Submarine.depth,Submarine.aim]
    
    def backward(self,value):
        Submarine.horizontal = Submarine.horizontal - value
        Submarine.position = [Submarine.horizontal,Submarine.depth,Submarine.aim]
    
    def down(self,value):
        Submarine.aim = Submarine.aim + value
        Submarine.position = [Submarine.horizontal,Submarine.depth,Submarine.aim]
    
    def up(self,value):
        Submarine.aim = Submarine.aim - value
        Submarine.position = [Submarine.horizontal,Submarine.depth,Submarine.aim]


# Get a new Submarine:
realSubmarine = Submarine(0,0,0)

# Now let's see what we have to do to get our instructions:
# Open the File
f = open('2021/Day2/input.txt', 'r')

# Each line should be a string separating a direction and an integer value

for line in f:
    
    command = line.split(" ")[0]
    value = int(line.split(" ")[1])

    if command == "forward":
        realSubmarine.forward(value)
    elif command == "up":
        realSubmarine.up(value)
    elif command == "down":
        realSubmarine.down(value)
    elif command == "backward":
        realSubmarine.backward(value)
    else:
        print("Sir, We have a problem!! Unknown command!")
        exit(1)

    # print("After: " + command + str(value) + " our New position: " + str(realSubmarine.position))

# Now we proccessed our commands, tell us where we are:

print("realSubmarine position: " + str(realSubmarine.position))
print("Product of position: " + str(realSubmarine.position[0] * realSubmarine.position[1]))