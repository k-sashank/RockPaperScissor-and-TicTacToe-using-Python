import random, sys
print('ROCK, PAPER, SCISSORS')
wins = 0
losses = 0
ties = 0
while True:
        print('%s Wins, %s Losses, %s Ties' % (wins, losses, ties))
        while True:
            print('Enter your move: (r)ock (p)aper (s)cissors or (q)uit')
            playerMove = input()
            if playerMove == 'q':
                if wins>losses and wins>ties:
                    print("You Won!")
                elif wins<losses and ties<losses:
                    print("You Lost! Better luck next time!")
                else:
                    print("Everyone's a Winner!")
                sys.exit()
            if playerMove == 'r':
                print('ROCK versus...')
            elif playerMove == 'p':
                print('PAPER versus...')
            elif playerMove == 's':
                print('SCISSORS versus...')
            randomNumber = random.randint(1, 3)
            if randomNumber == 1:
                computerMove = 'r'
                print('ROCK')
            elif randomNumber == 2:
                computerMove = 'p'
                print('PAPER')
            elif randomNumber == 3:
                computerMove = 's'
                print('SCISSORS')
            if playerMove == computerMove:
                print('It is a tie!')
                ties = ties + 1
                break
            elif playerMove == 'r' and computerMove == 's':
                print('You win!')
                wins = wins + 1
                break
            elif playerMove == 'p' and computerMove == 'r':
                print('You win!')
                wins = wins + 1
                break
            elif playerMove == 's' and computerMove == 'p':
                print('You win!')
                wins = wins + 1
                break
            elif playerMove == 'r' and computerMove == 'p':
                print('You lose!')
                losses = losses + 1
                break
            elif playerMove == 'p' and computerMove == 's':
                print('You lose!')
                losses = losses + 1
                break
            elif playerMove == 's' and computerMove == 'r':
                print('You lose!')
                losses = losses + 1
                break
