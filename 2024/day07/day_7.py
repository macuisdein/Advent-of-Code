test_values = []
remaining_numbers_list = []
from itertools import product
count = 0

def generate_test_equations(remaining_numbers, test_value):
    results = []
    for length in range(2, len(remaining_numbers) + 1):
        for i in range(len(remaining_numbers) - length + 1):
            subset = remaining_numbers[i:i+length]
            for ops in product(["+", "*"], repeat=length - 1):
                equation = str(subset[0])
                for i, op in enumerate(ops):
                    equation += f" {op} {subset[i + 1]}"
                    # print(equation)
                    # print(eval(equation))
                try:
                    if eval(equation) == int(test_value):
                        results.append(equation)
                except Exception as e:
                    continue
            # break
    return results

with open('sample.txt') as f:
    for line in f:
        test_value = line.split(':')[0]
        test_value = test_value.strip()
        test_values.append(test_value)
        remaining_numbers = line.split(':')[1]
        remaining_numbers = remaining_numbers.strip()
        remaining_numbers = remaining_numbers.split(' ')
        remaining_numbers_list.append(remaining_numbers)

for x in range(0,len(test_values)):
    # print(remaining_numbers_list[x],test_values[x])
    results = generate_test_equations(remaining_numbers_list[x],test_values[x])
    if len(results) > 0:
        count = count + 1

print(count)


    
