0

import time
import random
import  string
class Game:
    MINIMAX = 0
    ALPHABETA = 1
    HUMAN = 2
    AI = 3
    size = 0
    winSize = 0
    depth=0
    depthList=[]
    heuristicList=[]
    numOfStates=0
    totalTime=0
    totalStates=0
    heuristicsTimes=0
    def __init__(self, winsize=0, boardsize=0, recommend=True, ):

        self.initialize_game()
        self.recommend = recommend
        self.winSize=winsize
        self.size=boardsize


    def initialize_game(self):
        self.current_state = []
        # Player X always plays first
        self.player_turn = 'X'

    def setWinsize(self, wins):
        self.winSize = int(wins)
    def createBoard(self, n):
        self.size=int(n)
        for i in range(0, n):
            self.current_state.append(["." for c in range(0, n)])

    def draw_board(self):

        for r in range(len(self.current_state)):
            for c in self.current_state[r]:
                print(c, end=" ")
            print()

    def is_valid(self, px, py):
        if px < 0 or px > self.size-1 or py < 0 or py > self.size-1:
            return False
        elif self.current_state[px][py] != '.':
            return False
        else:
            return True

    def is_end(self):
        for i in range(0, self.size):
            for j in range(0, self.size):
                # win in rows
                if self.current_state[i][j] == "*" or self.current_state[i][j] == ".":
                    continue
                if i < self.size - (self.winSize - 1):
                    count = 0
                    for x in range(0, self.winSize - 1):
                        if (self.current_state[i + x][j] != self.current_state[i + x + 1][j]):
                            break
                        else:
                            count += 1
                            if count == self.winSize - 1:
                                return self.current_state[i][j]

                if j < self.size - (self.winSize - 1):
                    count = 0
                    for x in range(0, self.winSize - 1):
                        if (self.current_state[i][j + x] != self.current_state[i][j + x + 1]):
                            break
                        else:
                            count += 1
                            if count == self.winSize - 1:
                                return self.current_state[i][j]

                if i < self.size - (self.winSize - 1) and j < self.size - (self.winSize - 1):
                    count = 0
                    for x in range(0, self.winSize - 1):
                        if (self.current_state[i + x][j + x] != self.current_state[i + x + 1][j + x + 1]):
                            break
                        else:
                            count += 1
                            if count == self.winSize - 1:
                                return self.current_state[i][j]

                if j > self.winSize - 2 and i < self.size - (self.winSize - 1):
                    count = 0
                    for x in range(0, self.winSize - 1):
                        if (self.current_state[i + x][j - x] != self.current_state[i + x + 1][j - x - 1]):
                            break
                        else:
                            count += 1
                            if count == self.winSize - 1:
                                return self.current_state[i][j]
        for i in range(0, self.size):
            for j in range(0, self.size):
                if self.current_state[i][j] == '.':
                    return None
        print("xxxxxxx")
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
    def AI_move(self, x, y):
        if x==None or y==None:
            for i in range(0,self.size):
                for j in range(0,self.size):
                    if self.current_state[i][j]=='.':
                        x=i
                        y=j
        if self.current_state[x][y]=='.':
            self.current_state[x][y]=self.player_turn
        else:
            self.switch_player()
            self.result=self.player_turn

    def input_move(self):
        while True:
            print(F'Player {self.player_turn}, enter your move:')
            px = input('enter the x coordinate in letters: ')
            py = int(input('enter the y coordinate: '))
            if self.is_valid(int(px), int(py)):
                return (int(px), int(py))
            else:
                print('The move is not valid! Try again.')


    def switch_player(self):
        if self.player_turn == 'X':
            self.player_turn = 'O'
        elif self.player_turn == 'O':
            self.player_turn = 'X'
        return self.player_turn

    def e1(self):
        self.heuristicsTimes+=1
        start=time.time
        value = 0
        result = self.is_end()
        if result == "X":
            return -20 ** self.winSize
        elif result == "O":
            return 20 ** self.winSize
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
        end=time.time()
        self.totalTime+=round(end - start, 7)
        return value

    def e2(self):
        self.heuristicsTimes += 1
        start=time.time()
        value = 0
        count = 0
        recordState = '.'
        result = self.is_end()
        if result == "X":
            return -20 ** self.winSize
        elif result == "O":
            return 20 ** self.winSize
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
                        if self.current_state[i][j]=='O' or self.current_state[i][j]=='*':
                            value+= 10 ** count
                        recordState = self.current_state[i][j]
                    elif recordState == 'O' and (self.current_state[i][j] != recordState or j == self.size - 1):
                        value += 10 ** count
                        if self.current_state[i][j]=='X' or self.current_state[i][j]=='*':
                            value -= 10 ** count
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
                        if self.current_state[j][i]=='O' or self.current_state[j][i]=='*':
                            value+= 10 ** count
                        recordState = self.current_state[j][i]
                    elif recordState == 'O' and (self.current_state[j][i] != recordState or j == self.size - 1):
                        value += 10 ** count
                        if self.current_state[j][i]=='X' or self.current_state[j][i]=='*':
                            value-= 10 ** count
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
                        if self.current_state[x][i + x]=='O' or self.current_state[x][i + x]=='*':
                            value+= 10 ** count
                        recordState = self.current_state[x][i + x]
                    elif recordState == 'O' and (self.current_state[x][i + x] != recordState or x == self.size - i - 1):
                        value += 10 ** count
                        if self.current_state[x][i + x]=='X' or self.current_state[x][i + x]=='*':
                            value-= 10 ** count
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
                        if self.current_state[i + x][x]=='O' or self.current_state[i + x][x]=='*':
                            value+= 10 ** count
                        recordState = self.current_state[i + x][x]
                    elif recordState == 'O' and (self.current_state[i + x][x] != recordState or x == self.size - i - 1):
                        value += 10 ** count
                        if  self.current_state[i + x][x]=='X' or self.current_state[i + x][x]=='*':
                            value-= 10 ** count
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
                        if self.current_state[i - x][x]=='O' or self.current_state[i - x][x]=='*':
                            value+= 10 ** count
                        recordState = self.current_state[i - x][x]
                    elif recordState == 'O' and (self.current_state[i - x][x] != recordState or x == i):
                        value += 10 ** count
                        if self.current_state[i - x][x]=='X' or self.current_state[i - x][x]=='*':
                            value-= 10 ** count
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
                        if self.current_state[x + i][self.size - 1 - x]=='O' or self.current_state[x + i][self.size - 1 - x]=='*':
                            value+= 10 ** count
                        recordState = self.current_state[x + i][self.size - 1 - x]
                    elif recordState == 'O' and (self.current_state[x + i][self.size - 1 - x] != recordState or x == i):
                        value += 10 ** count
                        if self.current_state[x + i][self.size - 1 - x]=='X' or self.current_state[x + i][self.size - 1 - x]=='*':
                            value-= 10 ** count
                        recordState = self.current_state[x + i][self.size - 1 - x]
                    else:
                        recordState = self.current_state[x + i][self.size - 1 - x]
                    count = 0
        end = time.time()
        self.totalTime += round(end - start, 7)
        return value
    def minimax(self,depth,useE2,timelimit, max=False):

        startTime=time.time()
        value=10**(self.winSize+1)
        if max:
            value=-10**(self.winSize+1)
        x = None
        y = None
        endtime = time.time()
        timeduration = endtime - startTime
        timeleft = timelimit - timeduration

        for i in range(0, self.size):
            for j in range(0, self.size):
                if self.current_state[i][j] == '.':
                    self.numOfStates += 1
                    if max:
                        self.current_state[i][j] = 'O'
                        if depth != 0 and timeleft > 0:
                            self.depth += 1
                            (v, _, _) = self.minimax(depth - 1, useE2, timeleft, max=False)

                        else:
                            self.depthList.append(self.depth)
                            if timeleft <= 0:
                                print("*** Out of extra time at depth of", self.depth, "***")
                                x = random.randint(0, self.size - 1)
                                y = random.randint(0, self.size - 1)
                                print("Selected random move for O:", x, y)
                                return (value, x, y)
                            else:

                                if useE2:
                                    v = self.e2()
                                else:
                                    v = self.e1()
                        if v > value:
                            value = v
                            x = i
                            y = j


                    else:
                        self.current_state[i][j] = 'X'
                        if depth != 0 and timeleft > 0:
                            self.depth += 1
                            (v, _, _) = self.minimax(depth - 1, useE2, timeleft, max=True)

                        else:
                            self.depthList.append(self.depth)
                            if timeleft <= 0 and depth!=0:
                                print("*** Out of extra time at depth of", self.depth, "***")
                                x = random.randint(0, self.size - 1)
                                y = random.randint(0, self.size - 1)
                                print("Selected random move for X:", x, y)
                                return (value, x, y)
                            else:
                                if useE2:
                                    v = self.e2()

                                else:
                                    v = self.e1()

                        if v < value:
                            value = v
                            x = i
                            y = j
                    self.current_state[i][j] = '.'

        self.heuristicList.append(self.numOfStates)
        return (value, x, y)


    def alphabeta(self,depth, useE2,timelimit,alpha=-1000000,beta=1000000,max=False):

        startTime=time.time()

        value=10**(self.winSize+1)
        if max:
            value = -10**(self.winSize+1)
        x = None
        y = None
        endTime = time.time()
        timeduration = endTime - startTime
        timeleft = timelimit - timeduration
        for i in range(0, self.size):
            for j in range(0, self.size):
                if self.current_state[i][j] == '.':
                    self.numOfStates += 1
                    if max:
                        self.current_state[i][j] = 'O'
                        if depth != 0 and timeleft > 0:
                            self.depth += 1
                            (v, _, _) = self.alphabeta(depth - 1, useE2, timeleft, alpha, beta, max=False)
                        else:

                            self.depthList.append(self.depth)
                            if timeleft <= 0:
                                print("*** Out of extra time at depth of", self.depth, "***")
                                x = random.randint(0, self.size - 1)
                                y = random.randint(0, self.size - 1)
                                print("Selected random move for O:", x, y)
                                return (value, x, y)
                            else:

                                if useE2:
                                    v = self.e2()
                                else:
                                    v = self.e1()
                        if v > value:
                            value = v
                            x = i
                            y = j
                    else:
                        self.current_state[i][j] = 'X'
                        if depth != 0 and timeleft > 0:
                            self.depth += 1
                            (v, _, _) = self.alphabeta(depth - 1, useE2, timeleft, alpha, beta, max=False)
                        else:
                            self.depthList.append(self.depth)
                            if timeleft <= 0:
                                print("*** Out of extra time at depth of", self.depth, "***")
                                x = random.randint(0, self.size - 1)
                                y = random.randint(0, self.size - 1)
                                print("Selected random move for X:", x, y)
                                return (value, x, y)
                            else:
                                if useE2:
                                    v = self.e2()

                                else:
                                    v = self.e1()

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

        self.heuristicList.append(self.numOfStates)
        return (value, x, y)


    def play(self, player_o,player_x,depth_O,depth_X,timeLimit,useE2_X,useE2_O,algo_X,algo_O):
        steps=0
        totaldepths=0
        if algo_X == None:
            algo_X = self.ALPHABETA
        if algo_O == None:
            algo_O = self.ALPHABETA
        if player_x == None:
            player_x = self.HUMAN
        if player_o == None:
            player_o = self.HUMAN

        while True:

            if self.check_end():
                print("6(b)i\tAverage evaluation time:", self.totalTime/self.heuristicsTimes)
                print("6(b)ii\tTotal heuristic evaluations:",self.heuristicsTimes)
                print("6(b)iii\tEvaluations by depth:")
                print("6(b)iv\tAverage evaluation depth:",totaldepths/steps)
                print("6(b)v\tAverage recursion depth:")
                print("6(b)vi\tTotal moves:",steps)
                return
            steps+=1
            if (self.player_turn == 'X' and player_x == self.HUMAN) or (self.player_turn == 'O' and player_o == self.HUMAN):
                (x, y) = self.input_move()
                print("Player", self.player_turn,"under human control plays:", x, y)
                self.current_state[x][y]=self.player_turn
                self.draw_board()
                self.switch_player()
            else:
                heuristicEvaluation=0
                sumOfDepths=0
                self.heuristicList=[]
                self.depthList=[]
                self.depth=0
                self.numOfStates=0
                start=time.time()
                if self.player_turn=='X':
                    if algo_X==self.MINIMAX:
                        (v, x, y) = self.minimax(depth_X, useE2_X, timeLimit, max=False)
                    else:
                        (v, x, y) = self.alphabeta(depth_X, useE2_X, timeLimit, max=False)
                else:
                    if algo_O == self.MINIMAX:
                        (v, x, y) = self.minimax(depth_O, useE2_O, timeLimit, max=True)
                    else:
                        (v, x, y) = self.alphabeta(depth_O, useE2_O, timeLimit, max=True)
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
                self.AI_move(x,y)
                print("Player", self.player_turn,"under AI control plays:", x, y)
                print()
                end=time.time()
                evaluationTime=round(end - start, 7)
                for i in self.heuristicList:
                    heuristicEvaluation+=i
                for i in self.depthList:
                    sumOfDepths+=i
                self.draw_board()
                print("(i)\tEvaluation time:", evaluationTime)
                print("(ii)\tHeuristic evaluations:", heuristicEvaluation)
                print("(iii)\tEvaluations by depth:")
                print("(iv)\tAverage evaluation depth:", sumOfDepths/len(self.depthList))
                totaldepths+=sumOfDepths/len(self.depthList)
                print("(v)\tAverage recursion depth:")
                self.switch_player()

def main():
    print("Welcome to play Line 'em up !!!")
    print("-----------------**************-----------------")
    n = input("Please key in the size of the board:")
    g = Game(recommend=True)
    g.createBoard(int(n))
    b = input("Please key in the number of the blocs:")
    choice = int(input("Please select the way to generate blocs (0 for random, 1 for customize)"))
    listOfBlocs = []
    if choice == 0:
        for x in range(int(b)):
            i = random.randint(0, int(n) - 1)
            j = random.randint(0, int(n) - 1)
            if g.current_state[i][j] == '*':
                continue
            else:
                g.current_state[i][j] = '*'
                listOfBlocs.append("(" + str(i) + "," + str(j) + ")")
                x -= 1
    else:
        x = 0
        while x < (int(b)):
            print("\n" + "Please key in the coordinate of block " + str(x + 1))
            j = int(input("Please enter the column(start from 0)"))
            if j > (int(b) - 1):
                print("invalid input")
                continue
            i = int(input("Please enter the row(start from 0)"))
            if i > (int(b) - 1):
                print("invalid input")
                continue
            if g.current_state[i-1][j-1] == '*':
                print("duplicate coordinate")
                continue
            else:
                g.current_state[i-1][j-1] = '*'
                listOfBlocs.append("(" + str(j) + "," + str(i) + ")")
                x += 1
    print("The game board generated is: ")

    g.draw_board()
    print("\n")
    print("blocs=" + str(listOfBlocs) + "\n")
    s = input("Please key in the winning line-up size:")
    g.setWinsize(s)
    mode = int(input("Please enter a number to select the play mode(1 for H-H, 2 for H-AI, 3 for AI-H, 4 for AI-AI):"))
    if mode == 1:
        print("\n" + "Your choice is both player_X and player_O are human")
        d1 = 0
        d2 = 0
        t = 0
        a1 = 0
        a2 = 0
        e1 = 0
        e2 = 0
        player_x = 2
        player_o = 2
    else:
        if mode == 2:
            print("\n" + "Your choice is player_X is human and player_O is AI")
            d1 = 0
            d2 = input("What max depth of the adversarial search do you want to set for player_O?")
            t = input("What is the maximum allowed time(in seconds) you want to set for the game?")
            a1 = 0
            a2 = input("What algo do you want player_O(AI) use? (Enter 0 for minimax and 1 for aplabeta)")
            e1 = 0
            e2 = input("Which heuristic do you want player_O(AI) use?(Enter 0 for e1 1 for e2)")
            player_x = 2
            player_o = 3
        else:
            if mode == 3:
                print("\n" + "Your choice is player_X is AI and player_O is human")
                d1 = input("What max depth of the adversarial search do you want to set for player_X?")
                d2 = 0
                t = input("What is the maximum allowed time(in seconds) you want to set for the game?")
                a1 = input("What algo do you want player_X(AI) use? (Enter 0 for minimax and 1 for aplabeta))")
                a2 = 0
                e1 = input("Which heuristic do you want player_X(AI) use?(Enter 0 for e1 1 for e2)")
                e2 = 0
                player_x = 3
                player_o = 2
            else:
                print("\n" + "Your choice is both player_X and player_O are AI")
                d1 = input("What max depth of the adversarial search do you want to set for player_X?")
                d2 = input("What max depth of the adversarial search do you want to set for player_O?")
                t = input("What is the maximum allowed time(in seconds) you want to set for the game?")
                a1 = input("What algo do you want player_X use? (Enter 0 for minimax and 1 for aplabeta)")
                a2 = input("What algo do you want player_O use? (Enter 0 for minimax and 1 for aplabeta)")
                e1 = input("Which heuristic do you want player_X(AI) use?(Enter 0 for e1 1 for e2)")
                e2 = input("Which heuristic do you want player_O(AI) use?(Enter 0 for e1 1 for e2)")
                player_x = 3
                player_o = 3

    g.play(int(player_o),int(player_x),int(d2),int(d1),int(t),int(e1),int(e2),int(a1),int(a2))
if __name__ == "__main__":
    main()

























