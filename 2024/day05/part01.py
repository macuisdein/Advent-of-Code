def check_valid(update, rules):
	for rule in rules:
		#print(f"Checking rule {rule}")
		try:
			if update.index(rule[0]) > update.index(rule[1]):
				return False
			else:
				continue
		except ValueError:
			#print("Rule not found")
			continue
	return True

def fix_valid(update, rules):
	for rule in rules:
		#print(f"Checking rule {rule}")
		try:
			if update.index(rule[0]) > update.index(rule[1]):
				update[update.index(rule[0])], update[update.index(rule[1])] = update[update.index(rule[1])], update[update.index(rule[0])]
			else:
				continue
		except ValueError:
			#print("Rule not found")
			continue
	return update
	
	
rules = []
updates = []
valid_updates = []
broken_updates = []
middle_sum = 0
fixed_updates = []
fixed_middle_sum = 0

with open('input.py') as f:
	for line in f:
		if '|' in line:
			line = line.strip()
			line = line.split('|')
			rules.append(line)
		elif ',' in line:
			line = line.strip()
			line = line.split(',')
			updates.append(line)



for update in updates:
	if check_valid(update,rules):
		valid_updates.append(update)
	else:
		broken_updates.append(update)

print(f"Valid updates: {valid_updates}")

for update in valid_updates:
	middle = len(update) / 2
	middle_sum = middle_sum + int(update[int(middle)])

print(f"Sum of middle {middle_sum}")

for update in broken_updates:
	print(update)
	while check_valid(update, rules) != True:
		update = fix_valid(update, rules)
	print(update)
	fixed_updates.append(update)

for update in fixed_updates:
	middle = len(update) / 2
	#print(middle)
	fixed_middle_sum = fixed_middle_sum + int(update[int(middle)])

print(f"Sum of fixed middle {fixed_middle_sum}")


