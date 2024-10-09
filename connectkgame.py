from board import Board

def main():
    board = Board(8, 4)
    playerXsTurn = True

    while (board.winner == None):
        print("Turn", board.turn)
        board.printBoard()

        if playerXsTurn:
            print("X's turn... Enter a column number from 1 to ", board.n, ":", sep="")
        else:
            print("O's turn... Enter a column number from 1 to ", board.n, ":", sep="")
            
        move = board.processInput(input())
        if move == None:
            return

        if playerXsTurn:
            board.makeMove(move, 'X')
        else:
            board.makeMove(move, 'O')
        playerXsTurn = not playerXsTurn

    board.printBoard()
    print("The winner is ", board.winner, ". Congratulations!", sep="")
    print("--Game over--")

if __name__=="__main__":
    main()