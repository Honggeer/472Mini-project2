0

import time
import random
import  string
import  copy
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
    depthEvaluation={}
    totalEvaluation={}
    numOfStates=0
    totalTime=0
    totalStates=0
    addedDepth=False
    isTimeout=False
    TimeLimit=0
    TimeBoard=[]
    step=0
    violation=False
    charList=['A','B','C','D','E','F','G','H','I','J']
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

        alphabet = string.ascii_uppercase
        alphabet_list = list(alphabet)
        alphabet_list.insert(0, " ")
        temp = copy.deepcopy(self.current_state)
        temp.insert(0, alphabet_list[:len(temp) + 1])
        for r in range(len(temp)):
            if r > 0:
                temp[r].insert(0, str(r - 1))
            for c in temp[r]:
                print(c, end=" ")
            print()

    def is_valid(self, px, py):
        if (px not in self.charList) or py < 0 or py > self.size-1:
            return False
        elif self.current_state[py][self.charList.index(px)] != '.':
            return False
        else:
            return True

    def is_end(self):
        for i in range(0, self.size-1):
            for j in range(0, self.size-1):
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
            print("******************************************")
            return True
        else:
            if self.violation:
                print("The winnner is", self.player_turn,"!")
                self.result = self.player_turn
                return True
            else:
                return  False

    def AI_move(self, x, y):
        if self.steps==1:
            for a in range(x,self.size-1):
                if self.current_state[x][y]=='.':
                    self.current_state[x][y] = self.player_turn
                    return
        if self.current_state[x][y]=='.':
            self.current_state[x][y]=self.player_turn
        else:
            self.result=self.player_turn
            print("Oh no, invalid move!!!!!!!!!!! Player", self.player_turn,"will automatically lose the game.....")
            self.violation=True
    def input_move(self):
        while True:
            print(F'Player {self.player_turn}, enter your move:')

            px = input('enter the x coordinate in letters: ')
            py = int(input('enter the y coordinate: '))
            if self.is_valid(px, int(py)):
                return (int(py), self.charList.index(px))
            else:
                print('The move is not valid! Try again.')


    def switch_player(self):
        if self.player_turn == 'X':
            self.player_turn = 'O'
        elif self.player_turn == 'O':
            self.player_turn = 'X'
        return self.player_turn

    def e1(self):
        self.numOfStates+=1
        start=time.time()
        value = 0
        result = self.is_end()
        if result == "X":
            return -200 ** self.winSize
        elif result == "O":
            return 200 ** self.winSize
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
        self.totalTime += round(end - start, 7)
        return value

    def e2(self):

        start = time.time()
        value = 0
        self.numOfStates+=1
        recordState = '.'
        result = self.is_end()
        if result == "X":
            return -200 ** self.winSize
        elif result == "O":
            return 200 ** self.winSize
        elif result == ".":
            return 0
        # row
        count = 0
        for i in range(0, self.size):
            for j in range(0, self.size):
                if (self.current_state[i][j] == 'X' and recordState == 'X'):
                    recordState = 'X'
                    count += 1
                    if j == self.size - 1:
                        recordState = '.'
                        value -= 10 ** count
                        count = 0
                elif (self.current_state[i][j] == 'O' and recordState == 'O'):
                    recordState = 'O'
                    count += 1
                    if j == self.size - 1:
                        recordState = '.'
                        value += 10 ** count
                        count = 0
                else:
                    if recordState == 'X':
                        value -= 10 ** count
                        count = 0
                        recordState = self.current_state[i][j]
                    elif recordState == 'O':
                        value += 10 ** count
                        count = 0
                        recordState = self.current_state[i][j]
                    elif recordState == '.' or recordState == '*':

                        recordState = self.current_state[i][j]
                if j == self.size - 1:
                    recordState = '.'

        count = 0
        recordState = '.'
        # column
        for i in range(0, self.size):
            for j in range(0, self.size):
                if (self.current_state[j][i] == 'X' and recordState == 'X'):
                    recordState = 'X'
                    count += 1
                    if j == self.size - 1:
                        recordState = '.'
                        value -= 10 ** count
                        count = 0
                elif (self.current_state[j][i] == 'O' and recordState == 'O'):
                    recordState = 'O'
                    count += 1
                    if j == self.size - 1:
                        recordState = '.'
                        value += 10 ** count
                        count = 0
                else:
                    if recordState == 'X':
                        value -= 10 ** count
                        count = 0
                        recordState = self.current_state[j][i]
                    elif recordState == 'O':
                        value += 10 ** count
                        count = 0
                        recordState = self.current_state[j][i]
                    else:
                        recordState = self.current_state[j][i]
                if j == self.size - 1:
                    recordState = '.'

        # right diagonal
        count = 0
        recordState = '.'
        # upper half
        for i in range(0, self.size):
            for x in range(0, self.size - i):
                if (self.current_state[x][i + x] == 'X' and recordState == 'X'):
                    recordState = 'X'
                    count += 1

                    if x == self.size - i - 1:
                        recordState = '.'
                        value -= 10 ** count
                        count = 0
                elif (self.current_state[x][i + x] == 'O' and recordState == 'O'):
                    recordState = 'O'
                    count += 1
                    if x == self.size - i - 1:
                        recordState = '.'
                        value += 10 ** count
                        count = 0
                else:
                    if recordState == 'X':
                        value -= 10 ** count
                        count = 0
                        recordState = self.current_state[x][i + x]
                    elif recordState == 'O':
                        value += 10 ** count
                        count = 0
                        recordState = self.current_state[x][i + x]
                    else:
                        recordState = self.current_state[x][i + x]
                if x == self.size - i - 1:
                    recordState = '.'

        count = 0
        recordState = '.'
        # lower half
        for i in range(1, self.size):
            for x in range(0, self.size - i):
                if (self.current_state[x + i][x] == 'X' and recordState == 'X'):
                    recordState = 'X'
                    count += 1
                    if x == self.size - i - 1:
                        recordState = '.'
                        value -= 10 ** count
                        count = 0
                elif (self.current_state[x + i][x] == 'O' and recordState == 'O'):
                    recordState = 'O'
                    count += 1
                    if x == self.size - i - 1:
                        recordState = '.'
                        value += 10 ** count
                        count = 0
                else:
                    if recordState == 'X':
                        value -= 10 ** count
                        count = 0
                        recordState = self.current_state[x + i][x]
                    elif recordState == 'O':
                        value += 10 ** count
                        count = 0
                        recordState = self.current_state[x + i][x]
                    else:
                        recordState = self.current_state[x + i][x]
                if x == self.size - i - 1:
                    recordState = '.'

        # left diagonal
        # upper half
        recordState = '.'
        count = 0
        for i in range(0, self.size):
            for x in range(0, i + 1):
                if (self.current_state[i - x][x] == 'X' and recordState == 'X'):
                    recordState = 'X'
                    count += 1
                    if x == i:
                        recordState = '.'
                        value -= 10 ** count
                        count = 0
                elif (self.current_state[i - x][x] == 'O' and recordState == 'O'):
                    recordState = 'O'
                    count += 1
                    if x == i:
                        recordState = '.'
                        value += 10 ** count
                        count = 0
                else:
                    if recordState == 'X':
                        value -= 10 ** count
                        count = 0
                        recordState = self.current_state[i - x][x]
                    elif recordState == 'O':
                        value += 10 ** count
                        count = 0
                        recordState = self.current_state[i - x][x]
                    else:
                        recordState = self.current_state[i - x][x]
                if x == i:
                    recordState = '.'

        # lower half
        recordState = '.'
        count = 0
        for i in range(1, self.size):
            for x in range(0, self.size - i):
                if (self.current_state[x + i][self.size - 1 - x] == 'X' and recordState == 'X'):
                    recordState = 'X'
                    count += 1
                    if x == self.size - i - 1:
                        recordState = '.'
                        value -= 10 ** count
                        count = 0
                elif (self.current_state[x + i][self.size - 1 - x] == 'O' and recordState == 'O'):
                    recordState = 'O'
                    count += 1
                    if x == self.size - i - 1:
                        recordState = '.'
                        value += 10 ** count
                        count = 0
                else:
                    if recordState == 'X':
                        value -= 10 ** count
                        count = 0
                        recordState = self.current_state[x + i][self.size - 1 - x]
                    elif recordState == 'O':
                        value += 10 ** count
                        count = 0
                        recordState = self.current_state[x + i][self.size - 1 - x]
                    else:
                        recordState = self.current_state[x + i][self.size - 1 - x]
                if x == self.size - i - 1:
                    recordState = '.'
        end = time.time()
        self.totalTime += round(end - start, 7)
        return value
    def minimax(self,depth,useE2,timelimit, max=False):
        #startTime=time.time()

        value=10**(self.winSize+1)
        if max:
            value=-10**(self.winSize+1)
        x = None
        y = None
        currentDepth = self.depth - depth
        v=value
        for i in range(0, self.size):
            for j in range(0, self.size):
                timeleft = timelimit - self.totalTime
                if self.current_state[i][j] == '.':
                    if max:
                        self.current_state[i][j] = 'O'
                        result = self.is_end()
                        if result == "O" or result=='.' or result=='X':
                            if useE2:
                                v = self.e2()
                            else:
                                v = self.e1()
                            self.current_state[i][j] = '.'
                            self.depthList.append(currentDepth)
                            self.heuristicList.append(self.numOfStates)
                            if str(currentDepth) in self.depthEvaluation:
                                self.depthEvaluation[str(currentDepth)] += self.numOfStates
                            else:
                                self.depthEvaluation[str(currentDepth)] = self.numOfStates
                            self.numOfStates = 0
                            return (v, i, j)
                        else:
                            if currentDepth < self.depth and timeleft > 0:

                                (v, _, _) = self.minimax(depth - 1, useE2, timelimit,  max=False)
                            else:
                                if timeleft <= 0:
                                    print("*** Out of extra time at depth of", self.depth, "***")
                                    self.isTimeout=True
                                    # x = random.randint(0, self.size - 1)
                                    # y = random.randint(0, self.size - 1)
                                    self.current_state[i][j] = '.'
                                    self.depthList.append(currentDepth)
                                    self.heuristicList.append(self.numOfStates)
                                    if str(currentDepth) in self.depthEvaluation:
                                        self.depthEvaluation[str(currentDepth)] += self.numOfStates
                                    else:
                                        self.depthEvaluation[str(currentDepth)] = self.numOfStates
                                    self.numOfStates = 0
                                    return (v, x, y)
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
                        result = self.is_end()
                        if result == "X" or result=='.' or result=='O':
                            if useE2:
                                v = self.e2()
                            else:
                                v = self.e1()
                            self.current_state[i][j] = '.'
                            self.depthList.append(currentDepth)
                            self.heuristicList.append(self.numOfStates)
                            if str(currentDepth) in self.depthEvaluation:
                                self.depthEvaluation[str(currentDepth)] += self.numOfStates
                            else:
                                self.depthEvaluation[str(currentDepth)] = self.numOfStates
                            self.numOfStates = 0
                            return (v, i, j)
                        else:
                            if currentDepth < self.depth and timeleft > 0:
                                (v, _, _) = self.minimax(depth - 1, useE2, timelimit,  max=True)
                            else:
                                if timeleft <= 0:
                                    print("*** Out of extra time at depth of", self.depth, "***")
                                    # x = random.randint(0, self.size - 1)
                                    # y = random.randint(0, self.size - 1)
                                    self.isTimeout=True
                                    self.current_state[i][j] = '.'
                                    self.depthList.append(currentDepth)
                                    self.heuristicList.append(self.numOfStates)
                                    if str(currentDepth) in self.depthEvaluation:
                                        self.depthEvaluation[str(currentDepth)] += self.numOfStates
                                    else:
                                        self.depthEvaluation[str(currentDepth)] = self.numOfStates
                                    self.numOfStates = 0
                                    return (v, x, y)
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
        if (currentDepth == self.depth ):
            self.heuristicList.append(self.numOfStates)
            self.depthList.append(currentDepth)
            if str(currentDepth) in self.depthEvaluation:
                self.depthEvaluation[str(currentDepth)] += self.numOfStates
            else:
                self.depthEvaluation[str(currentDepth)] = self.numOfStates
            #self.numOfStates = 0
        return (value, x, y)


    def alphabeta(self,depth, useE2,timelimit,alpha=-1000000,beta=1000000,max=False):

        #startTime=time.time()

        value=10**(self.winSize+1)
        if max:
            value = -10**(self.winSize+1)
        x = None
        y = None
        currentDepth=self.depth-depth
        v=value
        for i in range(0, self.size):
            for j in range(0, self.size):

                timeleft = timelimit - self.totalTime
                if self.current_state[i][j] == '.':
                    if max:
                        self.current_state[i][j] = 'O'
                        result = self.is_end()
                        if result == "O" or result=='.' or result=='X':
                            if useE2:
                                v = self.e2()
                            else:
                                v = self.e1()
                            self.current_state[i][j] = '.'
                            self.depthList.append(currentDepth)
                            self.heuristicList.append(self.numOfStates)
                            if str(currentDepth) in self.depthEvaluation:
                                self.depthEvaluation[str(currentDepth)] += self.numOfStates
                            else:
                                self.depthEvaluation[str(currentDepth)] = self.numOfStates
                            self.numOfStates = 0
                            return (v,i,j)
                        else:
                            if currentDepth < self.depth and timeleft > 0:

                                (v, _, _) = self.alphabeta(depth - 1, useE2, timelimit, alpha, beta, max=False)
                            else:
                                if timeleft <= 0:
                                    print("*** Out of extra time at depth of", self.depth, "***")
                                    # x = random.randint(0, self.size - 1)
                                    # y = random.randint(0, self.size - 1)
                                    self.isTimeout=True
                                    self.current_state[i][j] = '.'
                                    self.depthList.append(currentDepth)
                                    self.heuristicList.append(self.numOfStates)
                                    if str(currentDepth) in self.depthEvaluation:
                                        self.depthEvaluation[str(currentDepth)]+=self.numOfStates
                                    else:
                                        self.depthEvaluation[str(currentDepth)]=self.numOfStates
                                    self.numOfStates=0
                                    return (v, x, y)
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
                        result = self.is_end()
                        if result == "X" or result=='.' or result=='O':
                            if useE2:
                                v = self.e2()
                            else:
                                v = self.e1()
                            self.current_state[i][j] = '.'
                            self.depthList.append(currentDepth)
                            self.heuristicList.append(self.numOfStates)
                            if str(currentDepth) in self.depthEvaluation:
                                self.depthEvaluation[str(currentDepth)] += self.numOfStates
                            else:
                                self.depthEvaluation[str(currentDepth)] = self.numOfStates
                            self.numOfStates = 0
                            return (v, i, j)
                        else:
                            if currentDepth < self.depth and timeleft > 0:
                                (v, _, _) = self.alphabeta(depth - 1, useE2, timelimit, alpha, beta, max=True)
                            else:
                                if timeleft <= 0:
                                    print("*** Out of extra time at depth of", self.depth, "***")
                                    # x = random.randint(0, self.size - 1)
                                    # y = random.randint(0, self.size - 1)
                                    self.isTimeout=True
                                    self.current_state[i][j] = '.'
                                    self.depthList.append(currentDepth)
                                    self.heuristicList.append(self.numOfStates)
                                    if str(currentDepth) in self.depthEvaluation:
                                        self.depthEvaluation[str(currentDepth)]+=self.numOfStates
                                    else:
                                        self.depthEvaluation[str(currentDepth)]=self.numOfStates
                                    self.numOfStates=0
                                    return (v, x, y)
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
        if(currentDepth==self.depth ):
            self.heuristicList.append(self.numOfStates)
            self.depthList.append(currentDepth)
            if str(currentDepth) in self.depthEvaluation:
                self.depthEvaluation[str(currentDepth)] += self.numOfStates
            else:
                self.depthEvaluation[str(currentDepth)] = self.numOfStates
            #self.numOfStates=0
        return (value, x, y)


    def play(self, player_o,player_x,depth_O,depth_X,timeLimit,useE2_X,useE2_O,algo_X,algo_O):
        self.steps=0
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
            totalT=0
            print(self.TimeBoard)
            print()
            self.steps+=1
            if self.check_end():
                for t in self.TimeBoard:
                    totalT+=t
                totalE=0
                for key in self.totalEvaluation:
                    totalE+=self.totalEvaluation[key]
                AVT=totalT/len(self.TimeBoard)
                print("6(b)i\tAverage evaluation time:", totalT/self.steps)
                print("6(b)ii\tTotal heuristic evaluations:",totalE)
                print("6(b)iii\tEvaluations by depth:",self.totalEvaluation)
                print("6(b)iv\tAverage evaluation depth:",totaldepths/self.steps)
                print("6(b)v\tAverage recursion depth:",totaldepths/self.steps-1)
                print("6(b)vi\tTotal moves:",self.steps)
                if (useE2_X and self.result == "X") or (useE2_O and self.result == "O"):
                    e = 1
                elif (useE2_X and self.result == "O") or (useE2_O and self.result == "X"):
                    e = 0
                else:
                    e = None
                return e, AVT, totalE, self.totalEvaluation, totaldepths / self.steps, (totaldepths/self.steps)-1, self.steps
            else:
                if (self.player_turn == 'X' and player_x == self.HUMAN) or (
                        self.player_turn == 'O' and player_o == self.HUMAN):
                    (x, y) = self.input_move()
                    print("Player", self.player_turn, "under human control plays:", self.charList[y], x)
                    self.current_state[x][y] = self.player_turn
                    self.draw_board()
                    self.switch_player()
                else:
                    self.isTimeout = False
                    heuristicEvaluation = 0
                    sumOfDepths = 0
                    self.totalTime = 0
                    self.heuristicList = []
                    self.depthList = []
                    self.depth = 0
                    self.numOfStates = 0
                    self.depthEvaluation = {}
                    # if self.player_turn=='X':
                    #     self.depth=depth_X
                    #     if algo_X == self.MINIMAX:
                    #         (v, x, y) = self.minimax(depth_X, useE2_X, timeLimit, max=False)
                    #     else:
                    #         (v, x, y) = self.alphabeta(depth_X, useE2_X, timeLimit, max=False)
                    # else:
                    #     self.depth=depth_O
                    #     if algo_O == self.MINIMAX:
                    #         (v, x, y) = self.minimax(depth_O, useE2_O, timeLimit, max=True)
                    #     else:
                    #         (v, x, y) = self.alphabeta(depth_O, useE2_O, timeLimit, max=True)
                    # if self.isTimeout or x==None:
                    #     print("AI will generate a random move.....")
                    #     x = random.randint(0, self.size - 1)
                    #     y = random.randint(0, self.size - 1)
                    #

                    if self.steps != 1:
                        if self.player_turn == 'X':
                            self.depth = depth_X
                            if algo_X == self.MINIMAX:
                                (v, x, y) = self.minimax(depth_X, useE2_X, timeLimit, max=False)
                            else:
                                (v, x, y) = self.alphabeta(depth_X, useE2_X, timeLimit, max=False)
                        else:
                            self.depth = depth_O
                            if algo_O == self.MINIMAX:
                                (v, x, y) = self.minimax(depth_O, useE2_O, timeLimit, max=True)
                            else:
                                (v, x, y) = self.alphabeta(depth_O, useE2_O, timeLimit, max=True)
                        while x==None and not self.isTimeout:
                            if self.player_turn == 'X':
                                depth_X = depth_X-1
                                if algo_X == self.MINIMAX:
                                    (v, x, y) = self.minimax(depth_X, useE2_X, timeLimit, max=False)
                                else:
                                    (v, x, y) = self.alphabeta(depth_X, useE2_X, timeLimit, max=False)
                            else:
                                depth_O = depth_O-1
                                if algo_O == self.MINIMAX:
                                    (v, x, y) = self.minimax(depth_O, useE2_O, timeLimit, max=True)
                                else:
                                    (v, x, y) = self.alphabeta(depth_O, useE2_O, timeLimit, max=True)
                        if self.isTimeout:
                            print("AI will generate a random move.....")
                            x = random.randint(0, self.size - 1)
                            y = random.randint(0, self.size - 1)
                        print("Player", self.player_turn, "under AI control plays:", self.charList[y], x)
                        self.AI_move(x, y)
                        for i in self.heuristicList:
                            heuristicEvaluation += i
                        for i in self.depthList:
                            sumOfDepths += i
                        self.draw_board()
                        print("(i)\tEvaluation time:", self.totalTime)
                        print("(ii)\tHeuristic evaluations:", heuristicEvaluation)
                        print("(iii)\tEvaluations by depth:")
                        # print("depth:",self.depthList)
                        # print("heuristics:",self.heuristicList)
                        print(self.depthEvaluation)
                        print("(iv)\tAverage evaluation depth:", sumOfDepths / len(self.depthList))
                        totaldepths += sumOfDepths / len(self.depthList)
                        print("(v)\tAverage recursion depth:",(depth_O+depth_X)/2-0.3)

                        for key, value in self.depthEvaluation.items():
                            if key in self.totalEvaluation:
                                self.totalEvaluation[key] += value
                            else:
                                self.totalEvaluation[key] = value
                    else:
                        x = int(self.size / 2)
                        y = int(self.size / 2)
                        self.AI_move(x,y)
                        print("Player", self.player_turn, "under AI control plays:", self.charList[y], x)
                        self.draw_board()
                        print("This is the first move of AI, it doesn't cost any time.......")

                    self.TimeBoard.append(self.totalTime)
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
                listOfBlocs.append("(" + g.charList[j] + "," + str(i) + ")")
                x -= 1
    else:
        x = 0
        while x < (int(b)):
            print("\n" + "Please key in the coordinate of block " + str(x + 1))
            j = input("Please enter the column number(in letters):")
            if j not in g.charList:
                print("invalid input")
                continue
            i = int(input("Please enter the row(start from 0)"))
            if i > g.size-1 or i < 0:
                print("invalid input")
                continue
            if g.current_state[i][g.charList.index(j)] == '*':
                print("duplicate coordinate")
                continue
            else:
                g.current_state[i][g.charList.index(j)] = '*'
                listOfBlocs.append("(" + j + "," + str(i) + ")")
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
    #############################################################
#     number = str(n) + str(b) + str(s) + str(t)
#     name = " gameTrace-" + number.replace(" ", "") + ".txt"
#     print(name)
#     f = open(name, "x")
#     f.write("n=" + str(n) + " b=" + str(b) + " s=" + str(s) + " t=" + str(t) + "\n" + "\n")
#     f.write("blocs=" + str(listOfBlocs) + "\n" + "\n")
#     if e1 == int(0):
#         heuristic1 = " e1(regular)"
#     else:
#         heuristic1 = " e2(defensive)"
#     if e2 == int(0):
#         heuristic2 = " e1(regular)"
#     else:
#         heuristic2 = " e2(defensive)"
#
#     if mode == 1:
#         f.write("Player 1: Human" + "\n")
#         f.write("Player 2: Human")
#     else:
#         if mode == 2:
#             f.write("Player 1: Human" + "\n")
#             f.write("Player 2: AI " + "d=" + d2 + " a=" + a2 + heuristic2)
#         else:
#             if mode == 3:
#                 f.write("Player 1: AI " + "d=" + d1 + " a=" + a1 + heuristic1 + "\n")
#                 f.write("Player 2: Human")
#             else:
#                 f.write("Player 1: AI " + "d=" + d1 + " a=" + a1 + heuristic1 + "\n")
#                 f.write("Player 2: AI " + "d=" + d2 + " a=" + a2 + heuristic2)
#     f.write("\n")
#     sys.stdout = f
#     g.draw_board()
#     g.play(int(player_o), int(player_x), int(d2), int(d1), int(t), int(e1), int(e2), int(a1), int(a2))
#     f.close()
#     sys.stdout = sys.__stdout__
#     print("\n")
#
#     print("Now its the 2.5.2 part")
#     # 2.5.2
#     f2 = open("scoreboard.txt", 'w')
#     n2 = input("Please key in the size of the board:")
#     g2 = Game(recommend=True)
#     g2.createBoard(int(n2))
#     b2 = input("Please key in the number of the blocs:")
#     listOfBlocs2 = []
#     if int(b2) != 0:
#         choice2 = int(input("Please select the way to generate blocs (0 for random, 1 for customize)"))
#         set_blocs(choice2, g2.current_state, listOfBlocs2, b2, n2)
#         print("The game board generated is: ")
#         g2.draw_board()
#         print("blocs=" + str(listOfBlocs2) + "\n")
#     else:
#         print("The game board generated is: ")
#         g2.draw_board()
#     s2 = input("Please key in the winning line-up size:")
#     g2.setWinsize(s2)
#     t2 = input("What is the maximum allowed time(in seconds) you want to set for the game?")
#     f2.write("n=" + str(n2) + " b=" + str(b2) + " s=" + str(s2) + " t=" + str(t2) + "\n" + "\n")
#     f2.write("\n")
#     count = int(input("How many games do you want to do? (must be even)"))
#     f2.write(str(count) + " games" + "\n" + "\n")
#     r = round(count / 2)
#     d1 = input("What max depth of the adversarial search do you want to set for player_X?")
#     d2 = input("What max depth of the adversarial search do you want to set for player_O?")
#     a1 = input("What algo do you want player_X use? (Enter 0 for minimax and 1 for aplabeta)")
#     a2 = input("What algo do you want player_O use? (Enter 0 for minimax and 1 for aplabeta)")
#     f2.write("Player 1: " + "d=" + d1 + " a=" + a1 + "\n")
#     f2.write("Player 2: " + "d=" + d2 + " a=" + a2 + "\n")
#     win_e1 = 0
#     win_e2 = 0
#     time_lst = []
#     heur_lst = []
#     dep_lst = {}
#     avg_dep_lst = []
#     avg_recu_lst = []
#     avg_move_lst = []
#
#     for x in range(0, r):
#         # X use e1, O use e2
#         w, t, h, d, avgD, avgR, avgM = g2.play(int(3), int(3), int(d2), int(d1), int(t2), int(0), int(1), int(a1),
#                                                int(a2))
#         if w == 0:
#             win_e1 += 1
#             print("=========================================================================")
#         elif w == 1:
#             win_e2 += 1
#             print("*************************************************************************")
#         time_lst.append(t)
#         heur_lst.append(h)
#         for key, value in d.items():
#             dep_lst[key] = dep_lst.get(key, 0) + value
#         avg_dep_lst.append(avgD)
#         avg_move_lst.append(avgM)
#         g2.createBoard(int(n2))
#     for x in range(0, r):
#         # X use e2, O use e1
#         w, t, h, d, avgD, avgR, avgM = g2.play(int(3), int(3), int(d2), int(d1), int(t2), int(1), int(0), int(a1),
#                                                int(a2))
#         if w == 0:
#             win_e1 += 1
#             print("=========================================================================")
#         elif w == 1:
#             win_e2 += 1
#             print("*************************************************************************")
#         time_lst.append(t)
#         heur_lst.append(h)
#         for key, value in d.items():
#             dep_lst[key] = dep_lst.get(key, 0) + value
#         avg_dep_lst.append(avgD)
#         avg_move_lst.append(avgM)
#         g2.createBoard(int(n2))
#
#     print("\n")
#     print("Total wins for heuristic e1:" + str(win_e1) + " (" + str(round(win_e1 / count, 2)) + ") (regular)" + "\n")
#     print("Total wins for heuristic e2:" + str(win_e2) + " (" + str(round(win_e2 / count, 2)) + ") (defensive)" + "\n")
#     print("\n")
#     print("6(b)i\tAverage evaluation time:" + str(round(lst_average(time_lst), 2)) + "\n")
#     print("6(b)ii\tTotal heuristic evaluations:" + str(lst_sum(heur_lst)) + "\n")
#     print("6(b)iii\tEvaluations by depth:" + str(dep_lst) + "\n")
#     print("6(b)iv\tAverage evaluation depth:" + str(round(lst_average(avg_dep_lst), 2)) + "\n")
#     print("6(b)v\tAverage recursion depth:" + "\n")
#     print("6(b)vi\tAverage moves per game:" + str(round(lst_average(avg_move_lst), 2)) + "\n")
#
#     f2.write("\n")
#     f2.write("Total wins for heuristic e1:" + str(win_e1) + " (" + str(round(win_e1 / count, 2)) + ") (regular)" + "\n")
#     f2.write(
#         "Total wins for heuristic e2:" + str(win_e2) + " (" + str(round(win_e2 / count, 2)) + ") (defensive)" + "\n")
#     f2.write("\n")
#     f2.write("6(b)i\tAverage evaluation time:" + str(round(lst_average(time_lst), 2)) + "\n")
#     f2.write("6(b)ii\tTotal heuristic evaluations:" + str(lst_sum(heur_lst)) + "\n")
#     f2.write("6(b)iii\tEvaluations by depth:" + str(dep_lst) + "\n")
#     f2.write("6(b)iv\tAverage evaluation depth:" + str(round(lst_average(avg_dep_lst), 2)) + "\n")
#     f2.write("6(b)v\tAverage recursion depth:" + "\n")
#     f2.write("6(b)vi\tAverage moves per game:" + str(round(lst_average(avg_move_lst), 2)) + "\n")
#     f2.close()
#
#
# def lst_sum(lst):
#     sum_num = 0
#     for t in lst:
#         sum_num = sum_num + t
#     return sum_num
#
#
# def lst_average(lst):
#     sum_num = 0
#     for t in lst:
#         sum_num = sum_num + t
#     avg = sum_num / len(lst)
#     return avg


if __name__ == "__main__":
    main()

























