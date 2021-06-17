import random
import sys


choices = ("STONE", "PAPER", "SCISSORS")
com_choice = ""
user_choice = ""
user_name =""
com_score = 0
user_score  = 0


def random_pick(choices_list):
    print("COMPUTER IS SELECTING CHOICE ..... ")
    return random.choice(choices_list)


def decision(com_score, user_score, com_choice, user_choice) :
    if (com_choice == "STONE" and user_choice == "SCISSORS") or (com_choice == "SCISSORS" and user_choice == "PAPER") or (com_choice == "PAPER" and user_choice == "STONE") :
            print("OPPS! YOU LOSE..")
            com_score += 1
            
    elif (com_choice == "STONE" and user_choice == "STONE") or (com_choice == "PAPER" and user_choice == "PAPER") or (com_choice == "SCISSORS" and user_choice == "SCISSORS"):
            print("Tie ...")
        
    else:
            user_score += 1
            print("You Win! Hurray...")        
        
    return com_score, user_score
        
            
def counter(name = "USER"):
    user_choice, com_choice = "", "" 
    com_score , user_score = 0, 0
    while user_score != 10 and com_score != 10 :
        user_choice = input(">> ").upper()
        if user_choice == "STONE" or user_choice == "PAPER" or user_choice == "SCISSORS" :
            com_choice = random_pick(choices)
            print(f"COMPUTER IS SELECTING A {com_choice}")
            com_score, user_score = decision(com_score, user_score, com_choice, user_choice)        
            print(f"COMPUTER SCORE : {com_score} \nUSER_SCORE : {user_score}")
        else:
            print("SORRY, something went wrong")
    else :
        if com_score == 10 :
            print(f"\n COMPUER WIN ! \nCOMPUTER SCORE {com_score} \nUSER SCORE {user_score}")
        else :
            print(f"\n {name} WIN ! \nCOMPUTER SCORE {com_score} \nUSER SCORE {user_score}")

if __name__ == "__main__" :
    
    print("\n     WELCOME, IN STONE PAPER SCISSOR GAME ......")
        
    while True:
        main_choice= input('''
Enter choices :
1. START
2. STOP
3. HELP
''')
        if main_choice == '1' :
            user_name = input("ENTER YOUR NAME .. ").upper()
            print(f"WELCOME {user_name}")
            counter(user_name)
            while True :
                again = input("PLAY AGAIN [Y/N] : ").upper()
                if again == 'Y':
                    counter(user_name)
                else :
                    sys.exit()
                
        elif main_choice == '2':
            sys.exit()
            
        elif main_choice == '3':
            print('''
     YOU HAVE 10 POINT
  BETWEEN YOU AND COMPUTER 
     WHICH SCORE IS MORE GET WIN .....       
    ''')
        else:
            print("SORRY, I CAN'T UNDERSTAND IT \n  YOU ENTER WRONG CHOICE")