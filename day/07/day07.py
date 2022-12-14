#!/usr/bin/env python3

import re

data = 'day/07/input'


def cleanInput(data):
    lines = []
    with open(data, 'r') as f:
        for line in f.readlines():
            lines.append(line.strip())

    return lines


def processData(data):
    cwd = []
    dirs = {}

    for line in data:
        # change directory
        m = re.match(r'\$ cd (.*)$', line)
        if m:
            dirName = m.groups()[0]
            
            # go back/up
            if dirName == '..':
                size = dirs[tuple(cwd)]['size']
                cwd.pop()
                dirs[tuple(cwd)]['size'] += int(size)

            else:
                cwd.append(dirName)
                dirs[tuple(cwd)] = {'size': 0}

        # list directory
        m = re.match(r'\$ ls', line)
        if m:
            pass

        # directory name is cwd
        m = re.match(r'^dir (.*)$', line)
        if m:
            pass

        # filename with file size
        m = re.match(r'^(\d+)\s(\w.*)$', line)
        if m:
            size = m.groups()[0]
            file = m.groups()[1]
            dirs[tuple(cwd)]['size'] += int(size)

    # handle adding last set of dirs back to root
    for x in range(len(cwd) - 1, 0, -1):
        dirs[tuple(cwd[:x])]['size'] += dirs[tuple(cwd)]['size']

    return dirs


def calculateSize(dirs, maxSize):
    totalSize = 0
    
    for directory in dirs.keys():
        dSize = dirs[directory]['size']
        # print(f'{directory}: {dSize}')
        if dSize <= maxSize:
            totalSize += dSize

    return totalSize


def partTwo(dirs):

    # calculate size needed
    totalDiskSpace = 70_000_000
    usedSpace = dirs[tuple('/',)]['size']
    remainingSpace = totalDiskSpace - usedSpace
    spaceNeeded = 30_000_000 - remainingSpace
    currentMaxSize = 0

    for directory in dirs.keys():
        dSize = dirs[directory]['size']
        if dSize > spaceNeeded:
            if currentMaxSize == 0:
                currentMaxSize = dSize
            else:
                currentMaxSize = min(dSize,currentMaxSize)
            
    return currentMaxSize


if __name__ == '__main__':
    lines = cleanInput(data)
    dirs = processData(lines)
    print(f'Day 07 - part One: {calculateSize(dirs, 100_000)}')
    print(f'Day 07 - part Two: {partTwo(dirs)}')