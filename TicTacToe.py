import sys
theBoard = {'1': ' ', '2': ' ', '3': ' ',
            '4': ' ', '5': ' ', '6': ' ',
            '7': ' ', '8': ' ', '9': ' '}
def printBoard(board):
    print(board['1'] + '|' + board['2'] + '|' + board['3'])
    print('-+-+-')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-+-+-')
    print(board['7'] + '|' + board['8'] + '|' + board['9'])
def check(board):
    if((board['1']=='O' and board['2']=='O' and board['3']=='O') or (board['4']=='O' and board['5']=='O' and board['6']=='O') or (board['7']=='O' and board['8']=='O' and board['9']=='O') or (board['1']=='O' and board['4']=='O' and board['7']=='O') or (board['2']=='O' and board['5']=='O' and board['8']=='O') or (board['3']=='O' and board['6']=='O' and board['9']=='O') or (board['1']=='O' and board['5']=='O' and board['9']=='O') or (board['3']=='O' and board['5']=='O' and board['7']=='O')):
        print('Player O wins')
        sys.exit()
    if((board['1']=='X' and board['2']=='X' and board['3']=='X') or (board['4']=='X' and board['5']=='X' and board['6']=='X') or (board['7']=='X' and board['8']=='X' and board['9']=='X') or (board['1']=='X' and board['4']=='X' and board['7']=='X') or (board['2']=='X' and board['5']=='X' and board['8']=='X') or (board['3']=='X' and board['6']=='X' and board['9']=='X') or (board['1']=='X' and board['5']=='X' and board['9']=='X') or (board['3']=='O' and board['5']=='O' and board['7']=='O')):
        print('Player X wins')
        sys.exit()
    if(board['1']!=' ' and board['2']!=' ' and board['3']!=' ' and board['4']!=' ' and board['5']!=' ' and board['6']!=' ' and board['7']!=' ' and board['8']!=' ' and board['9']!=' '):
        print("It's a tie")
        sys.exit()

turn = 'X'
for i in range(9):
    printBoard(theBoard)
    print('Turn for ' + turn + '. Move on which space?')
    move = input()
    theBoard[move] = turn
    check(theBoard)
    if turn == 'X':
        turn = 'O'
    else:
        turn = 'X'
printBoard(theBoard)
