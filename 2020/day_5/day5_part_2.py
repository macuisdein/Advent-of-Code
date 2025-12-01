#!/usr/local/bin/python3
boardingPass = [line.rstrip('\n') for line in open('input')]

start = 0
end = 0
maxSeatID = 0
allseats = []
def upper(start,end):
    makehalf = (end - start) * 0.5
    start = start + round(makehalf)
    return start, end

def lower(start,end):
    makehalf = (end - start)  * 0.5
    end = start + int(makehalf)
    return start, end

def newRow(start,end):
    start = 0
    end = 127
    return start,end

def newSeat(start,end):
    start = 0
    end = 7
    return start,end


for passes in boardingPass:
    rows = passes[0:7]
    start,end = newRow(start,end)
    for char in rows:
        if char == 'F':
            start,end = lower(start,end)
        elif char == 'B':
            start,end = upper(start,end)
    row = end
    seats = passes[7:10]
    start,end = newSeat(start,end)
    for char in seats:
        if char == 'L':
            start,end = lower(start,end)
        elif char == 'R':
            start,end = upper(start,end)
    column = end
    seatID = (row * 8) + column
    allseats.append(seatID)
    if seatID > maxSeatID:
        maxSeatID = seatID
     
    print("Row: " + rows + " = " + str(row) + " Column: " + seats + " = " + str(column) + " Seat ID: " + str(seatID))

print ("Max seat ID = " + str(maxSeatID))
myseat = 0
allseats.sort()
print(allseats)
for neighboor in allseats:
    if (neighboor + 2) in allseats:
        if (neighboor +1) not in allseats:
            myseat = neighboor + 1
print ("My seat ID = " + str(myseat))