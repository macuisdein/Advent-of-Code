import numpy as np
import sys

starting_point = []


def edge_east(current_position, max_x):
	if current_position['x'] +1 >= max_x:
		return True
		
def edge_west(current_position):
	if current_position['x'] -1 < 0:
		return True
		
def edge_south(current_position, max_y):
	if current_position['y'] +1 >= max_y:
		return True

def edge_north(current_position):
	if current_position['y'] -1 < 0:
		return True

def get_starting_point(np_version):
	position = {}
	y,x = np.where(np_version == '^')
	direction = 'N'
	position['x'] = int(x[0])
	position['y'] = int(y[0])
	return position, direction 

def get_obstacles(np_version):
	y,x = np.where(np_version == '#')
	y = y.tolist()
	x = x.tolist()
	obstacles = {}
	for item in range(0,len(x)):
		obstacles[item] = (y[item],x[item])
	return obstacles

def advance_north(current_position):
	# Advanced north is to change y - 1
	current_position['y'] = current_position['y'] -1
	return current_position

def advance_south(current_position):
	# Advanced south is to change y + 1
	current_position['y'] = current_position['y'] +1
	return current_position

def advance_west (current_position):
	# Advanced west is to change x + 1
	current_position['x'] = current_position['x'] -1
	return current_position

def advance_east (current_position):
	# Advanced west is to change x - 1
	current_position['x'] = current_position['x'] +1
	return current_position

def look_north(current_position, obstacles):
	# Take the current position and see if we need to turn
	if (current_position['y'] - 1, current_position['x']) in obstacles.values():
		return "E"
	else:
		return "N"

def look_south(current_position, obstacles):
	# Take the current position and see if we need to turn
	if (current_position['y'] + 1, current_position['x']) in obstacles.values():
		return "W"
	else:
		return "S"
		
		
def look_east(current_position, obstacles):
	# Take the current position and see if we need to turn
	if (current_position['y'], current_position['x'] + 1) in obstacles.values():
		return "S"
	else:
		return "E"
		
				
def look_west(current_position, obstacles):
	# Take the current position and see if we need to turn
	if (current_position['y'],current_position['x'] - 1) in obstacles.values():
		return "N"
	else:
		return "W"								

def advance_guard(current_position, direction, obstacles):
	if direction == "N":
		current_position = advance_north(current_position)
		direction = look_north(current_position, obstacles)
		#print(f"Direction is now {direction}")
	elif direction == "S":
		current_position = advance_south(current_position)
		direction = look_south(current_position, obstacles)
		#print(f"Direction is now {direction}")
	elif direction == "W":
		current_position = advance_west(current_position)
		direction = look_west(current_position, obstacles)
		#print(f"Direction is now {direction}")
	elif direction == "E":
		current_position = advance_east(current_position)
		direction = look_east(current_position, obstacles)
		#print(f"Direction is now {direction}")
	return direction, current_position

def count_positions(positions):
	total_positions = len(set(positions))
	return total_positions

lines = []
positions = []
with open('input.py') as f:
	for line in f:
		line_list = []
		max_x = len(line)
		line = line.strip()
		for char in line:
			line_list.append(char)
		lines.append(line_list)
	max_y = len(line_list)
		
array_version = np.array(lines)


current_position, direction = get_starting_point(array_version)
positions.append((current_position['y'], current_position['x']))
#print(positions)
obstacles = get_obstacles(array_version)

print(f"Starting point is {current_position}")

print(f"Obstacles are {obstacles}")

max_count_steps = 0
count_steps = 0
while True:
	count_steps = count_steps + 1
	if count_steps > max_count_steps:
		max_count_steps = count_steps
	#print(f"Current position: {current_position}\t Direction: {direction}")
	if direction == 'N':
		if edge_north(current_position):
			#print(f"End of march {direction}")
			break
		else:
			direction, current_position = advance_guard(current_position, direction, obstacles)
			positions.append((current_position['y'], current_position['x']))
			continue
	elif direction == "S":
		if edge_south(current_position, max_y):
			#print(f"End of march {direction}")
			break
		else:
			direction, current_position = advance_guard(current_position, direction, obstacles)
			positions.append((current_position['y'], current_position['x']))
			continue
	elif direction == "W":
		if edge_west(current_position):
			#print(f"End of march {direction}")
			break
		else:
			direction, current_position = advance_guard(current_position, direction, obstacles)
			positions.append((current_position['y'], current_position['x']))
			continue
	elif direction == "E":
		if edge_east(current_position, max_x):
			#print(f"End of march {direction}")
			break
		else:
			direction, current_position = advance_guard(current_position, direction, obstacles)
			positions.append((current_position['y'], current_position['x']))
			continue

print(f"Count of positions: {count_positions(positions)}")
print(f"Number of steps: {count_steps}")
print(f"Max count steps: {max_count_steps}")

# Part 2

positions_visited = set(positions)
starting_position = (current_position['y'], current_position['x'])
positions_visited.discard(starting_position)

found_loop = 0

for position in positions_visited:
    visited_states = set()
    obstacles = get_obstacles(array_version)
    obstacles[len(obstacles)] = position  # Add new obstruction

    current_position, direction = get_starting_point(array_version)
    count_steps = 0
    while True:
        state = (current_position['y'], current_position['x'], direction)
        if state in visited_states:
            found_loop += 1
            break
        visited_states.add(state)

        count_steps += 1
        if count_steps > 4 * max_count_steps:  # Optional: safeguard against infinite loops
            break

        if direction == "N" and edge_north(current_position):
            break
        elif direction == "S" and edge_south(current_position, max_y):
            break
        elif direction == "W" and edge_west(current_position):
            break
        elif direction == "E" and edge_east(current_position, max_x):
            break

        direction, current_position = advance_guard(current_position, direction, obstacles)

print(f"We found {found_loop} loops")
