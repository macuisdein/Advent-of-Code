#!/usr/bin/env python3
invalids = []

def chunk_list_loop(lst, chunk_size):
    """Splits a sequence into equally sized chunks using a loop and slicing."""
    chunks = []
    for i in range(0, len(lst), chunk_size):
        chunks.append(lst[i:i + chunk_size])
    return chunks

with open('input.txt', 'r') as f:
    lines = f.readlines()
    for line in lines:
        pairs = line.split(',')
        for pair in pairs:
            start = pair.split('-')[0]
            stop = pair.split('-')[1]
            for item in range(int(start), int(stop)+ 1):
                item = str(item)
                length = len(item)
                if length %2 == 0:
                    half = int(length / 2)
                    first = item[:half]
                    second = item[half:]
                    if first == second:
                        invalids.append(int(item))

total = 0
for item in invalids:
    total = item + total
# print(f"Invalids are: {invalids}")
print(f"The total is {total}")

# Part 2
invalids_2 = []
with open('input.txt', 'r') as f:
    lines = f.readlines()
    for line in lines:
        pairs = line.split(',')
        for pair in pairs:
            start = pair.split('-')[0]
            stop = pair.split('-')[1]
            for item in range(int(start), int(stop)+ 1):
                item = str(item).strip()
                length = len(item)
                # print(f"Item {item } has length {length}")
                for l in range(1,length + 1):
                    test_item = []
                    # print(f"Trying with length {l}")
                    test_item = chunk_list_loop(item, l )
                    # print(test_item)
                    # print(f'The test item is {test_item}')
                    if (len(set(test_item)) == 1) and (len(test_item) > 1):
                        print(f"{item} = {test_item} ")
                        invalids_2.append(int(item))
                        continue

total = 0
invalids_2 = set(invalids_2)
for item in invalids_2:
    total = item + total
print(f"Invalids are: {invalids_2}")
print(f"The Part 2 total is {total}")