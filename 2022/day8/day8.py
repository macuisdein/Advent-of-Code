#!/usr/bin/env python3

class Tree(object):
    def __init__(self,location,height):
        self.x = location[0]
        self.y = location[1]
        self.height = height
    
    def check_height(self):
        return self.height

    def check_ideal(self):        
        left_value = 0
        for left in reversed(range(0,self.x)):
            if self.height > forrest[self.y][left].check_height():
                left_value = left_value + 1
            elif self.height == forrest[self.y][left].check_height():
                left_value = left_value + 1
                break
            else:
                left_value = left_value + 1
                break
        right_value = 0
        for right in range(self.x+1,99):
            if self.height > forrest[self.y][right].check_height():
                right_value = right_value + 1
            elif self.height == forrest[self.y][right].check_height():
                right_value = right_value + 1
                break
            else:
                right_value = right_value + 1
                break
        up_value = 0
        for up in reversed(range(0,self.y)):
            if self.height > forrest[up][self.x].check_height():
                up_value = up_value + 1
            elif self.height == forrest[up][self.x].check_height():
                up_value = up_value + 1
                break
            else:
                up_value = up_value + 1
                break
        down_value = 0
        for down in range(self.y+1,99):
            if self.height > forrest[down][self.x].check_height():
                down_value = down_value + 1
            elif self.height == forrest[down][self.x].check_height():
                down_value = down_value + 1
                break
            else:
                down_value = down_value + 1
                break
        self.ideal_score = up_value * down_value * left_value * right_value
        return self.ideal_score

    def check_visible(self):
        self.is_visible = False
        self._check_edge()
        if self.is_visible:
            return True
        else:
            self._check_neighbor()
        
        if self.is_visible:
            return True
        else:
            return False

    def _check_edge(self):
        if self.x == 0:
            self.is_visible = True
        elif self.x == 98:
            self.is_visible = True
        elif self.y == 0:
            self.is_visible = True
        elif self.y == 98:
            self.is_visible = True
    
    def _check_neighbor(self):
        for left in reversed(range(0,self.x)):
            if self.height <= forrest[self.y][left].check_height():
                self.is_visible = False
                break
            else:
                self.is_visible = True
                
        if self.is_visible == True:      
            return
        for right in range(self.x+1,99):
            if self.height <= forrest[self.y][right].check_height():
                self.is_visible = False
                break
            else:
                self.is_visible = True
        if self.is_visible == True:
            return
        for up in reversed(range(0,self.y)):
            if self.height <= forrest[up][self.x].check_height():
                self.is_visible = False
                break
            else:
                self.is_visible = True
        if self.is_visible == True:
            return
        for down in range(self.y+1,99):
            if self.height <= forrest[down][self.x].check_height():
                self.is_visible = False
                break
            else:
                self.is_visible = True
            
        if self.is_visible == True:
            return

forrest = [[0 for x in range(99)] for y in range(99)]

file = open("input.txt")
y = 0
for line in file:
    x = 0
    for height in line.strip():
        forrest[y][x] = Tree((x,y),int(height))
        x = x+1
    y = y+1
file.close()

count_of_visible = 0
most_ideal = 0
for y in range(99):
    for x in range(99):
        if forrest[y][x].check_visible():
            count_of_visible = count_of_visible +1
        how_ideal = forrest[y][x].check_ideal()
        if how_ideal > most_ideal:
            most_ideal = how_ideal

print(f"Visible trees = {count_of_visible}")
print(f"Most ideal is score is {most_ideal}")