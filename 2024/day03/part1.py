import re


running_sum = 0
running_sum2 = 0

def find_valid_mul(line):
	matches = re.findall(r"mul\(\d{1,3},\d{1,3}\)", line)
	return matches

def do_multiplication(mul):
	number = re.findall(r"\d{1,3}",mul)
	result = int(number[0]) * int(number[1])
	return result

def part_2(line):
	running_sum2 = 0
	commands = re.findall("mul\(\d{1,3},\d{1,3}\)|do\(\)|don't\(\)",line)
	return commands

def calculate_part_2(commands):
	run = 0
	enabled_commands = []
	running_sum2 = 0
	enabled = True
	for command in commands:
		if enabled and "mul" in command:
			print(f"Enabled command {command}")
			enabled_commands.append(command)
		elif "mul" in command and enabled == False:
			print(f"Disabled command {command}")
			continue
		elif "don't()" in command:
			print("We are now disabled")
			enabled = False
		elif "do()" in command:
			print("We are now enabled")
			enabled = True
	print(f"Run {run} Enabled commands: {enabled_commands}")
	print(f"Run {run} All commands: {commands}")
	for mul in enabled_commands:
		mul = mul.strip()
		result = do_multiplication(mul)
		running_sum2 = result + running_sum2
	return running_sum2

with open("input.py") as f:
	enabled_commands = []
	part_2_sum = 0
	for line in f:
		matches = find_valid_mul(line)
		for mul in matches:
			mul = mul.strip()
			result = do_multiplication(mul)
			running_sum = result + running_sum
		part2_commands = part_2(line)
		enabled_commands = enabled_commands + part2_commands
	print(f"Part 2 commands {enabled_commands}")
	part_2_sum = calculate_part_2(enabled_commands)

print(matches)
print(f"Part1: {running_sum}")
print(f"Part2: {part_2_sum}")


