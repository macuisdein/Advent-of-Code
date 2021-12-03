#!/usr/local/opt/python@3.10/bin/python3

# We are piloting our submarine and have directions 'forward' 'down' and 'up' - 
# let's add 'backward' just in case.



class Submarine(object):
    depth = 0
    horizontal = 0
    position = [horizontal,depth]


    def __init__(self, horizontal, depth):
        Submarine.horizontal = horizontal
        Submarine.depth = depth
        Submarine.position = [self.horizontal,self.depth]
    
    def forward(self,value):
        Submarine.horizontal = Submarine.horizontal + value
        Submarine.position = [Submarine.horizontal,Submarine.depth]
    
    def backward(self,value):
        Submarine.horizontal = Submarine.horizontal - value
        Submarine.position = [Submarine.horizontal,Submarine.depth]
    
    def down(self,value):
        Submarine.depth = Submarine.depth + value
        Submarine.position = [Submarine.horizontal,Submarine.depth]
    
    def up(self,value):
        Submarine.depth = Submarine.depth - value
        Submarine.position = [Submarine.horizontal,Submarine.depth]

# Let's test our submarine movement:
myTestSubmarine = Submarine(0,0)
myTestSubmarine.forward(2)
myTestSubmarine.down(2)
myTestSubmarine.up(1)


# As long as our movement is corrent, we should be at [2,1]
assert myTestSubmarine.position == [2,1]

# If not at [2,1], uncomment to see where we are:
# print("Test Submarine position now: " + str(myTestSubmarine.position))

# Get a new Submarine:
realSubmarine = Submarine(0,0)

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

# Now we proccessed our commands, tell us where we are:

print("realSubmarine position: " + str(realSubmarine.position))
print("Product of position: " + str(realSubmarine.position[0] * realSubmarine.position[1]))