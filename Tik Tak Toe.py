#!/usr/bin/env python
# coding: utf-8

# # Tik Tak Toe Game


import sys
import random
import time

class TikTakToe :
    def __init__(self):
        self.index_list = [' ',' ',' ',' ',' ',' ',' ',' ',' ']
        self.index_control_list = []
        self.player_name_list = []
        self.input_val = []
        self.p_no = 0
        self.player_list = [[],[]]
        self.multiple_choice()
        print("Welcome in the world of Tic Tak Toe Created by Satyam Tiwari")
        
    def com_choice_taker(self):
        com_choice_val = random.choice(self.com_list)
        self.com_list.remove(com_choice_val)
        return com_choice_val

    def com_player_name_taker(self):
        self.player_name_list.append(input(f"Enter Player name: "))
        self.player_name_list.append("Computer")
        
    def player_name_taker(self):
        for player_no in range(2):
            self.player_name_list.append(input(f"Enter Player{player_no+1} name: "))
            
    def com_input_symbol_taker(self):
        user_symbol = input(f"{self.player_name_list[0]} enter your symbol : ")
        if user_symbol.upper() != 'X':
            self.input_val.append(user_symbol)
            self.input_val.append('X')
        elif user_symbol.upper() != 'O':
            self.input_val.append(user_symbol)
            self.input_val.append('O')
    
    def input_symbol_taker(self):
        for symb in range(2):
            self.input_val.append(input(f"{self.player_name_list[symb]} enter your symbol : "))
    
    def print_diagram(self,index_list_values=None):
        if index_list_values == None:
            index_list_values = self.index_list.copy()
        print(f'   |   |   ')
        print(f' {index_list_values[0]} | {index_list_values[1]} | {index_list_values[2]} ')
        print(f'   |   |   ')
        print(f'--- --- ---')
        print(f'   |   |   ')
        print(f' {index_list_values[3]} | {index_list_values[4]} | {index_list_values[5]} ')
        print(f'   |   |   ')
        print(f'--- --- ---')
        print(f'   |   |   ')
        print(f' {index_list_values[6]} | {index_list_values[7]} | {index_list_values[8]} ')
        print(f'   |   |   ')
        print()
        
    def com_input_index(self):
            if self.p_no == 0:
                index = int(input(f"{self.player_name_list[self.p_no]} Enter the index from 1 to 9 : "))
                if (index>0 and index<10) and index not in self.index_control_list:
                    self.index_control_list.append(index)
                    self.com_list.remove(index)
                    #previous
                    self.index_list[index-1] = self.input_val[self.p_no]
                    self.player_list[self.p_no].append(index)
                    self.print_diagram()
                    self.win_checker()
                    self.p_no += 1
                else:
                    print("Enter a valid index number ... ")
            else:
                if len(self.com_list)>0:
                    print("Computer's chance .......")
                    time.sleep(0.4)
                    computer_val = self.com_choice_taker()
                    self.index_control_list.append(computer_val)
                    self.index_list[computer_val-1] = self.input_val[self.p_no]
                    self.player_list[self.p_no].append(computer_val)
                    self.print_diagram()
                    self.win_checker()
                    self.p_no -= 1
            if len(self.index_control_list) == 9:
                print("OPPS! No one win this game....")
                sys.exit(0)

    def input_index(self):
        index = int(input(f"{self.player_name_list[self.p_no]} Enter the index from 1 to 9 : "))
        if (index>0 and index<10) and index not in self.index_control_list:
            self.index_control_list.append(index)
            if self.p_no == 0:
                self.index_list[index-1] = self.input_val[self.p_no]
                self.player_list[self.p_no].append(index)
                self.print_diagram()
                self.win_checker()
                self.p_no += 1
            else:
                self.index_list[index-1] = self.input_val[self.p_no]
                self.player_list[self.p_no].append(index)
                self.print_diagram()
                self.win_checker()
                self.p_no -= 1
            if len(self.index_control_list) == 9:
                print("OPPS! No one win this game....")
                sys.exit(0)
        else:
            print("Enter a valid index number ... ")

    def help_fun(self):
        print("Here a raw tic tok toe game index")
        help_index_list = list(range(1,10))
        self.print_diagram(help_index_list)
        print("This is a index order you can put your symbol according to these ....")
        
    def win_checker(self):
        win_index_list = ((1,2,3),(4,5,6),(7,8,9),(1,4,7),(2,5,8),(3,6,9),(1,5,9),(3,5,7))
        counter = 0
        for tuple_in_tuple in win_index_list:
            for tuple_val in tuple_in_tuple:
                if tuple_val in self.player_list[self.p_no]:
                    counter += 1
                else:
                    counter = 0
                    break
            if counter == 3:
                print(f"Hurrey.... {self.player_name_list[self.p_no]} win this match")
                sys.exit(0)
    
    def main_multi_fun(self):
        while True:
            choice = int(input('''
            Enter the choice :
            1.Start
            2.Stop
            3.Help
            '''))
            if choice == 1:
                self.player_name_taker()
                self.input_symbol_taker()
                self.print_diagram()
                while True:
                    self.input_index()
            elif choice == 2:
                break
            elif choice == 3:
                self.help_fun()
            else:
                print("Invalid Choice ... ")
        
    def main_single_fun(self):
        while True:
            choice = int(input('''
            Enter the choice :
            1.Start
            2.Stop
            3.Help
            '''))
            if choice == 1:
                self.com_list = list(range(1,10))
                self.com_player_name_taker()
                self.com_input_symbol_taker()
                self.print_diagram()
                while True:
                    self.com_input_index()
            elif choice == 2:
                break
            elif choice == 3:
                self.help_fun()
            else:
                print("Invalid Choice ... ")

                
    def multiple_choice(self):
        com_choice = int(input('''
        Way of playing :
        1. Single player
        2. Multi player
        '''))
        if com_choice == 1:
            self.main_single_fun()
        elif com_choice == 2:
            self.main_multi_fun()
        else:
            print("You Enter invalid choice....")
        
TikTakToe()





