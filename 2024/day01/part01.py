list_one = []
list_two = []
ordered_list_one = []
ordered_list_two = []
differece_list = []
sum_of_difference = 0

with open("input.py") as f:
	for line in f:
		list_one.append(int(line.split()[0]))
		list_two.append(int(line.split()[1]))

ordered_list_one = list_one
ordered_list_two = list_two

ordered_list_one.sort()
ordered_list_two.sort()



for x in range(0, len(ordered_list_one)):
	difference = abs(ordered_list_one[x] - ordered_list_two[x])
	differece_list.append(difference)
	sum_of_difference = sum_of_difference + difference

print(f"Part One: Sum of difference is {sum_of_difference}")

multiplicand_list = []
multiplicand_sum = 0

for number in list_one:
	multiple = number * list_two.count(number)
	multiplicand_list.append(multiple)
	multiplicand_sum = multiplicand_sum + multiple

print(f"Part Two: Sum of multiplicand is {multiplicand_sum}")

  
	

