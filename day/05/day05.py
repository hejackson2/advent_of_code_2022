#!/usr/bin/env python

# variables
# data = 'day/05/test-input'
# data = 'day/05/test-input-2'
data = 'day/05/input'


def readInput(data):

    # read in files to initial tables
    beginTable = []
    moves = []
    with open(data, 'r') as file:
        for line in file.readlines():

            # we need to keep the whitespace, but get rid of newlines
            line = line.replace('\n', '')

            # skip line between table and moves
            if line == '':
                continue

            # populate moves table
            elif 'move' in line:
                moves.append(line)

            # build beginning table
            else:
                beginTable.append(line)

        beginTable.pop()

    # change moves table to numeric values
    move = []
    for item, line in enumerate(moves):
        move.append(line.split(' '))
        move[item].pop(4)   # remove 'to' before destination column
        move[item].pop(2)   # remove 'from' before starting column
        move[item].pop(0)   # remove 'move' from start

    # convert move to integers
    for x, y in enumerate(move):
        for j, k in enumerate(move[x]):
            move[x][j] = int(move[x][j])


    # covert beginTable to lists of lists of single characters
    newTable = []
    for item, row in enumerate(beginTable):
        newTable.append([])
        for x in range(1, len(row) - 1, 4):
            newTable[item].append(row[x])

    # create a table of columns from newTable
    columns = []
    # go through each column of each row of newTable
    for column in range(len(newTable[0])):

        # go through each row for that column
        columns.append('')
        for row in range(len(newTable)):
            columns[column] += newTable[row][column]

        # reverse string so column (bottom-up) is presented (left-right)
        columns[column] = columns[column][::-1].strip()

    # return columns and move
    return(columns, move)



def parseMoves(columns, moves):
    # parse through moves
    for x, y in enumerate(moves):

        # (q)uantity to move, (s)tarting column, (d)estination column
        q, s, d = moves[x]

        # cycle through {q} moves
        for a in range(q):

            # pull from start
            b = columns[s-1][-1]
            columns[s-1] = columns[s-1][:-1]

            # push to destination
            columns[d-1] += b


    # derive answer as last string from each column
    answer = ''
    for z in columns:
        answer += z[-1]

    
    return(answer)



def parseMoves2(columns, moves):

    # parse through moves
    for x, y in enumerate(moves):

        # (q)uantity to move, (s)tarting column, (d)estination column
        q, s, d = moves[x]

        # pull from start
        b = columns[s-1][-q:]
        columns[s-1] = columns[s-1][:-q]

        # push to destination
        columns[d-1] += b

        answer = ''
        for z in columns:
            if len(z) > 0:
                answer += z[-1]
            else:
                answer += ' '

    # derive answer as last string from each column
    answer = ''
    for z in columns:
        if len(z) > 0:
            answer += z[-1]
        else:
            answer += ' '
    
    return(answer)



def main():
    columns, moves = readInput(data)
    answer = parseMoves(columns, moves)
    print(f'The answer to part one is {answer}')

    columns, moves = readInput(data)
    answer = parseMoves2(columns, moves)
    print(f'The answer to part two is {answer}')


if __name__ == '__main__':
    main()