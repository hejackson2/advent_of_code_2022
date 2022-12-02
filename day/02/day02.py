#!/usr/bin/env python
'''
first half:
A = Rock, B = Paper, C = Scissors
X = Rock, Y = Paper, Z = Scissors

single round sore: second column X = 1, Y = 2, z = 3
total round: single round score + win = lost, 3 = draw, win = 6

second half changes:
X = lose, Y = draw, Z = win
'''

import os

strategyGuide = open('day/02/input')
# strategyGuide = ['A Y', 'B X', 'C Z']

# X = Lose = 0, Y = Draw = 3, Z = Win = 6
outcomeScore = {'X': 0, 'Y': 3, 'Z': 6}
choiceScore = {'R': 1, 'P': 2, 'S': 3}

outcomeMatrix = {
    'X': {              # Lose
        'A': 'S',           # Scissors loses to Rock
        'B': 'R',           # Rock loses to Paper
        'C': 'P'            # Paper loses to Scissors
    }, 
    'Y': {              # Draw
        'A': 'R',           # Rock / Rock
        'B': 'P',           # Paper / Paper
        'C': 'S'            # Scissors / Scissors
    },
    'Z': {              # Win
        'A': 'P',           # Paper beats Rock
        'B': 'S',           # Scissors beats Paper
        'C': 'R'            # Rock beats Paper
    }
}

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
    choice = outcomeMatrix[k][j]
    score += choiceScore[choice]

    
    totalScore += score


print(f'total score: {totalScore}')
strategyGuide.close()