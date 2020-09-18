print('\033[2J')
print('\033[1;0H', '-'*17, '   ')
print('\033[4;0H', '-'*17, '   ')

def printBoard(board):
    print('\033[6;0H  ' + str(board).replace('\n', '\n  '))

def printGeneration(generation):
    print('\033[2;0H', 'Generation:', generation, '   ')

def printGameNumber(game, max_games):
    print('\033[3;0H', 'Game:', game, '/', max_games, '      ')