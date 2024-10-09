class Board:
    def processInput(val):
        try:
            val = int(val) - 1
        except ValueError:
            print("Goodbye!")
            return None
        return val
    
    def __init__(self, board_size, win_con): 
        self.n = board_size
        self.k = win_con 
        self.board = [['_' for i in range(self.n)] for j in range(self.n)]
        self.turn = 0
        self.winner = None

    def makeMove(self, move, val):
        if self.isValidMove(move):
            for i in range(self.n - 1, -1, -1):
                if self.getBoardVal(i, move) == '_':
                    self.setBoardVal(i, move, val)
                    self.turn += 1
                    self.detectWinning(i, move)           
                    # check if the game is over
                    return
        else:
            newMove = self.processInput(input())
            self.makeMove(newMove, val)

    def detectWinning(self, row, col):
        stop1H = False
        stop2H = False
        stop1CountH = 0
        stop2CountH = 0

        stop1V = False
        stop2V = False
        stop1CountV = 0
        stop2CountV= 0

        stop1D1 = False
        stop2D1 = False
        stop1CountD1 = 0
        stop2CountD1 = 0

        stop1D2 = False
        stop2D2 = False
        stop1CountD2 = 0
        stop2CountD2 = 0

        val = self.getBoardVal(row, col)

        for i in range(self.n):
            if not stop1V:
                try: 
                    if self.getBoardVal(row-i, col) == val:
                        stop1CountV += 1
                    else: 
                        stop1V = True
                except IndexError:
                    stop1V = True
            if not stop2V:
                try: 
                    if self.getBoardVal(row+i, col) == val:
                        stop2CountV += 1
                    else: 
                        stop2V = True
                except IndexError:
                    stop2V = True

            if not stop1H:
                try: 
                    if self.getBoardVal(row, col-i) == val:
                        stop1CountH += 1
                    else: 
                        stop1H = True
                except IndexError:
                    stop1H = True
            if not stop2H:
                try: 
                    if self.getBoardVal(row, col+i) == val:
                        stop2CountH += 1
                    else: 
                        stop2H = True
                except IndexError:
                    stop2H = True

            if not stop1D1:
                try: 
                    if self.getBoardVal(row-i, col+i) == val:
                        stop1CountD1 += 1
                    else: 
                        stop1D1 = True
                except IndexError:
                    stop1D1 = True
            if not stop2D1:
                try: 
                    if self.getBoardVal(row+i, col-i) == val:
                        stop2CountD1 += 1
                    else: 
                        stop2D1 = True
                except IndexError:
                    stop2D1 = True

            if not stop1D2:
                try: 
                    if self.getBoardVal(row-i, col-i) == val:
                        stop1CountD2 += 1
                    else: 
                        stop1D2 = True
                except IndexError:
                    stop1D2 = True
            if not stop2H:
                try: 
                    if self.getBoardVal(row+i, col+i) == val:
                        stop2CountD2 += 1
                    else: 
                        stop2D2 = True
                except IndexError:
                    stop2D2 = True
            
        if stop1CountV + stop2CountV > self.k or stop1CountH + stop2CountH > self.k or stop1CountD1 + stop2CountD1 > self.k or stop1CountD2 + stop2CountD2 > self.k:
            self.winner = val
            return True
        
        return False

    def isValidMove(self, move):
        if move < 0 or move > self.n - 1:
            print("Only moves from 1 to", self.n, "are valid. Try again...")
            return False

        if self.getBoardVal(0, move) == '_':
            return True
        else:
            print("This column is full. Try a different column!")
            return False

    def getBoardVal(self, row, col):
        return self.board[row][col]
    
    def setBoardVal(self, row, col, val):
        self.board[row][col] = val

    def printBoard(self):
        print()
        print("---- Turn ", self.turn, " ----", sep="")
        for row in self.board:
            printableItem = ""
            for col in row:
                printableItem += col
                printableItem += " "
            print(printableItem)
        xAxis = ""
        for i in range(1,self.n + 1):
            xAxis += str(i)
            xAxis += " "
        print()
        print(xAxis)
        print()
        print("---------------")
        print()

    def processInput(self, val):
        try:
            val = int(val) - 1
        except ValueError:
            print("Goodbye!")
            return None
        return val