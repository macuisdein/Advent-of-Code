import numpy as np

def check_rolls(position, lines):
    pass

all_lines = []

with open('input', 'r') as f:
    lines = f.readlines()

for line in lines:
    line_list = []
    line = line.strip()
    for char in line:
        line_list.append(char)
    all_lines.append(line_list)

numpy_array = np.array(all_lines)

rows, cols = numpy_array.shape

forklift_accessible_rolls = 0

for r in range(rows):
    for c in range(cols):
        current_value = numpy_array[r, c]
        # print(f"Value at ({r}, {c}): {current_value}")
        if current_value == '@':
            # print(f"We found a roll {current_value} at ({r}, {c}) ")

            # Define offsets for surrounding values (8 neighbors)
            neighbor_offsets = [
                (-1, -1), (-1, 0), (-1, 1),
                (0, -1),           (0, 1),
                (1, -1), (1, 0), (1, 1)
            ]
            number_of_rolls_around = 0
            # print("  Surrounding values:")
            for dr, dc in neighbor_offsets:
                nr, nc = r + dr, c + dc  # Neighbor row and column

                # Check if neighbor coordinates are within array bounds
                if 0 <= nr < rows and 0 <= nc < cols:
                    neighbor_value = numpy_array[nr, nc]
                    if neighbor_value == '@':
                        # print(f"    Neighbor at ({nr}, {nc}): {neighbor_value} is a roll.")
                        number_of_rolls_around = number_of_rolls_around + 1
                else:
                    pass
                    # print(f"    Neighbor at ({nr}, {nc}): Out of bounds")
            if number_of_rolls_around < 4:
                # print(f"We can use ({r}, {c})")
                forklift_accessible_rolls = forklift_accessible_rolls + 1

print(f"We have {forklift_accessible_rolls} forklift accessible rolls")

# Part 2

numpy_array = np.array(all_lines)
forklift_accessible_rolls = 0
rows, cols = numpy_array.shape

def check_roll(rows, cols, numpy_array, forklift_accessible_rolls):
    values_of_rolls = []
    for r in range(rows):
        for c in range(cols):
            current_value = numpy_array[r, c]
            # print(f"Value at ({r}, {c}): {current_value}")
            if current_value == '@':
                # print(f"We found a roll {current_value} at ({r}, {c}) ")

                # Define offsets for surrounding values (8 neighbors)
                neighbor_offsets = [
                    (-1, -1), (-1, 0), (-1, 1),
                    (0, -1),           (0, 1),
                    (1, -1), (1, 0), (1, 1)
                ]
                number_of_rolls_around = 0
                # print("  Surrounding values:")
                for dr, dc in neighbor_offsets:
                    nr, nc = r + dr, c + dc  # Neighbor row and column

                    # Check if neighbor coordinates are within array bounds
                    if 0 <= nr < rows and 0 <= nc < cols:
                        neighbor_value = numpy_array[nr, nc]
                        if neighbor_value == '@':
                            # print(f"    Neighbor at ({nr}, {nc}): {neighbor_value} is a roll.")
                            number_of_rolls_around = number_of_rolls_around + 1
                    else:
                        pass
                        # print(f"    Neighbor at ({nr}, {nc}): Out of bounds")
                if number_of_rolls_around < 4:
                    # print(f"We can use ({r}, {c})")
                    forklift_accessible_rolls = forklift_accessible_rolls + 1
                    values_of_rolls.append((r,c))
    return forklift_accessible_rolls, values_of_rolls

def remove_rolls(numpy_array, values_of_rolls):
    for value in values_of_rolls:
        numpy_array[value] = 'x'

forklift_accessible_rolls, values_of_rolls = check_roll(rows, cols, numpy_array, forklift_accessible_rolls)

while len(values_of_rolls) > 0:
    remove_rolls(numpy_array, values_of_rolls)
    forklift_accessible_rolls, values_of_rolls = check_roll(rows, cols, numpy_array, forklift_accessible_rolls)

print(f"We have {forklift_accessible_rolls} forklift accessible rolls")