##Generate a random number between 1 and 9 (including 1 and 9). Ask the user to guess the number,
##then tell them whether they guessed too low, too high, or exactly right.

import random

def guessing_game():
    while True:
        num = 0
        while num not in range(1,10):
            num = input('Enter number between 1 to 9:')

        game_num = random.randint(1,9)
        print 'Your Number: ' + str(num)
        print 'Generated Number: ' + str(game_num)
        
        if num == game_num:
            return 'Congrats!! You guessed it right...'
        elif abs(num - game_num) <= 2:
            return 'You were so close!'
        elif abs(num - game_num) >= 3:
            return 'You were not close!'


result = guessing_game()
print result
