0

import time

class Gamem:
    MINIMAX = 0
    ALPHABETA=1
    HUMAN=2
    AI=3
    size=0
    winSize=0
    def __init__(self, recommend = True):
        
	    self.initialize_game()
	    self.recommend = recommend
		
    def initialize_game(self):
	    self.current_state = [['.','.','.'],
							  ['.','.','.'],
							  ['.','.','.']]
		# Player X always plays first
	    self.player_turn = 'X'
		
		
    def initialize_game(self):
	    self.current_state = [['.','.','.'],
							  ['.','.','.'],
							  ['.','.','.']]
		# Player X always plays first
	    self.player_turn = 'X'
    def draw_board(self):
	    print()
	    for y in range(0, self.size):
		    for x in range(0, self.size):
			    print(F'{self.current_state[x][y]}', end="")
		    print()
	    print()
    def is_valid(self, px, py):
	    if px < 0 or px > 2 or py < 0 or py > 2 :
		    return False
	    elif self.current_state[px][py] != '.':
		    return False
	    else:
		    return True
    def is_end(self):
        for i in range(0,self.size):
            for j in range(0,self.size):
                #win in rows
                if i<self.size-(self.winSize-1):
                    for x in range(0,self.winSize-2):
                        if(self.current_state[i+x][j]!=self.current_state[i+x+1][j]):
                            break
                    return self.current_state[i][j]
                elif j<self.size-(self.winSize-1):
                    for x in range(0,self.winSize-2):
                        if(self.current_state[i][j+x]!=self.current_state[i][j+x+1]):
                            break
                    return self.current_state[i][j]
                elif i<self.size-(self.winSize-1) and  j<self.size-(self.winSize-1):
                    for x in range(0,self.winSize-2):
                        if(self.current_state[i+x][j+x]!=self.current_state[i+x+1][j+x+1]):
                            break
                        return self.current_state[i][j]
                elif j>self.winSize-2 and i<self.size-(self.winSize-1):
                    for x in range(0,self.winSize-2):
                        if(self.current_state[i-x][j+x]!=self.current_state[i+x-1][j+x]):
                            break
                        return self.current_state[i][j]
        for i in range(0,self.size):
            for j in range(0,self.size):
                if self.current_state[i][j]=='.':
                    return None
        return '.'
    def check_end(self):
        self.result=self.is_end()
        if self.result!=None:
            if self.result=='X':
                print("The winner is X!")
            elif self.result=='O':
                print("The winner is O!")
            elif self.result=='.':
                print("It's a tie.")
            self.initialize_game()
        return self.result
    def input_move(self):
	    while True:
		    print(F'Player {self.player_turn}, enter your move:')
		    px = int(input('enter the x coordinate: '))
		    py = int(input('enter the y coordinate: '))
		    if self.is_valid(px, py):
			    return (px,py)
		    else:
			    print('The move is not valid! Try again.')

    def switch_player(self):
	    if self.player_turn == 'X':
		    self.player_turn = 'O'
	    elif self.player_turn == 'O':
		    self.player_turn = 'X'
	    return self.player_turn
    def e1(self):
        value=0
        numOfO=0
        numOfX=0
        x=None
        y=None
        result=self.is_end()
        if result=="X":
            return -10000
        elif result=="O":
            return 10000
        elif result==".":
            return 0
        for i in range(0,self.size):
            numOfO=0
            numOfX=0
            for j in range(0,self.size):
                if self.current_state[i][j]=='X':
                    numOfX+=1
                elif self.current_state[i][j]=='O':
                    numOfO+=1
            value+=(numOfO-numOfX)
        for i in range(0,self.size):
            numOfX=0
            numOfO=0
            for j in range(0,self.size):
                if self.current_state[j][i]=='X':
                    numOfX+=1
                elif self.current_state[j][i]=='O':
                    numOfO+=1
            value+=(numOfO-numOfX)
        return value
    def e2(self):
        value=0
        x=None
        y=None
        rowlist=[]
        columnlist=[]
        rightDialist=[]
        leftDialist=[] 
        row=[]
        column=[]
        rightDia=[]
        leftDia
        result=self.is_end()
        if result=="X":
            return -10**self.winSize
        elif result=="O":
            return 10**self.winSize
        elif result==".":
            return 0
        
       