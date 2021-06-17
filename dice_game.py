#Dice game

import random
import time
import sys

while True :
    def start():
        sum = 0
        counter = 0
        verification = 'y'
        while counter < 3 and verification == 'y' :
            dice_number = random.randint(1, 6)
            print('Computer is rolling a dice ',end ='')
            for i in range(3):
                time.sleep(random.random())
                print('...', end='')
            print(f'\nResult {dice_number}')
            sum += dice_number
            if sum >= 12 and counter == 2 :
                print(f'HURRAY! , You Win \nTotal Score is {sum}')
            elif counter == 2 :
                print(f'OPPS!!! , You Lose \nTotal score is {sum}')
            if counter < 2 :
                verification = input("Continue [Y/N] \n-->").lower()
            counter += 1
        else:
            if verification == 'n' :
                print('You exit from that game ')
            else :
                print('All three chances are over ')

    def stop():
        print('Game is terminated ')
        sys.exit(0)

    def help():
        print('''
    You have 3 chance to roll the dice 
    If the Sum of dice number is greater tham "12"
    then you win 
    otherwise lose
    ''')

    try:
        choice_list = int(input('\nEnter choice \n1.Start Game \n2.Exit Game\n3.Help\n--> '))
    except(ValueError):
        print('Your choice is not in numerical form ')
        sys.exit(0)
       
    if choice_list == 1 :
        start()
    elif choice_list == 2 :
        stop()
    elif choice_list == 3 :
        help()
    else :
        print('Wrong choice')
        sys.exit(0)
        
