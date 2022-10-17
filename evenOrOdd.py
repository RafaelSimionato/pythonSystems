# Even or Odd Game

# This is an Odd or Even game. In this game, the player can play odd or even against the computer
# The game ends when the player loses. The player's consecutive win total is shown at the end of the game

from random import randint
v = 0
while True:
    player = int(input('Enter a value: '))
    computer = randint(0, 10)
    total = player + computer
    tipe = ' '
    while tipe not in 'EO':
        tipe = str(input('Even or Odd? [E/O] ')).strip().upper()[0]
    print(f'You played {player} and the Computer {computer}. Total of {total}. ' ,end='')
    print('IT WAS EVEN' if total % 2 == 0 else 'IT WAS ODD')
    if tipe == 'E':
        if total % 2 == 0:
            print('YOU WON! ')
            v += 1
        else:
            print('YOU WERE DEFEATED! ')
            break
    elif tipe == 'O':
        if total % 2 == 1:
            print('YOU WON! ')
            v += 1
        else:
            print('YOU WERE DEFEATED! ')
            break
    print('LET´S PLAY AGAIN... ')
print(f'GAME OVER! YOU WON {v} TIMES')
