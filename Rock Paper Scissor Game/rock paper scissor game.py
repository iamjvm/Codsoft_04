import random
user_score = 0
computer_score = 0
score_count = 0
new_game = 0
print('\n')
print('Welcome to play Rock - Paper  - Scissors  Game!\n')
print('Winning Rules: \n'
                        +' Rock vs Paper: Paper wins \n'
                        +' Rock vs Scissors: Rock wins \n'
                        +' Paper vs Scissors: Scissors wins \n'
                        +' The first in reach 6 points wins the battle \n')    
# declaring possible actions for user and computer
possible_actions = ['1 for Rock, 2 for Paper, 3 for Scissors']
print('Possible Actions:  \n'
                        +' 1 for Rock  \n' 
                        +' 2 for Paper  \n'
                        +' 3 for Scissors  \n')
while True:
    score_count != 1
    # taking an input from user
    print('\n')
    user_action = int(input('Choose an Action: '))
    while user_action < 1 or user_action > 3:
    # if user enters an invalid input get a loop
        user_action = int(input('Please choose a valid Action: '))
    # reporting user action selected
    if user_action == 1:
        user_action_name = 'Rock '
    elif user_action == 2:
        user_action_name = 'Paper '
    else:
        user_action_name = 'Scissors '
    print('Your choice is: ' + user_action_name)
    # taking an input from computer
    print('\nNow the computer chooses:')
    computer_action = random.randint(1, 3)
    if computer_action == 1:
        computer_action_name = 'Rock '
    elif computer_action == 2:
        computer_action_name = 'Paper '
    else:
        computer_action_name = 'Scissors '
    print("Computer choice is: " + computer_action_name)
    print('\n')
    print(user_action_name + " vs. " + computer_action_name)
    # reporting a tie
    if user_action == computer_action:
        print('It is a tie, you and the computer chose ' + user_action_name)
    # reporting winner according to action
    elif user_action == 1:
        if computer_action == 3:
            print('Rock smashes scissors! You win !')
            user_score += 1
        else:
            print('Paper covers rock! You lose ')
            computer_score += 1
    elif user_action == 2:
        if computer_action == 1:
            print('Paper covers rock! You win !')
            user_score += 1
        else:
            print('Scissors cuts paper! You lose .')
            computer_score += 1
    elif user_action == 3:
        if computer_action == 2:
            print('Scissors cuts paper! You win !')
            user_score += 1
        else:
            print('Rock smashes scissors! You lose .')
            computer_score += 1
    # Total of rounds played in total will also be displayed. 
    while True:    
        print('\n')
        if score_count == 5:
            print('There is a winner')
        if user_score >= 5:
            print(' You are the winner ')
        elif computer_score >= 5:
            print(' Computer is the winner ')
        print('Final Scores:')
        print(f'Computer:{computer_score}')
        print(f'User:{user_score}')
    # The Player can quit the game at any time
    # The player is asked to quit or restart the game
        print('\n')
        play_again = input(' Do you want to play again? Type Y if you wish to continue, otherwise type N: ')
        if play_again.lower() != "y":
            print (' See you next time')
        break