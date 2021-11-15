0

import time
import random

class Game:
    MINIMAX = 0
    ALPHABETA = 1
    HUMAN = 2
    AI = 3
    size = 0
    winSize = 0
    numOfHeuristics=0
    currentHeuristics=0
    depth=0

    def __init__(self, recommend=True):

        self.initialize_game()
        self.recommend = recommend



    def initialize_game(self):
        self.current_state = []
        # Player X always plays first
        self.player_turn = 'X'
    def createBoard(self, n):
        for i in range(0,n):
            list=[]
            for j in range(0,n):
               list.append('.')
            self.current_state.append(list)


    def draw_board(self):
        print()
        for y in range(0, self.size):
            for x in range(0, self.size):
                print(F'{self.current_state[x][y]}', end="")
            print()
        print()

    def is_valid(self, px, py):
        if px < 0 or px > 2 or py < 0 or py > 2:
            return False
        elif self.current_state[px][py] != '.':
            return False
        else:
            return True

    def is_end(self):
        for i in range(0, self.size):
            for j in range(0, self.size):
                # win in rows
                if i < self.size - (self.winSize - 1):
                    for x in range(0, self.winSize - 2):
                        if (self.current_state[i + x][j] != self.current_state[i + x + 1][j]):
                            break
                        else:
                            if x == 4:
                                return self.current_state[i][j]
                            continue

                elif j < self.size - (self.winSize - 1):
                    for x in range(0, self.winSize - 2):
                        if (self.current_state[i][j + x] != self.current_state[i][j + x + 1]):
                            break
                        else:
                            if x == 4:
                                return self.current_state[i][j]
                            continue

                elif i < self.size - (self.winSize - 1) and j < self.size - (self.winSize - 1):
                    for x in range(0, self.winSize - 2):
                        if (self.current_state[i + x][j + x] != self.current_state[i + x + 1][j + x + 1]):
                            break
                        else:
                            if x == 4:
                                return self.current_state[i][j]
                            continue

                elif j > self.winSize - 2 and i < self.size - (self.winSize - 1):
                    for x in range(0, self.winSize - 2):
                        if (self.current_state[i - x][j + x] != self.current_state[i + x - 1][j + x]):
                            break
                        else:
                            if x == 4:
                                return self.current_state[i][j]
                            continue

        for i in range(0, self.size):
            for j in range(0, self.size):
                if self.current_state[i][j] == '.':
                    return None
        return '.'

    def check_end(self):
        self.result = self.is_end()
        if self.result != None:
            if self.result == 'X':
                print("The winner is X!")
            elif self.result == 'O':
                print("The winner is O!")
            elif self.result == '.':
                print("It's a tie.")
            self.initialize_game()
        return self.result

    def input_move(self):
        while True:
            print(F'Player {self.player_turn}, enter your move:')
            px = input('enter the x coordinate in letters: ')
            px.lower()
            orderNum = ord(px) - 97
            while (orderNum > self.n - 1):
                px = int(input('Warning! Invalid Number please enter it agian.'))
                orderNum = ord(px) - 97
            px = orderNum
            py = int(input('enter the y coordinate: '))
            if self.is_valid(px, py):
                return (px, py)
            else:
                print('The move is not valid! Try again.')


    def switch_player(self):
        if self.player_turn == 'X':
            self.player_turn = 'O'
        elif self.player_turn == 'O':
            self.player_turn = 'X'
        return self.player_turn

    def e1(self):
        self.numOfHeuristics+=1
        value = 0
        result = self.is_end()
        if result == "X":
            return -10000
        elif result == "O":
            return 10000
        elif result == ".":
            return 0
        for i in range(0, self.size):
            numOfO = 0
            numOfX = 0
            for j in range(0, self.size):
                if self.current_state[i][j] == 'X':
                    numOfX += 1
                elif self.current_state[i][j] == 'O':
                    numOfO += 1
            value += (numOfO - numOfX)
        for i in range(0, self.size):
            numOfX = 0
            numOfO = 0
            for j in range(0, self.size):
                if self.current_state[j][i] == 'X':
                    numOfX += 1
                elif self.current_state[j][i] == 'O':
                    numOfO += 1
            value += (numOfO - numOfX)
        return value

    def e2(self):
        self.numOfHeuristics += 1
        value = 0
        x = None
        y = None
        count = 0
        recordState = '.'
        result = self.is_end()
        if result == "X":
            return -10 ** self.winSize
        elif result == "O":
            return 10 ** self.winSize
        elif result == ".":
            return 0
        # row

        for i in range(0, self.size):
            for j in range(0, self.size):
                if (self.current_state[i][j] == 'X' and recordState == 'X'):
                    recordState = 'X'
                    count += 1
                elif (self.current_state[i][j] == 'O' and recordState == 'O'):
                    recordState = 'O'
                    count += 1
                else:
                    if recordState == 'X' and (self.current_state[i][j] != recordState or j == self.size - 1):
                        value -= 10 ** count
                        recordState = self.current_state[i][j]
                    elif recordState == 'O' and (self.current_state[i][j] != recordState or j == self.size - 1):
                        value += 10 ** count
                        recordState = self.current_state[i][j]
                    else:
                        recordState = self.current_state[i][j]

                    count = 0

        count = 0
        recordState = '.'
        # column
        for i in range(0, self.size):
            for j in range(0, self.size):
                if (self.current_state[j][i] == 'X' and recordState == 'X'):
                    recordState = 'X'
                    count += 1
                elif (self.current_state[j][i] == 'O' and recordState == 'O'):
                    recordState = 'O'
                    count += 1
                else:
                    if recordState == 'X' and (self.current_state[j][i] != recordState or j == self.size - 1):
                        value -= 10 ** count
                        recordState = self.current_state[j][i]
                    elif recordState == 'O' and (self.current_state[j][i] != recordState or j == self.size - 1):
                        value += 10 ** count
                        recordState = self.current_state[j][i]
                    else:
                        recordState = self.current_state[j][i]
                    count = 0
        # right diagonal
        count = 0
        recordState = '.'
        # upper half
        for i in range(0, self.size):
            for x in range(0, self.size - i):
                if (self.current_state[x][i + x] == 'X' and recordState == 'X'):
                    recordState = 'X'
                    count += 1
                elif (self.current_state[x][i + x] == 'O' and recordState == 'O'):
                    recordState = 'O'
                    count += 1
                else:
                    if recordState == 'X' and (self.current_state[x][i + x] != recordState or x == self.size - i - 1):
                        value -= 10 ** count
                        recordState = self.current_state[x][i + x]
                    elif recordState == 'O' and (self.current_state[x][i + x] != recordState or x == self.size - i - 1):
                        value += 10 ** count
                        recordState = self.current_state[x][i + x]
                    else:
                        recordState = self.current_state[x][i + x]
                    count = 0
        count = 0
        recordState = '.'
        # lower half
        for i in range(1, self.size):  # because 0 has already been counted in upper dialogue
            for x in range(0, self.size - i):
                if (self.current_state[i + x][x] == 'X' and recordState == 'X'):
                    recordState = 'X'
                    count += 1
                elif (self.current_state[i + x][x] == 'O' and recordState == 'O'):
                    recordState = 'O'
                    count += 1
                else:
                    if recordState == 'X' and (self.current_state[i + x][x] != recordState or x == self.size - i - 1):
                        value -= 10 ** count
                        recordState = self.current_state[i + x][x]
                    elif recordState == 'O' and (self.current_state[i + x][x] != recordState or x == self.size - i - 1):
                        value += 10 ** count
                        recordState = self.current_state[i + x][x]
                    else:
                        recordState = self.current_state[i + x][x]
                    count = 0
        count = 0
        recordState = '.'

        # left diagonal
        # upper half
        for i in range(0, self.size):
            for x in range(0, i + 1):
                if (self.current_state[i - x][x] == 'X' and recordState == 'X'):
                    recordState = 'X'
                    count += 1
                elif (self.current_state[i - x][x] == 'O' and recordState == 'O'):
                    recordState = 'O'
                    count += 1
                else:
                    if recordState == 'X' and (self.current_state[i - x][x] != recordState or x == i):
                        value -= 10 ** count
                        recordState = self.current_state[i - x][x]
                    elif recordState == 'O' and (self.current_state[i - x][x] != recordState or x == i):
                        value += 10 ** count
                        recordState = self.current_state[i - x][x]
                    else:
                        recordState = self.current_state[i - x][x]
                    count = 0
        count = 0
        recordState = '.'
        # lower half
        for i in range(0, self.size):
            for x in range(0, self.size - i):
                if (self.current_state[x + i][self.size - 1 - x] == 'X' and recordState == 'X'):
                    recordState = 'X'
                    count += 1
                elif (self.current_state[x + i][self.size - 1 - x] == 'O' and recordState == 'O'):
                    recordState = 'O'
                    count += 1
                else:
                    if recordState == 'X' and (self.current_state[x + i][self.size - 1 - x] != recordState or x == i):
                        value -= 10 ** count
                        recordState = self.current_state[x + i][self.size - 1 - x]
                    elif recordState == 'O' and (self.current_state[x + i][self.size - 1 - x] != recordState or x == i):
                        value += 10 ** count
                        recordState = self.current_state[x + i][self.size - 1 - x]
                    else:
                        recordState = self.current_state[x + i][self.size - 1 - x]
                    count = 0
        return value
    def minimax(self,depth,useE2,time, max=False):
        self.depth+=1
        startTime=time.time()
        value=10**(self.winSize+1)
        if max:
            value=-10**(self.winSize+1)
        x = None
        y = None
        result = self.is_end()
        if result == 'X':
            return (-1, x, y,self.depth)
        elif result == 'O':
            return (1, x, y,self.depth)
        elif result == '.':
            return (0, x, y,self.depth)

        else:
            endtime=time.time()
            timeduration=endtime-startTime
            timeleft=time-timeduration
            if depth!=0 and timeleft>0:
              if max:
                  return self.minimax(self,depth-1,useE2,timeleft,max=False)
              else:
                  return self.minimax(self.depth-1,useE2,timeleft,max=True)
            else:
                for i in range(0, self.size):
                    for j in range(0, self.size):
                        if self.current_state[i][j] == '.':
                            if max:
                                self.current_state[i][j] = 'O'
                                if useE2:
                                    (v, _, _) = self.e2()
                                else:
                                    (v, _, _) = self.e1()
                                if v > value:
                                    value = v
                                    x = i
                                    y = j
                            else:
                                self.current_state[i][j] = 'X'
                                if useE2:
                                    (v, _, _) = self.e2()
                                else:
                                    (v, _, _) = self.e1()
                                if v < value:
                                    value = v
                                    x = i
                                    y = j
                            self.current_state[i][j] = '.'
                return (value,x,y,self.depth)
    def alphabeta(self,depth, useE2,time,alpha=-1000000,beta=1000000,max=False):
        self.depth+=1
        startTime=time.time()
        value=10**(self.winSize+1)
        if max:
            value = -10**(self.winSize+1)
        x = None
        y = None
        result = self.is_end()
        if result == 'X':
            return (-10**self.winSize, x, y,self.depth)
        elif result == 'O':
            return (10**self.winSize, x, y,self.depth)
        elif result == '.':
            return (0, x, y,self.depth)
        else:
            endTime=time.time()
            timeduration=endTime-startTime
            timeLeft=time-timeduration
            if depth!=0 and timeLeft>0:
                if max:
                    return self.alphabeta(self,depth-1,useE2,timeLeft,max=False)
                else:
                    return self.alphabeta(self,depth-1,useE2,timeLeft,max=True)
            else:
                for i in range(0, self.size):
                    for j in range(0, self.size):
                        if self.current_state[i][j] == '.':
                            if max:
                                self.current_state[i][j] = 'O'
                                if useE2:
                                    (v, _, _) = self.e2();
                                else:
                                    (v, _, _) = self.e1();
                                if v > value:
                                    value = v
                                    x = i
                                    y = j
                            else:
                                self.current_state[i][j] = 'X'
                                if useE2:
                                    (v, _, _) = self.e2();
                                else:
                                    (v, _, _) = self.e1();
                                if v < value:
                                    value = v
                                    x = i
                                    y = j
                            self.current_state[i][j] = '.'
                            if max:
                                if value >= beta:
                                    return (value, x, y)
                                if value > alpha:
                                    alpha = value
                            else:
                                if value <= alpha:
                                    return (value, x, y)
                                if value < beta:
                                    beta = value
                return (value, x, y,self.depth)
    def play(self, player_o,player_x,depth_O,depth_X,timeLimit,useE2,algo_X,algo_O):
        if algo == None:
            algo = self.ALPHABETA
        if player_x == None:
            player_x = self.HUMAN
        if player_o == None:
            player_o = self.HUMAN
        while True:
            self.draw_board()
            self.numOfHeuristics=0
            if self.check_end():
                return
            if (self.player_turn == 'X' and player_x == self.HUMAN) or (self.player_turn == 'O' and player_o == self.HUMAN):
                (x, y) = self.input_move()
                print("Player", self.player_turn,"under human control plays:", x, y)
            else:
                start=time.time()
                if self.player_turn=='X':
                    if algo_X==self.MINIMAX:
                        (v, x, y) = self.minimax(depth_X, useE2, timeLimit, max=False)
                    else:
                        (v, x, y) = self.alphabeta(depth_X, useE2, timeLimit, max=False)
                else:
                    if algo_O == self.MINIMAX:
                        (v, x, y) = self.minimax(depth_O, useE2, timeLimit, max=True)
                    else:
                        (v, x, y) = self.alphabeta(depth_O, useE2, timeLimit, max=True)
                # if algo==self.MINIMAX:
                #     if self.player_turn == 'X':
                #         (v, x, y) = self.minimax(depth_X,useE2,timeLimit,max=False)
                #     else:
                #         (v, x, y) = self.minimax(depth_O,useE2,timeLimit,max=True)
                # else:
                #     if self.player_turn == 'X':
                #         (v, x, y) = self.alphabeta(depth, useE2,timeLimit,max=False)
                #     else:
                #         (v, x, y) = self.alphabeta(depth, useE2,timeLimit,max=True)
                print("Player", self.player_turn,"under AI control plays:", x, y)
                print()
                end=time.time()
                evaluationTime=round(end - start, 7)
                print("(i)\tEvaluation time:", evaluationTime)
                print("(ii)\tHeuristic evaluations:", v)






















