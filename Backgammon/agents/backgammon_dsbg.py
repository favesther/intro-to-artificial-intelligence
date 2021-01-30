'''
Name(s): Xinyi Yang
UW netid(s): xyang6
'''

from game_engine import genmoves

class BackgammonPlayer:
    def __init__(self):
        self.GenMoveInstance = genmoves.GenMoves()
        # two counters
        self.num_states = 0  # number of states created by the agent
        self.num_cutoffs = 0  # number of alpha-beta cutoffs
        self.max_ply = 3
        self.prune = True # alpha-beta prune variable
        self.function = None
        self.die1 = 1 
        self.die2 = 6


    # returns a string representing a unique nick name for your agent
    def nickname(self):
        # TODO: return a string representation of your UW netid(s)
        return "Panacea"

    # If prune==True, changes the search algorthm from minimax
    # to Alpha-Beta Pruning
    def useAlphaBetaPruning(self, prune=False):
        # TODO: use the prune flag to indiciate that your search
        # should use Alpha-Beta rather than minimax
        self.prune = prune
        self.num_states = 0 # reset counter and cutoffs to 0
        self.num_cutoffs = 0

    # Returns a tuple containing the number explored
    # states as well as the number of cutoffs.
    def statesAndCutoffsCounts(self):
        # TODO: return a tuple containig states and cutoff
        return (self.num_states, self.num_cutoffs)

    # Given a ply, it sets a maximum for how far an agent
    # should go down in the search tree. If maxply==-1,
    # no limit is set
    def setMaxPly(self, maxply=-1):
        # TODO: set the max ply
        self.max_ply = maxply


    # If not None, it update the internal static evaluation
    # function to be func
    def useSpecialStaticEval(self, func):
        # TODO: update your staticEval function appropriately
        self.function = func

    def initialize_move_gen_for_state(self, state, who, die1, die2):
        self.move_generator = self.GenMoveInstance.gen_moves(state, who, die1, die2)
    
    # Given a state and a roll of dice, it returns the best move for
    # the state.whose_move
    def move(self, state, die1=1, die2=6):
        # TODO: return a move for the current state and for the current player.
        # Hint: you can get the current player with state.whose_move
        self.die1 = die1
        self.die2 = die2
        self.initialize_move_gen_for_state(state, state.whose_move, self.die1, self.die2)
        return self.abminimax(state, state.whose_move, -1e10, 1e10,  self.max_ply)[1]


    # Given a state, returns an integer which represents how good the state is
    # for the two players (W and R) -- more positive numbers are good for W
    # while more negative numbers are good for R
    def staticEval(self, state):
        # TODO: return a number for the given state
        # if self.function != None:
        #     return self.function(state)
        
        W = 0
        R = 1
        w_position,r_position=[],[]
        w_distance, r_distance = 0,0
        
        '''on board'''
        # get the position of all the checkers on board
        for i in state.pointLists:
            w_position.append(i.count(W))
            r_position.append(i.count(R))
        
        # compute all the distance
        for i in enumerate(w_position):
            w_distance += (24 - i[0])*i[1] # i[0] ~ index, i[1] ~ number of checkers
        # w_distance is negative
        
        for i in enumerate(r_position):
            r_distance += (i[0] + 1) * i[1]
        # r_distance is positive

        pts = r_distance - w_distance

        '''on bar'''
        # for each, subtract 24 points, to go all over again
        pts += (-24) * state.bar.count(W) 
        pts += 24 * state.bar.count(R)

        '''offs'''
        # for each, add 25 points
        pts += 25 * len(state.white_off)
        pts += (-25) * len(state.red_off) 
        # print ("D分数在这里", pts)
        return pts     
      

    def get_all_moves(self):
        """Uses the mover to generate all legal moves."""
        move_list = []
        done_finding_moves = False
        any_non_pass_moves = False
        while not done_finding_moves:
            try:
                m = next(self.move_generator)    # Gets a (move, state) pair.
                # print("next returns: ",m[0]) # Prints out the move.    For debugging.
                if m[0] != 'p':
                    any_non_pass_moves = True
                    move_list.append(m)    # Add the (move,state) to the list.
            except StopIteration as e:
                done_finding_moves = True
        if not any_non_pass_moves:
            move_list.append(('p', None)) # when pass, state = None
        return move_list    



    def abminimax(self, state, whose_move, alpha, beta, plyLeft):
        if state is None: 
            return 0,'p'
        if plyLeft == 0:
            return self.staticEval(state), None

        self.initialize_move_gen_for_state(state, whose_move, self.die1, self.die2)

        moves = self.get_all_moves()  

        self.num_states += 1      

        if whose_move == 0:
            maxVal = -10e5
            for m in moves:
                if len(moves) == 1: 
                    best_state = m[0]

                val = self.abminimax(m[1], 1-whose_move, alpha, beta, plyLeft-1)[0]
                if val > maxVal:
                    maxVal = val
                    best_state = m[0]

                if self.prune:
                    alpha = max(alpha, maxVal)
                    if beta <= alpha:
                        self.num_cutoffs += 1
                        break
            return maxVal, best_state
        
        else:
            minVal = 10e5
            for m in moves:
                if len(moves) == 1:
                    best_state = m[0]
                val = self.abminimax(m[1], 1-whose_move, alpha, beta,  plyLeft-1)[0]
                
                if val < minVal:
                    minVal = val

                    best_state = m[0]

                if self.prune:
                    beta = min(beta,minVal)
                    if beta <= alpha:
                        self.num_cutoffs += 1
                        break
            return minVal, best_state