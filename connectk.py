def gameRun(n, k):
# handles one instance of game running
    playerX = 'X'
    playerO = 'O'
    playerXsTurn = True
    board = createBoard(n)
    turn = 1
    gameOver = False
    while(not gameOver):
        print("Turn", turn)
        printBoard(board, False)
        if playerXsTurn:
            print("Player X's turn... Enter a column number from 1 to", n)
            move = input()
            if move == "#q" or type(move) != int:
                print("Goodbye!")
                return
            # insufficient safeguarding of type(move)
            # this should be handled in a function that can call makeMove()
            if move > n or move < 1:
                print("Only moves from 1 to", n, "are valid. Try again...")
                move = input()
            makeMove(playerX, move, board)
        else:
            print("Player O's turn...Enter a column number from 1 to", n)
            move = input()
            if move == "#q":
                print("Goodbye!")
                return
            if move > n or move < 1:
                print("Only moves from 1 to", n, "are valid. Try again... ")
                move = input()
            makeMove(playerO, move, board)
            print("One turn for player: ", playerO)
                
        playerXsTurn = not playerXsTurn
        turn += 1
        gameOver = isGameOver(board)[0]
        print("Is game over?", gameOver)
    print(gameOver)

def makeMove(player, col, board):
# for any given player and a board you can make a move 
    # print("Player:", player)
    # print("Column:", col)
    # print("Board:", board)
    
    print("Making move for:", player)
    print("Move made:", col)
    if not isValidMove(col, board):
        # prompt the player to input a new move
        print("Move is invalid. Col", col, "is full. Try again, player", player)
        # makeMove(player, col, board)
    else:
        # make move logic (change the board)
        return board

def isGameOver(board):
# returns (won or not, the player who won)
# checks if there are k slots in a row using checkX(board) functions
    winner = None
    won = False
    if (checkHorizontal(board))[0] or (checkVertical(board))[0] or (checkDiagonal(board))[0]:
        won = True
        res = [(checkHorizontal(board))[1], (checkVertical(board))[1], (checkDiagonal(board))[1]]
        for i in res:
            if i != None:
                winner = i
    # why is game over? returns (True, 'O')... because the checks are wrong.
    return won, winner

def checkHorizontal(board):
# checks if there are k slots in a row, horizontally
    return False, 'X'

def checkVertical(board):
# checks if there are k slots in a row, horizontally
    return False, 'O'

def checkDiagonal(board):
# checks if there are k slots in a row, on both diagonals
    return False, None

def isValidMove(col, board):
# checks if a move is valid
    return True

def createBoard(n):
# create a board of size N * N
    # board = [[n * '_'] * n]
    board = [['_' for i in range(n)] for j in range(n)]
    return board

def printBoard(board, gameEnded):
# can we identify the winning coordinates and make them capital case when we print the gameEnded board?
    if not gameEnded:
        print()
        print("----- Board -----")
        for line in board:
            printableItem = ""
            for i in range(len(line)):
                printableItem += line[i]
                printableItem += " "
            print(printableItem)
        xAxis = ""
        for i in range(1,len(board)+1):
            xAxis += str(i)
            xAxis += " "
        print()
        print(xAxis)
        print()
        print("-----------------")
        print()
    else: 
        print("Not yet developed.")
    

def testing():
    # printBoard(createBoard(4), False)
    # test flow of gameRun
    gameRun(8, 2)
    
def main():
    n = 4 # board size (width and height)
    k = 2 # condition to win
    # check that N and K are valid (K <= N) if user input used to determine game parameters
    testing()
    return
    gameRun(n, k)
    return

if __name__=="__main__":
    main()
