#!/usr/bin/env python

import string

# list of letters (https://www.i2tutorials.com/python-program-to-generate-a-list-of-alphabets-in-lowercase/)
lowerCase = list(string.ascii_lowercase)
upperCase = list(string.ascii_uppercase)
priorityList = lowerCase + upperCase

# file = 'day/03/test-input'
file = 'day/03/input'
# file = 'day/03/rucksack_items.txt'

total = 0

# read the data
with open(file) as f:
    lines = f.readlines()
    for line in lines:
        lines[lines.index(line)] = line.strip()

    # get groups of 3
    for y in range(len(lines) // 3):
        a = []
        for x in range(3):
            a.append(lines.pop(0))

        # search through list a for commonalities
        badgePriority = 0
        for c in a[0]:
            if c in a[1] and c in a[2]:
                total += priorityList.index(c) + 1
                badgePriority = priorityList.index(c) + 1
                break    

print(total)