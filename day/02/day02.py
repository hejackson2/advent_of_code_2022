#!/usr/bin/env python
'''
single round sore: second column X = 1, Y = 2, z = 3
total round: single round score + win = lost, 3 = draw, win = 6
'''

import os

strategyGuide = open('day/02/input')

choiceScore = {'X': 1, 'Y': 2, 'Z': 3}
equivalentChoice = {'A': 'X', 'B': 'Y', 'C': 'Z'}

totalScore = 0
score = 0

for line in strategyGuide.readlines():
    line = line.strip()
    # j = first player choice
    # k = second player response
    j, k = line.split(' ')

    score = 0

    # points for choice
    score += choiceScore[k]

    # points for outcome
    if equivalentChoice[j] == k:        # draw
        score += 3

    # Rock vs
    elif j == 'A':
        # paper
        if k == 'Y':
            score += 6
        # scissors
        elif k == 'Z':
            score += 0

    # Paper vs
    elif j == 'B':
        # rock
        if k == 'X':
            score += 0
        # scissors
        elif k == 'Z':
            score += 6

    # Scissors vs
    elif j == 'C':
        # rock
        if k == 'X':
            score += 6
        # paper
        elif k == 'Y':
            score += 0


    # update totalScore
    totalScore += score


print(f'total score: {totalScore}')
strategyGuide.close()

 