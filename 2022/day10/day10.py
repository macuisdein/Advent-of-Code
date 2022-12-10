#!/usr/bin/env python3

cycle = 1
register = 1
signal_strength = 0
cycle_check = [20,60,100,140,180,220]
image = []

for item in range(0,250):
    image.append('.')

file = open("input.txt")
for line in file:
    if (cycle % 40 == register) or (cycle % 40 == register +1) or (cycle % 40 == register + 2 ):
        image[cycle] = '#'
    if "noop" in line:
        cycle = cycle + 1
        if cycle in cycle_check:
            signal_strength = signal_strength + (cycle * register)
        
    elif "addx" in line:
        cycle = cycle + 1
        if (cycle % 40 == register) or (cycle % 40 == register +1) or (cycle % 40 == register + 2 ):
            image[cycle] = '#'
        if cycle in cycle_check:
            signal_strength = signal_strength + (cycle * register)
        
        cycle = cycle + 1
        register = register + int(line.split()[1])
        if (cycle % 40 == register) or (cycle % 40 == register +1) or (cycle % 40 == register + 2 ):
            image[cycle] = '#'
        if cycle in cycle_check:
            signal_strength = signal_strength + (cycle * register)
        
print(f"Signal strength = {signal_strength}")

print("".join(image[1:40]))
print("".join(image[41:80]))
print("".join(image[81:120]))
print("".join(image[121:160]))
print("".join(image[161:200]))
print("".join(image[201:240]))
