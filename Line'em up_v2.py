0

import time
import random
import string

class Game:
    MINIMAX = 0
    ALPHABETA = 1
    HUMAN = 2
    AI = 3
    size = 0
    winSize = 0
    depth=0
    # #The input
    # n = input("Please key in the size of the board:")
    # keyboard = [n-1][n-1]
    # b = input("Please key in the number of the blocs:")
    # for x in range(b):
    #     i = random.randint(0, n-1)
    #     j = random.radnint(0, n-1)
    #     if not keyboard[i][j]:
    #         --x
    #     else:
    #         keyboard[i][j] = "b"
    # s = input("Please key in the winning line-up size:")
    # d1 = input("Please key in the max depth of ad search of player 1:")
    # d2 = input("Please key in the max depth of ad search of player 2:")
    # t = input("Please key in the max allowed time for AI to return a move:")
    # a = input("Enter 0 to use Minimax and 1 to use Alphabeta")
    # mode = input("Please key in the play mode(H-H, H-AI, AI-H, AI-AI")
    # characters = ['A''B''C''D''E''F''G''H''I''J']


    def __init__(self, recommend=True):

        self.initialize_game()
        self.recommend = recommend

    def initialize_game(self):
        self.current_state = []
        # Player X always plays first
        self.player_turn = 'X'


    # def createBoard(self, n):
    #     for i in range(0, n):
    #         list = []
    #         for j in range(0, n):
    #             list.append('.')
    #         self.current_state.append(list)

    def createBoard(self, n):
        board = []
        for i in range(0, n):
            board.append(["." for c in range(0, n)])
        self.current_state = board
        return board

    # def draw_board(self):
    #     print()
    #     for y in range(0, self.size):
    #         for x in range(0, self.size):
    #             print(F'{self.current_state[x][y]}', end="")
    #         print()
    #     print()

    def draw_board(self):
        alphabet = string.ascii_uppercase
        alphabet_list = list(alphabet)
        alphabet_list.insert(0, " ")
        temp = self.current_state
        temp.insert(0, alphabet_list[:len(temp)+1])
        for r in range(len(temp)):
            if r > 0:
                temp[r].insert(0, str(r-1))
            for c in temp[r]:
                print(c, end=" ")
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
        if self.mode != "AI-AI":
            while True:
                print(F'Player {self.player_turn}, enter your move:')
                px = input('enter the x coordinate in letters: ')
                px.lower()
                orderNum = ord(px) - 97
                while (orderNum > self.n-1):
                    px = int(input('Warning! Invalid Number please enter it agian.'))
                    orderNum = ord(px) - 97
                px = orderNum
                py = int(input('enter the y coordinate: '))
                if self.is_valid(px, py):
                    return (px, py)
                else:
                    print('The move is not valid! Try again.')

        while True:
            print(F'Player {self.player_turn}, enter your move:')
            px = int(input('enter the x coordinate: '))
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
    def minimax(self,depth,useE2, max=False):
        value=10**(self.winSize+1)
        if max:
            value=-10**(self.winSize+1)
        x = None
        y = None
        result = self.is_end()
        if result == 'X':
            return (-1, x, y)
        elif result == 'O':
            return (1, x, y)
        elif result == '.':
            return (0, x, y)
        else:
            if depth!=0:
              if max:
                  return self.minimax(self,depth-1,useE2,max=False)
              else:
                  return self.minimax(self.depth-1,useE2,max=True)
            else:
                for i in range(0, 3):
                    for j in range(0, 3):
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
                return (value,x,y)
    def alphabeta(self,depth, useE2,alpha=-1000000,beta=1000000,max=False):
        value=10**(self.winSize+1)
        if max:
            value = -10**(self.winSize+1)
        x = None
        y = None
        result = self.is_end()
        if result == 'X':
            return (-10**self.winSize, x, y)
        elif result == 'O':
            return (10**self.winSize, x, y)
        elif result == '.':
            return (0, x, y)
        else:
            if depth!=0:
                if max:
                    return self.alphabeta(self,depth-1,useE2,max=False)
                else:
                    return self.alphabeta(self,depth-1,useE2,max=True)
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
                return (value, x, y)


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
    mode = int(input("Please enter a number to select the play mode(1 for H-H, 2 for H-AI, 3 for AI-H, 4 for AI-AI):"))
    if mode == 1:
        print("\n" + "Your choice is both player_X and player_O are human")
        d1 = 0
        d2 = 0
        t = 0
        a1 = 0
        a2 = 0
    else:
        if mode == 2:
            print("\n" + "Your choice is player_X is human and player_O is AI")
            d1 = 0
            d2 = input("What max depth of the adversarial search do you want to set for player_O?")
            t = input("What is the maximum allowed time(in seconds) you want to set for the game?")
            a1 = 0
            a2 = input("What method do you want player_O use? (return FALSE for minimax and TRUE for aplabeta)")
            e1 = input("Do you want player_O use e1?(return TRUE or FALSE)")

        else:
            if mode == 3:
                print("\n" + "Your choice is player_X is AI and player_O is human")
                d1 = input("What max depth of the adversarial search do you want to set for player_X?")
                d2 = 0
                t = input("What is the maximum allowed time(in seconds) you want to set for the game?")
                a1 = input("What method do you want player_X use? (return FALSE for minimax and TRUE for aplabeta)")
                a2 = 0

            else:
                print("\n" + "Your choice is both player_X and player_O are AI")
                d1 = input("What max depth of the adversarial search do you want to set for player_X?")
                d2 = input("What max depth of the adversarial search do you want to set for player_O?")
                t = input("What is the maximum allowed time(in seconds) you want to set for the game?")
                a1 = input("What method do you want player_X use? (return FALSE for minimax and TRUE for aplabeta)")
                a2 = input("What method do you want player_X use? (return FALSE for minimax and TRUE for aplabeta)")
                e1 = input("Do you want player_O use e1?(return TRUE or FALSE)")


    # number = str(n) + str(b) + str(s) + str(t)
    # name = " gameTrace-" + number.replace(" ", "") + ".txt"
    # print(name)
    # f = open(name, "x")
    # f.write("n=" + str(n) + " b=" + str(b) + " s=" + str(s) + " t=" + str(t) + "\n" + "\n")
    # f.write("blocs=" + str(listOfBlocs) + "\n" + "\n")
    # if mode == 1:
    #     f.write("Player 1: H " + "d=" + d1 + " a=" + a + " e1(regular)" + "\n")
    #     f.write("Player 1: H " + "d=" + d2 + " a=" + a + " e2(defensive)")
    # else:
    #     if mode == 2:
    #         f.write("Player 1: H " + "d=" + d1 + " a=" + a + " e1(regular)" + "\n")
    #         f.write("Player 1: AI " + "d=" + d2 + " a=" + a + " e2(defensive)")
    #     else:
    #         if mode == 3:
    #             f.write("Player 1: AI " + "d=" + d1 + " a=" + a + " e1(regular)" + "\n")
    #             f.write("Player 1: H " + "d=" + d2 + " a=" + a + " e2(defensive)")
    #         else:
    #             f.write("Player 1: AI " + "d=" + d1 + " a=" + a + " e1(regular)" + "\n")
    #             f.write("Player 1: AI " + "d=" + d2 + " a=" + a + " e2(defensive)")
    # f.write("\n")


if __name__ == "__main__":
    main()










