#!/usr/bin/env python
'''
single round sore: second column X = 1, Y = 2, z = 3
total round: single round score + win = lost, 3 = draw, win = 6

second half changes:
X = lose, Y = draw, Z = win
'''

import os

strategyGuide = open('day/02/input')
# strategyGuide = ['A Y', 'B X', 'C Z']

outcomeScore = {'X': 0, 'Y': 3, 'Z': 6}
choiceScore = {'R': 1, 'P': 2, 'S': 3}
equivalentChoice = {'A': 'R', 'B': 'P', 'C': 'S'}

totalScore = 0
score = 0

for line in strategyGuide.readlines():
# for line in strategyGuide:
    line = line.strip()
    # j = first player choice
    # k = outcome from game
    j, k = line.split(' ')

    score = 0

    # points for outcomeScore
    score += outcomeScore[k]

    # what choice is needed for outcome
    # draw
    if k == 'Y':
        choice = equivalentChoice[j]
        score += choiceScore[choice]

    # lose
    elif k == 'X':
        # rock, choose scissors to lose
        if j == 'A':
            score += choiceScore['S']

        # paper, choose rock to lose
        elif j == 'B':
            score += choiceScore['R']

        # scissors, choose paper
        elif j == 'C':
            score += choiceScore['S']

    # win
    elif k == 'Z':
        # rock, chose paper
        if j == 'A':
            score += choiceScore['P']

        # paper, choose scissors
        elif j == 'B':
            score += choiceScore['S']

        # scissors, chose rock
        elif j == 'C':
            score += choiceScore['R']

    
    totalScore += score


print(f'total score: {totalScore}')
strategyGuide.close()

 