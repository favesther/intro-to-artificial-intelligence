'''Farmer_Fox.py
by Xinyi Yang
UWNetID: xyang6
Student number: 1968343

Assignment 2, in CSE 415, Winter 2021.
 
This file contains my problem formulation for the problem of
the Farmer, Fox, Chicken, and Grain.
'''
PROBLEM_NAME ="farmerFox"
PROBLEM_VERSION="1.0"
#<METADATA>
#</METADATA>

#<COMMON_DATA>
#</COMMON_DATA>

#<COMMON_CODE>
F = 0
f = 1
c = 2
g = 3 # array index to access character state
N = 4
codebook={0:'farmer',1:'fox',2:'chicken',3:'grain', 4:'No one'}

LEFT = 0 # same idea for left side of river
RIGHT = 1 # etc.

class State():
    def __init__(self, d=None):
        if d==None:
            d = [0,0,0,0]
        self.d = d

    def __eq__(self, s2):
        if self.d != s2.d: return False
        return True

    def __str__(self):
        # Produces a textual description of a state.
        p = self.d
        txt = "[ "
        for i in range(4):
            if p[i]==0:
                txt += codebook[i] + " "
        txt += "--- "        
        for i in range(4):
            if p[i]==1:
                txt += codebook[i] + " "
        txt += "]"                    
        return txt

    def __hash__(self):
        return (self.__str__()).__hash__()

    def copy(self):
        # Performs anz appropriately deep copy of a state,
        # for use by operators in creating new states.
        news = State({})
        news.d = [self.d[i] for i in [F,f,c,g]]
        return news

    def can_move(self, code):
        '''Tests whether it's legal to move the boat and take
         m missionaries and c cannibals.'''
        p = self.d
        if code!=4 and p[code]!=p[F]: return False
        o=p.copy()
        o[F]=1-o[F]        
        if code!=4: o[code]=1-o[code]
        if o[c]==o[f] and o[F]!=o[c]: return False
        if o[c]==o[g] and o[F]!=o[c]: return False                
        return True


    def move(self, code):
        '''Assuming it's legal to make the move, this computes
         the new state resulting from moving the boat carrying
         m missionaries and c cannibals.'''
        news = self.copy()  # start with a deep copy.
        p = news.d
        p[F] = 1 - p[F]
        if code != 4: p[code] = 1 - p[code]        
        return news

def goal_test(s):
    '''If all characters are on the right, then s is a goal state.'''
    p = s.d
    return (p[F]==1 and p[f]==1 and p[c]==1 and p[g]==1)

def goal_message(s):
    return "Congratulations on successfully guiding the characters across the river!"

class Operator:
    def __init__(self, name, precond, state_transf):
        self.name = name
        self.precond = precond
        self.state_transf = state_transf

    def is_applicable(self, s):
        return self.precond(s)

    def apply(self, s):
        return self.state_transf(s)

# </COMMON_CODE>

# <INITIAL_STATE>
CREATE_INITIAL_STATE = lambda: State(d=[0,0,0,0])
# </INITIAL_STATE>

# <OPERATORS>
combinations = [1,2,3,4]
OPERATORS = [Operator(
    "farmer can go across the river with " + codebook[code],
    lambda s, i=code: s.can_move(i),
    lambda s, i=code: s.move(i))
    for code in combinations]
# </OPERATORS>

# <GOAL_TEST> (optional)
GOAL_TEST = lambda s: goal_test(s)
# </GOAL_TEST>

# <GOAL_MESSAGE_FUNCTION> (optional)
GOAL_MESSAGE_FUNCTION = lambda s: goal_message(s)
# </GOAL_MESSAGE_FUNCTION>