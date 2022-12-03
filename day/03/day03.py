#!/usr/bin/env python

import string

# list of letters (https://www.i2tutorials.com/python-program-to-generate-a-list-of-alphabets-in-lowercase/)
lowerCase = list(string.ascii_lowercase)
upperCase = list(string.ascii_uppercase)
priorityList = lowerCase + upperCase

# file = 'day/03/test-input'
file = 'day/03/input'

total = 0

# read through file
with open(file) as f:
    for line in f.readlines():
        line = line.strip()

        firstHalf = line[:len(line) // 2]
        secondHalf = line[len(line) // 2:]

        for c in firstHalf:
            if c in secondHalf:
                # print(f'{c}: {priorityList.index(c) + 1}')
                total += priorityList.index(c) + 1
                break


print(total)