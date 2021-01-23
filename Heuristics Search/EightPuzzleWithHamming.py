'''EightPuzzleWithManhattan.py
by Xinyi Yang
UWNetID: xyang6
Student number: 1968343

Assignment 2, Part 2, in CSE 415, Winter 2021.
 
This file contains my problem formulation for the problem of
the Eight Puzzle with Hamming distance heuristic.
'''

from EightPuzzle import *

goal = [[0,1,2],[3,4,5],[6,7,8]]

def h(s):
  count = 0
  for i in range(3):
    for j in range(3):
      if s.b[i][j]!=goal[i][j]: count+=1

  return count
