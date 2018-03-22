##Complexity:
##    space: We need 2 variables to store 2 player's input so space complexity would
##            be O(2) which can be approximated to O(1).
##    Time: We are just checking the result using if elif statements so time complexity
##            would be O(1)

def find_winner():
    while True:
        user_1 = ''
        while user_1 not in ('rock','paper','scissor'):
            print('Please enter value among(rock, paper, scissors)!!')
            user_1 = input('User1, enter the input: ' ).lower() 

        user_2 = ''
        while user_2 not in ('rock','paper','scissor'):
            print('Please enter value among(rock, paper, scissors)!!')
            user_2 = input('User2, enter the input: ' ).lower() 

        if (user_1 == 'rock' and user_2 == 'scissors'):
            print('Congratulations User_1!!')
            return
        elif (user_2 == 'rock' and user_1 == 'scissors'):
            print('Congratulations User_2!!')
            return
        elif (user_1 == 'scissors' and user_2 == 'paper'):
            print('Congratulations User_1!!')
            return
        elif (user_2 == 'scissors' and user_1 == 'paper'):
            print('Congratulations User_2!!')
            return
        elif (user_1 == 'paper' and user_2 == 'rock'):
            print('Congratulations User_1!!')
            return
        elif (user_2 == 'paper' and user_1 == 'rock'):
            print('Congratulations User_2!!')
            return

find_winner()
        
        
