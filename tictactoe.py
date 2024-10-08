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
    possibleMoves = [x for x, letter in enumerate(board) if letter == ' ' and x != 0]
    move = 0

    for let in ['O', 'X']:
        for i in possibleMoves:
            boardCopy = board[:]
            boardCopy[i] = let
            if isWinner(boardCopy, let):
                move = i
                return move

    conersOpen = []
    for i in possibleMoves:
        if i in [1, 3, 7, 9]:
            conersOpen.append(i)

    if len(conersOpen) > 0:
        move = selectRandom(conersOpen)
        return move

    if 5 in possibleMoves:
        move = 5
        return move

    edgesOpen = []
    for i in possibleMoves:
        if i in [2, 4, 6, 8]:
            edgesOpen.append(i)

    if len(edgesOpen) > 0:
        move = selectRandom(edgesOpen)

    return move


def selectRandom(li):
    import random
    ln = len(li)
    r = random.randrange(0, ln)
    return li[r]


def isBoardFull(board):
    if board.count(' ') > 1:
        return False
    else:
        return True

def playAgain():
    global board
    response = input('Jogar novamente? (S/N): ')
    try:
        response = response.lower()
        if response == 'n':
            return False
        if response == 's':
            board = [' ' for x in range(10)]
            printBoard(board)
            return True
    except:
        print("Sua resposta deve ser S ou N!")
        return True


def main():
    print("Jogo da Velha")
    printBoard(board)

    while not (isBoardFull(board)):
        if not (isWinner(board, 'O')):
            playerMove()
            printBoard(board)
        else:
            print("O computador venceu!")
            if not playAgain():
                break

        if not (isWinner(board, 'X')):
            move = compMove()
            if move == 0:
                print('Empate!')
                if not playAgain():
                    break
            else:
                insertLetter('O', move)
                print('O computador colocou \'O\' na posição', move, ':')
                printBoard(board)
        else:
            print("Você venceu!")
            if not playAgain():
                break

    if isBoardFull(board):
        print("Empate!")

main()