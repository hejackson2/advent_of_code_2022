#!/usr/bin/env python

# initial variables
data = 'day/04/input'

## Part One
total = 0
# read through data
with open(data) as file:
    for line in file.readlines():
        line = line.strip()

        # split into two range strings
        rangeList = line.split(',')

        # create string for each range
        rangeStrings = ['', '']
        for item, string in enumerate(rangeList):
            startHour = int(string.split('-')[0])
            endHour = int(string.split('-')[1])

            # create new string with all hours inclusive
            for hour in range(startHour, endHour + 1):
                rangeStrings[item] += ',' + str(hour)

        # add ending to prevent incorrect matches
        for item, string in enumerate(rangeStrings):
            rangeStrings[item] += ','

        # check if either are included in the other
        if rangeStrings[0] in rangeStrings[1] or \
            rangeStrings[1] in rangeStrings[0]:
            total += 1

print(f'part one total: {total}')


## part two
total = 0

with open(data) as file:
    for line in file.readlines():
        line = line.strip()

        # split into two range strings
        rangeList = line.split(',')

        # get startHour and endHour for each section
        rangeHours = []
        for item, string in enumerate(rangeList):
            startHour = int(string.split('-')[0])
            endHour = int(string.split('-')[1])

            rangeHours.append(startHour)
            rangeHours.append(endHour)

        overlap = False
        # first side
            # lower value in range of second side?
            # higher value in range of second side?
        for v in rangeHours[:2]:
            if v in range(rangeHours[2], rangeHours[3] + 1):
                overlap = True
                break

        # second side
            # lower value in range of second side?
            # higher value in range of second side?
        for v in rangeHours[2:]:
            if v in range(rangeHours[0], rangeHours[1] + 1):
                overlap = True
                break

        if overlap == True:
            total += 1

print(f'part two total: {total}')


        
