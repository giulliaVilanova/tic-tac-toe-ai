board = [' ' for x in range(10)]

def insertLetter(letter, pos):
    board[pos] = letter

def spaceIsFree(pos):
    return board[pos] == ' '

def printBoard(board):
    print('   |   |   ')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |   ')
    print('-----------')
    print('   |   |   ')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |   ')
    print('-----------')
    print('   |   |   ')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |   ')

def isWinner(bo, le):
    return ((bo[7] == le and bo[8] == le and bo[9] == le) or
            (bo[4] == le and bo[5] == le and bo[6] == le) or
            (bo[1] == le and bo[2] == le and bo[3] == le) or
            (bo[1] == le and bo[4] == le and bo[7] == le) or
            (bo[2] == le and bo[5] == le and bo[8] == le) or
            (bo[3] == le and bo[6] == le and bo[9] == le) or
            (bo[1] == le and bo[5] == le and bo[9] == le) or
            (bo[3] == le and bo[5] == le and bo[7] == le))

def playerMove():
    run = True
    while run:
        move = input("Selecione uma posição para jogar (1-9): ")
        try:
            move = int(move)
            if move > 0 or move < 10:
                if spaceIsFree(move):
                    run = False
                    insertLetter('X', move)
                else:
                    print("Este espaço já está sendo ocupado!")
            else:
                print("Por favor digite um número entre 1 e 9!")
        except:
            print("Por favor, digite um número!")

def compMove():
    pass

def selectRandom(board):
    pass

def isBoardFull(board):
    if board.count(' ') > 1:
        return True
    else:
        return False

def main():
    print("Jogo da Velha")
    printBoard()

    while not(isBoardFull(board)):
        if not (isWinner(board, 'O')):
            playerMove()
            printBoard()
        else:
            print("O computador venceu!")
            break

        if not (isWinner(board, 'X')):
            compMove()
            printBoard()
        else:
            print("Você venceu!")
            break

    if isBoardFull(board):
        print("Empate!")
main()
printBoard(board)
