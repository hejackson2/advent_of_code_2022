#!/usr/bin/env python

# data = 'day/08/test-input'
data = 'day/08/input'


def readData(data):
    grid = []
    with open(data, 'r') as f:
        for row, line in enumerate(f.readlines()):
            line = line.strip()
            
            # create a new list for each row
            grid.append([])

            # create a separate entry for each letter in each line
            for letter in line:
                grid[row].append(letter)

    # grid[row][col]
    return grid



def checkVisibility(r,c, grid):

    visible = True

    # top to row
    fromTheTop = []
    topVisible = True
    for y in range(r):
        fromTheTop.append(grid[y][c])
        if grid[y][c] >= grid[r][c]:
            topVisible = False
            break
        
    # row to bottom
    toTheBottom = []
    bottomVisible = True
    for y in range(r+1, len(grid)):
        toTheBottom.append(grid[y][c])
        if grid[y][c] >= grid[r][c]:
            bottomVisible = False
            break

    # left to column
    leftVisible = True
    fromTheLeft = grid[r][:c]
    for x in fromTheLeft:
        if x >= grid[r][c]:
            leftVisible = False
            break

    # column to right
    rightVisible = True
    toTheRight = grid[r][c + 1:]
    for x in toTheRight:
        if x >= grid[r][c]:
            rightVisible = False
            break

    if (
        topVisible == False and
        bottomVisible == False and
        leftVisible  == False and
        rightVisible == False
    ):
        return False

    else:
        return True



def visibleCount(visible):
    count = 0
    for row in visible:
        for col in row:
            if col == 'T':
                count += 1

    return count
            


def partOne(grid):
    # get edges
    right = len(grid[0]) - 1
    bottom = len(grid) - 1

    # visibility grid: T = visibile, F = not-visible
    visible = []

    # walk the grid, every column in every row
    for r, row in enumerate(grid):
        # create new row in visible
        visible.append([])

        for c, col in enumerate(row):
            
            # handle top row, all visible
            if r == 0:
                visible[r].append('T')

            # handle bottom row, all visible
            elif r == right:
                visible[r].append('T')

            # handle left most column, all visible
            elif c == 0:
                visible[r].append('T')

            elif c == bottom:
                visible[r].append('T')

            else:
                # testing value
                if checkVisibility(r, c, grid) == True:
                    visible[r].append('T')
                else:
                    visible[r].append('F')

    return visible
        



if __name__ == '__main__':
    grid = readData(data)
    visible = partOne(grid)
    print(visibleCount(visible))

