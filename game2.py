#Game of dice

import time
import random
import sys

def start() :
    
    sums = 0
    counter = 0
    
    while counter < 3:
        counter += 1
        number = random.randint(1,6)
        sums += number
        print(' Dice is Rolling .... ')
        time.sleep(1)
        print("Dice will rolled and the number will come is : ", number)
        
        if sums > 12 and counter == 2 :
            print(" Hurray YOU WON ")

    else :
        print("OPPS! YOU LOSE", end='\n')

def stop() :
    print('Game will be terminated\n')
    sys.exit(0)
    
def help():
    print('''You have 3 chance to roll the dice 
if the sumss of three roll in the dice is more than 12 
then YOU "WIN"
OTHERWISE
  LOSE 
 ''')

ready = input("Ready for game [Y/N] ").lower()

if ready == 'y' :
    print('''
1. Start the game
2. Exit from the game
3. Help 
 ''')

    try :
        choice = int(input('Enter your choice '))
        if choice == 1 :
            start()
        elif choice == 2 :
            stop()
        elif choice == 3 :
            help()
        else :
            print('Wrong choice entered ')
    
    except(ValueError):
        print('Entered choice is not number ! ')

else :
    print('Game will be terminated\n')
    sys.exit(0)
