import sys
import random
import time

while True :
    def start():
        colour_list = [ 'RED' , 'GREEN' , 'BLUE' , 'YELLOW' ]
        #colour_list = shuffle_colour(colour_list)
        coins = 0
        counter = 0
        while counter < 5 :
            colour_computer = random.choice(colour_list)
            print(' COMPUTER IS CHOOSING A COLOUR ', end = '')
            for i in range(3):
                time.sleep(random.random())
                print('...', end='')
            colour_user = input('\n ENTER YOUR COLOUR ').upper()
            if colour_user in colour_list :
                counter += 1
                if colour_user == colour_computer :
                    coins += 50
                    print(f' HURRAY , YOU WIN \nTotal Coins you get {coins} ')
                else :
                    print('OPPS!!! You Lose')
            else:
                print('Heyy, You entered wrong colour')
        else :
            print(f'All 5 Chances get over \nTotal coin you win is {coins}')
            
    #def shuffle_colour(colour_list):
    #    number = random.randint(1,5)
    #    for i in range(number):
    #        colour_list = random.shuffle(colour_list)
    #    return colour_list

    def stop():
        sys.exit(0)

    def help():
        print('''
    You have 5 chances 
        Computer choses a colour randomly
    if you choose a same colour 
        then you get +50 coins each time 
    ''')

    try :
        choice = int(input('Enter choice \n1.start the game \n2.Exit from the game \n3.Help\n --> '))
    except(ValueError):
        print('You Entered not a Numerical Value')
        sys.exit(0)
    if choice == 1 :
        start()
    elif choice == 2 :
        stop()
    elif choice == 3 :
        help()
    else :
        print('Wrong choice')
        sys.exit(0)