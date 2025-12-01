def is_all_descending(row):
	desc_row = row.copy()
	desc_row.sort(reverse=True)
	if row == desc_row:
		return True
	else:
		return False

def is_all_ascending(row):
	asc_row = row.copy()
	asc_row.sort()
	if row == asc_row:
		return True
	else:
		return False

def safe_gap(number1, number2):
	gap = abs(int(number1) - int(number2))
	if gap > 3:
		return False
	elif gap == 0:
		return False
	else:
		if gap <= 3:
			return True

def all_safe_gap(row):
	for number in range(0,len(row) - 1):
		if safe_gap(row[number], row[number+1]):
			pass
		else:
			return False
	return True


# Part 2
def remove_a_part(row):
	for index in range(0,len(row)):
		row_removed = row.copy()
		del row_removed[index]
		if is_all_descending(row_removed) == True:
			if all_safe_gap(row_removed) == True:
				return row[index]
		elif is_all_ascending(row_removed) == True:
			if all_safe_gap(row_removed) == True:
				return row[index]
	return False
				

lines = []
safe_lines = 0
not_safe_lines = 0
part_2_safe = 0

with open("input.py") as f:
	for line in f:
		new_line = line.split(' ')
		number_line = list(map(int, new_line))
		lines.append(number_line)

print(f"Number of lines {len(lines)}")

for line in lines:
	print(line)
	if is_all_ascending(line) == True:
		if all_safe_gap(line):
			safe_lines = safe_lines + 1
			continue
		else:
			not_safe_lines = not_safe_lines + 1
	if is_all_descending(line) == True:
		if all_safe_gap(line):
			safe_lines = safe_lines + 1
			continue
		else:
			not_safe_lines = not_safe_lines + 1
	
	not_safe_lines = not_safe_lines + 1
	print(f"We need to try to save {line}")
	item = remove_a_part(line)
	if item:
		print(f"We saved {line} by removing {item}!")
		part_2_safe = part_2_safe + 1
	else:
		print(f"We could not save {line}")
print(f"The number of safe lines is {safe_lines}")
print(f"The number of unsafe lines is {not_safe_lines}")
print(f"The sum of {safe_lines} and {not_safe_lines} = {safe_lines + not_safe_lines}")
print(f"We saved {part_2_safe} lines so Part 2 answer is {part_2_safe + safe_lines}")


