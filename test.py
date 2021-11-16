import  time
testList=[['.','.','O','.','.'],
          ['.','X','.','O','.'],
          ['O','X','X','X','O'],
          ['.','X','.','*','.'],
          ['.','O','.','.','.']]
class Test:
    size=5
    winSize=4
    def __init__(self, recommend=True):
        self.initialize_Test()
        self.recommend = recommend
    def initialize_Test(self):
        self.current_state = testList
        # Player X always plays first

    def is_end(self):
        for i in range(0, self.size):
            for j in range(0, self.size):
                # win in rows
                if self.current_state[i][j]=="*" or self.current_state[i][j]==".":
                    continue
                if i < self.size - (self.winSize - 1):
                    count=0
                    for x in range(0, self.winSize-1 ):
                        if (self.current_state[i + x][j] != self.current_state[i + x + 1][j]):
                            break
                        else:
                            count+=1
                            if count == self.winSize-1:
                                return self.current_state[i][j]


                if j < self.size - (self.winSize - 1):
                    count=0
                    for x in range(0, self.winSize - 1):
                        if (self.current_state[i][j + x] != self.current_state[i][j + x + 1]):
                            break
                        else:
                            count+=1
                            if count == self.winSize-1:
                                return self.current_state[i][j]


                if i < self.size - (self.winSize - 1) and j < self.size - (self.winSize - 1):
                    count=0
                    for x in range(0, self.winSize - 1):
                        if (self.current_state[i + x][j + x] != self.current_state[i + x + 1][j + x + 1]):
                            break
                        else:
                            count+=1
                            if count == self.winSize-1:
                                return self.current_state[i][j]


                if j > self.winSize - 2 and i < self.size - (self.winSize - 1):
                    count=0
                    for x in range(0, self.winSize - 1):
                        if (self.current_state[i + x][j - x] != self.current_state[i + x + 1][j - x - 1]):
                            break
                        else:
                            count+=1
                            if count == self.winSize-1:
                                return self.current_state[i][j]


        for i in range(0, self.size):
            for j in range(0, self.size):
                if self.current_state[i][j] == '.':
                    return None
        return '.'

    def e2(self):

        start = time.time()
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
                        if self.current_state[i][j] == 'O' or self.current_state[i][j] == '*':
                            value += 10 ** count
                        recordState = self.current_state[i][j]
                    elif recordState == 'O' and (self.current_state[i][j] != recordState or j == self.size - 1):
                        value += 10 ** count
                        if self.current_state[i][j] == 'X' or self.current_state[i][j] == '*':
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
                        if self.current_state[j][i] == 'O' or self.current_state[j][i] == '*':
                            value += 10 ** count
                        recordState = self.current_state[j][i]
                    elif recordState == 'O' and (self.current_state[j][i] != recordState or j == self.size - 1):
                        value += 10 ** count
                        if self.current_state[j][i] == 'X' or self.current_state[j][i] == '*':
                            value -= 10 ** count
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
                        if self.current_state[x][i + x] == 'O' or self.current_state[x][i + x] == '*':
                            value += 10 ** count
                        recordState = self.current_state[x][i + x]
                    elif recordState == 'O' and (self.current_state[x][i + x] != recordState or x == self.size - i - 1):
                        value += 10 ** count
                        if self.current_state[x][i + x] == 'X' or self.current_state[x][i + x] == '*':
                            value -= 10 ** count
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
                        if self.current_state[i + x][x] == 'O' or self.current_state[i + x][x] == '*':
                            value += 10 ** count
                        recordState = self.current_state[i + x][x]
                    elif recordState == 'O' and (self.current_state[i + x][x] != recordState or x == self.size - i - 1):
                        value += 10 ** count
                        if self.current_state[i + x][x] == 'X' or self.current_state[i + x][x] == '*':
                            value -= 10 ** count
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
                        if self.current_state[i - x][x] == 'O' or self.current_state[i - x][x] == '*':
                            value += 10 ** count
                        recordState = self.current_state[i - x][x]
                    elif recordState == 'O' and (self.current_state[i - x][x] != recordState or x == i):
                        value += 10 ** count
                        if self.current_state[i - x][x] == 'X' or self.current_state[i - x][x] == '*':
                            value -= 10 ** count
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
                        if self.current_state[x + i][self.size - 1 - x] == 'O' or self.current_state[x + i][
                            self.size - 1 - x] == '*':
                            value += 10 ** count
                        recordState = self.current_state[x + i][self.size - 1 - x]
                    elif recordState == 'O' and (self.current_state[x + i][self.size - 1 - x] != recordState or x == i):
                        value += 10 ** count
                        if self.current_state[x + i][self.size - 1 - x] == 'X' or self.current_state[x + i][
                            self.size - 1 - x] == '*':
                            value -= 10 ** count
                        recordState = self.current_state[x + i][self.size - 1 - x]
                    else:
                        recordState = self.current_state[x + i][self.size - 1 - x]
                    count = 0
        end = time.time()

        return value
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
def main():
    test=Test(recommend=True)
    print(test.e2())
    print(-20**2)
if __name__ == "__main__":
	main()

