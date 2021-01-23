'''EightPuzzleWithManhattan.py
by Xinyi Yang
UWNetID: xyang6
Student number: 1968343

Assignment 2, Part 2, in CSE 415, Winter 2021.
 
This file contains my problem formulation for the problem of
the Eight Puzzle with Manhattan distance heuristic.
'''

from EightPuzzle import *

goal = [[0,1,2],[3,4,5],[6,7,8]]

def h(s):
    count = 0
    for i in range(3):
        for j in range(3):
            for index, row in enumerate(goal):
                if s.b[i][j] in row and s.b[i][j]!=0:
                    count = count+abs(j-row.index(s.b[i][j]))+abs(i-index)

    return count
