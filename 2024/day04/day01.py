import numpy as np


def check_north(x,y,location,array_version,value,depth, max_y,max_x):
	check_value = y[location] - depth
	if check_value < 0:
		return False
	if array_version[check_value][x[location]] == value:
		return True
	else:
		return False
	
def check_south(x,y,location,array_version,value,depth, max_y,max_x):
	check_value = y[location] + depth
	if check_value > max_y:
		return False
	if array_version[check_value][x[location]] == value:
		return True
	else:
		return False

def check_east(x,y,location,array_version,value,depth, max_y,max_x):
	check_value = x[location] + depth
	if check_value > max_x:
		return False
	if array_version[y[location]][check_value] == value:
		return True
	else:
		return False
	
def check_west(x,y,location,array_version,value,depth, max_y,max_x):
	check_value = x[location] - depth
	if check_value < 0:
		return False
	if array_version[y[location]][check_value] == value:
		return True
	else:
		return False
	
def check_north_west(x,y,location,array_version,value,depth, max_y,max_x):
	check_value = y[location] - depth
	check_value2 = x[location] - depth
	if check_value < 0:
		return False
	if check_value2 < 0:
		return False
	if array_version[check_value][check_value2] == value:
		return True
	else:
		return False

def check_north_east(x,y,location,array_version,value,depth, max_y,max_x):
	check_value = y[location] - depth
	check_value2 = x[location] + depth
	if check_value < 0:
		return False
	if check_value2 > max_x:
		return False
	if array_version[check_value][check_value2] == value:
		return True
	else:
		return False

def check_south_east(x,y,location,array_version,value,depth, max_y,max_x):
	check_value = y[location] + depth
	check_value2 = x[location] + depth
	if check_value > max_y:
		return False
	if check_value2 > max_x:
		return False
	if array_version[check_value][check_value2] == value:
		return True
	else:
		return False

def check_south_west(x,y,location,array_version,value,depth, max_y,max_x):
	check_value = y[location] + depth
	check_value2 = x[location] - depth
	if check_value > max_y:
		return False
	if check_value2 < 0:
		return False
	if array_version[check_value][check_value2] == value:
		return True
	else:
		return False

full_list = []
max_x = 0
max_y = 0
count_of_xmas = 0

with open('input.py') as f:
	for line in f:
		max_y = max_y + 1
		line = line.strip()
		max_x = len(line)
		line_list = []
		for char in line:
			line_list.append(char)
		full_list.append(line_list)

array_version = np.array(full_list)

y,x = np.where(array_version == 'X')


#print(f"Found X at {y[0],x[0]}")
max_x = max_x -1
max_y = max_y -1
#print(f"Max Y {max_y}")
#print(f"Max X {max_x}")
#print(f"Length of X: {len(x)}")
#print(f"Length of Y: {len(y)}")

for location in range(0,len(x)):
	#print(f"Checking {(x[location],y[location])} for 'M'")
	if check_east(x,y,location,array_version,"M", 1, max_y,max_x):
		#print(f"Found M at {y[location],x[location]}" )
		if check_east(x,y,location,array_version,"A", 2, max_y,max_x):
			#print(f"Found A at {x[location],y[location]}" )
			if check_east(x,y,location,array_version,"S", 3, max_y,max_x):
				print(f"Found XMAS east from {y[location],x[location]}" )
				count_of_xmas = count_of_xmas + 1
	if check_west(x,y,location,array_version,"M", 1, max_y,max_x):
		#print(f"Found M at {x[location],y[location]}" )
		if check_west(x,y,location,array_version,"A", 2, max_y,max_x):
			if check_west(x,y,location,array_version,"S", 3, max_y,max_x):
				print(f"Found XMAS west at {y[location],x[location]}" )
				count_of_xmas = count_of_xmas + 1
	if check_north(x,y,location,array_version,"M", 1, max_y,max_x):
		if check_north(x,y,location,array_version,"A", 2, max_y,max_x):
			if check_north(x,y,location,array_version,"S",3, max_y,max_x):
				print(f"Found XMAS north at {y[location],x[location]}" )
				count_of_xmas = count_of_xmas + 1
	if check_south(x,y,location,array_version,"M",1, max_y,max_x):
		if check_south(x,y,location,array_version,"A",2, max_y,max_x):
			if check_south(x,y,location,array_version,"S",3, max_y,max_x):
				print(f"Found XMAS south at {y[location],x[location]}" )
				count_of_xmas = count_of_xmas + 1
	if check_south_west(x,y,location,array_version,"M",1, max_y,max_x):
		if check_south_west(x,y,location,array_version,"A",2, max_y,max_x):
			if check_south_west(x,y,location,array_version,"S",3, max_y,max_x):
				print(f"Found XMAS south_west at {y[location],x[location]}" )
				count_of_xmas = count_of_xmas + 1
	if check_north_west(x,y,location,array_version,"M",1, max_y,max_x):
		if check_north_west(x,y,location,array_version,"A",2, max_y,max_x):
			if check_north_west(x,y,location,array_version,"S",3, max_y,max_x):
				print(f"Found XMAS north_west at {y[location],x[location]}" )
				count_of_xmas = count_of_xmas + 1
	if check_north_east(x,y,location,array_version,"M",1, max_y,max_x):
		if check_north_east(x,y,location,array_version,"A",2, max_y,max_x):
			if check_north_east(x,y,location,array_version,"S",3, max_y,max_x):
				print(f"Found XMAS north_east at {y[location],x[location]}" )
				count_of_xmas = count_of_xmas + 1
	if check_south_east(x,y,location,array_version,"M",1, max_y,max_x):
		if check_south_east(x,y,location,array_version,"A",2, max_y,max_x):
			if check_south_east(x,y,location,array_version,"S",3, max_y,max_x):
				print(f"Found XMAS south_east at {y[location],x[location]}" )
				count_of_xmas = count_of_xmas + 1
	
print(f"Count of XMAS = {count_of_xmas}")


# Part 2
# Now we need to find the A locations and check for M & S
count_of_mas =0
y,x = np.where(array_version == 'A')

for location in range(0,len(x)):
	#print(f"Checking {(x[location],y[location])} for 'M'")
	if check_north_east(x,y,location,array_version,"M", 1, max_y,max_x):
		if check_south_west(x,y,location,array_version,"S", 1, max_y,max_x):
			if check_north_west(x,y,location,array_version,"M", 1, max_y,max_x):
				if check_south_east(x,y,location,array_version,"S", 1, max_y,max_x):
					count_of_mas = count_of_mas + 1
			if check_north_west(x,y,location,array_version,"S", 1, max_y,max_x):
				if check_south_east(x,y,location,array_version,"M", 1, max_y,max_x):
					count_of_mas = count_of_mas + 1
	if check_north_east(x,y,location,array_version,"S", 1, max_y,max_x):
		if check_south_west(x,y,location,array_version,"M", 1, max_y,max_x):
			if check_north_west(x,y,location,array_version,"M", 1, max_y,max_x):
				if check_south_east(x,y,location,array_version,"S", 1, max_y,max_x):
					count_of_mas = count_of_mas + 1
			if check_north_west(x,y,location,array_version,"S", 1, max_y,max_x):
				if check_south_east(x,y,location,array_version,"M", 1, max_y,max_x):
					count_of_mas = count_of_mas + 1
print(f"Count of MAS = {count_of_mas}")
