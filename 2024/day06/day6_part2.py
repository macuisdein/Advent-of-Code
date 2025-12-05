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

def obstacle_in_front(current_position, direction, obstacles):
    y = current_position['y']
    x = current_position['x']
    if direction == "N":
        check = (y - 1, x)
    elif direction == "S":
        check = (y + 1, x)
    elif direction == "W":
        check = (y, x - 1)
    elif direction == "E":
        check = (y, x + 1)
    else:
        raise ValueError(f"Unknown direction {direction}")
    return check in obstacles.values()

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

def advance_guard(current_position, direction, obstacles):
    # If there is something directly in front, turn right (no move).
    # Otherwise, move forward one step.
    if obstacle_in_front(current_position, direction, obstacles):
        # turn right 90 degrees
        if direction == "N":
            direction = "E"
        elif direction == "E":
            direction = "S"
        elif direction == "S":
            direction = "W"
        elif direction == "W":
            direction = "N"
        # do NOT move
        return direction, current_position
    else:
        # move one step forward in the current direction
        if direction == "N":
            current_position = advance_north(current_position)
        elif direction == "S":
            current_position = advance_south(current_position)
        elif direction == "W":
            current_position = advance_west(current_position)
        elif direction == "E":
            current_position = advance_east(current_position)
        return direction, current_position

def count_positions(positions):
	total_positions = len(set(positions))
	return total_positions

lines = []
positions = []
with open('input') as f:
	for line in f:
		line = line.rstrip('\n')
		line_list = []
		line = line.strip()
		for char in line:
			line_list.append(char)
		lines.append(line_list)
		
array_version = np.array(lines)
max_y, max_x = array_version.shape 


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
start_pos, _ = get_starting_point(array_version)
starting_position = (start_pos['y'], start_pos['x'])
positions_visited.discard(starting_position)  # Exclude starting position

found_loop = 0  # Counter for valid loop-causing obstructions

def causes_loop(block_y, block_x):
    # Reset obstacles and add new obstruction
    obstacles = get_obstacles(array_version)
    obstacles[len(obstacles)] = (block_y, block_x)

    current_position, direction = get_starting_point(array_version)

    # Track (y, x, direction) states
    seen_states = set()

    while True:
        state = (current_position['y'], current_position['x'], direction)
        if state in seen_states:
            # We’re repeating the same position *and* facing -> loop
            return True
        seen_states.add(state)

        # Check if next move would leave the map
        if direction == "N" and edge_north(current_position):
            return False
        elif direction == "S" and edge_south(current_position, max_y):
            return False
        elif direction == "W" and edge_west(current_position):
            return False
        elif direction == "E" and edge_east(current_position, max_x):
            return False

        # Otherwise advance the guard one step
        direction, current_position = advance_guard(current_position, direction, obstacles)

for (y, x) in positions_visited:
    if causes_loop(y, x):
        found_loop += 1

print(f"We found {found_loop} valid loop-causing obstructions.")


