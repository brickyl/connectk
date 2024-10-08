def gameRun(n, k):
    playerX = 'X'
    playerO = 'O'
    playerXsTurn = True
    board = createBoard(n)
    turn = 1
    gameOver = False
    winner = ""

    while(not gameOver):
        print("Turn", turn)
        printBoard(board, turn)
        if playerXsTurn:
            player = playerX
        else: player = playerO
        print(player, "'s turn... Enter a column number from 1 to ", n, ":", sep="")
        move = input()
        try:
            move = int(move) - 1
        except ValueError:
            print("Goodbye!")
            return
        board = makeMove(player, move, board) 
        if board == None:
            return
        gameOverData = isGameOver(board, k)
        gameOver = gameOverData[0]
        winner = gameOverData[1]
        if not gameOver:
            playerXsTurn = not playerXsTurn
            turn += 1
    printBoard(board, turn)
    print("The winner is ", winner, ". Congratulations!", sep="")
    print("--Game over--")

def isValidMove(move, board):
# col is an integer
# checks if a move is valid... two conditions
# 1. the column must be valid
# 2. the column must be open
    n = len(board)

    if move < 0 or move > n - 1:
        print("Only moves from 1 to", n, "are valid. Try again...")
        return False
    else:
        colMax = len(board)
        for r in range(len(board)):
            colCt = 0
            for c in range(len(board[0])):
                if r == move:
                    item = board[c][r]
                    if item == 'X' or item == 'O':
                        colCt += 1
            if colCt == colMax:
                print("This column is full. Try a different column!")
                return False
    return True

def makeMove(player, col, board):
# for any given player and a board you can make a move 
    if not isValidMove(col, board):
        newMove = input()
        try:
            newMove = int(newMove) - 1
        except ValueError:
            print("Goodbye!")
            return
        return makeMove(player, newMove, board) 
    else:
        colHeight = 0
        for r in range(len(board)-1, -1, -1):
            for c in range(len(board[0])):
                if c == col and board[r][c] != '_':
                    colHeight += 1
        boardHeight = len(board)
        rowNum = boardHeight - colHeight
        board[rowNum - 1][col] = player
        return board

def isGameOver(board, k):
# returns (won or not, the player who won)
# checks if there are k slots in a row using checkX(board) functions
# another way to do this could be using - take any element and see if there are 4 adjacent same elements in a line in any direction
    winner = None
    won = False
    horiz = checkHorizontal(board, k)
    vert = checkVertical(board, k)
    diag = checkDiagonal(board, k)
    if horiz[0] or vert[0] or diag[0]:
        won = True
        res = [horiz[1], vert[1], diag[1]]
        for i in res:
            if i != None:
                winner = i
    return won, winner

def checkHorizontal(board, k):
# checks if there are k slots in a row, horizontally
    for row in board:
        consecutive = 1
        currVal = '_'
        for item in row:
            if currVal == item:
                consecutive += 1
            else:
                currVal = item
                consecutive = 1 
            if consecutive >= k and currVal != '_':
                return True, currVal
    else:
        return False, None


def checkVertical(board, k):
# checks if there are k slots in a row, horizontally
    for r in range(len(board)):
        consecutive = 1
        currVal = '_'
        for c in range(len(board[0])):
            item = board[c][r]
            if currVal == item:
                consecutive += 1
            else:
                currVal = item
                consecutive = 1 
            if consecutive >= k and currVal != '_':
                return True, currVal
    else:
        return False, None

def checkDiagonal(board, k):
# checks if there are k slots in a row, on both diagonals
# check bottom-left to upper-right direction diagonals /
    for c in range(len(board[0])):
        upDiags1 = [] 
        currVal = '_'
        counter = 1
        for r in range(c+1):
            upDiags1.append(board[r][c-r])
        # check upDiags for similarity
        for val in upDiags1:
            if val != '_' and val == currVal:
                counter += 1
                if counter >= k:
                    return True, currVal
            else:
                currVal = val
                counter = 1
        
    for r in range(len(board)):
        startC = len(board[0]) - 1
        upDiags2 = []
        for c in range(startC):
            if r + c <= len(board) - 1:
                upDiags2.append(board[r+c][startC-c])
        # check upDiags for similarity
        for val in upDiags2:
            if val != '_' and val == currVal:
                counter += 1
                if counter >= k:
                    return True, currVal
            else:
                currVal = val
                counter = 1
    
# check upper-left to bottom-right direction diagonals \
    for r in range(len(board)):
        coords = []
        for iterator in range(len(board[0])-r):
            coords.append((r+iterator, iterator))

        swapped = []
        currVal = '_'
        counter = 1
        for crd in coords:
            crdR = crd[0]
            crdC = crd[1]
            swapped.append((crdC, crdR))

        coordsVals = []
        swappedVals = []
        for c in coords:
            c0 = c[0]
            c1 = c[1]
            coordsVals.append(board[c0][c1])
            
        for c in swapped:
            c0 = c[0]
            c1 = c[1]
            swappedVals.append(board[c0][c1])
        
        for item in coordsVals:
            if item == currVal and item != '_':
                counter += 1
                if counter >= k:
                    return True, currVal
            else:
                currVal = item
                counter = 1

        currVal = '_'
        counter = 1
        for item in swappedVals:
            if item == currVal and item != '_':
                counter += 1
                if counter >= k:
                    return True, currVal
            else:
                currVal = item
                counter = 1  
    return False, None


def createBoard(n):
# create a board of size N * N
    board = [['_' for i in range(n)] for j in range(n)]
    return board

def printBoard(board, turnNum):
    print()
    print("---- Turn ", turnNum, " ----", sep="")
    for row in board:
        printableItem = ""
        for col in row:
            printableItem += col
            printableItem += " "
        print(printableItem)
    xAxis = ""
    for i in range(1,len(board)+1):
        xAxis += str(i)
        xAxis += " "
    print()
    print(xAxis)
    print()
    print("---------------")
    print()

    
def main():
    n = 5 # board size (width and height)
    k = 4 # condition to win
    # check that N and K are valid (k <= n) if user input used to determine game parameters
    if k <= n:
        gameRun(n, k)

if __name__=="__main__":
    main()
