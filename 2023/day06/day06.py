import math
file = open("input2.txt", "r")
lines = file.readlines()
print(f"Length of input is {len(lines)}")

times=[]
distances=[]

for line in lines:
    if "Time" in line:
        time_input = line.split(':')[1]
        times=time_input.split()
    elif "Distance" in line:
        distance_input = line.split(':')[1]
        distances = distance_input.split()

if len(times) != len(distances):
    print(f"We have an error in parsing!")

print(f"Times are {times}")
print(f"Distances are {distances}")

win_count={}

for x in range(len(times)):
    win_count[x] = 0
    speed = 0
    distance = 0
    for y in range(1,int(times[x])):
        # print(f"First time is {y} of {times[x]}")
        speed = y
        distance = speed * (int(times[x]) - y)
        if distance > int(distances[x]):
            # print(f"Distance traveled is {distance}")
            win_count[x] = win_count[x] + 1
print(f"Win count is {win_count}")
print(f"Total win = {math.prod(dict.values(win_count))}")

large_time=''
large_distance=''
for time in times:
    large_time = large_time + time
for distance in distances:
    large_distance = large_distance + distance

print(f"Large time = {large_time}")
print(f"Large_distance = {large_distance}")

large_win_count=0
speed = 0
distance = 0
for y in range(0,int(large_time)):
    # print(f"First time is {y} of {times[x]}")
    speed = y
    distance = speed * (int(large_time) - y)
    if distance > int(large_distance):
        # print(f"Distance traveled is {distance}")
        large_win_count = large_win_count + 1
print(f"Win count is {large_win_count}")