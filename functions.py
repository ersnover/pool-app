import json
import time
from poolclasses import Game

def Import_JSON():
    try:
        with open("status.json") as file:
            archive = json.load(file)
    except json.decoder.JSONDecodeError:
        archive = []
    return archive

def Write_JSON():
    with open("status.json","w") as file:
        json.dump(archive,file)

def Print_Menu():
    print("Choose an option:\n1 -- Table Manager\n2 -- Create Report\n3 -- Export Report\nq -- Quit")

def Get_Menu_Choice():
    valid_choice = False
    while valid_choice == False:
        menu_choice = input(">> ")
        if menu_choice == 'q' or menu_choice == 'Q':
            print("Goodbye!")
            quit()
        try:
            menu_choice = int(menu_choice)
            if menu_choice == 1 or menu_choice == 2 or menu_choice == 3:
                valid_choice = True
            else:
                print("Please select a valid option")
        except ValueError:
            print("Please enter a number, or q to quit")
    return menu_choice

def Main_Menu():
    Print_Menu()
    choice = Get_Menu_Choice()
    if choice == 1:
        Table_Manager()
    if choice == 2:
        Create_Report()
    if choice == 3:
        Export_Report()

def Table_Manager():
    pass


def New_Game(table_number):
    print(f"\nOpening New Game on Table {table_number}\n" + "-"*28)
    index = len(games_list)
    username = input("Enter user's first initial and last name: ")
    new_game = Game(index, username, table_number)
    print(f"\nGame ID: {index}\nUser: {username}\nTable: {table_number}\nPress s to Start Game\nPress x to cancel and return to Table Manager")
    confirm = input(">> ")
    valid_input = False
    while valid_input == False:
        if confirm == 's' or confirm == 'S':
            new_game.Open_Game()
            games_list.append(new_game)
            valid_input = True
        elif confirm == 'x' or confirm == 'X':
            valid_input = True
            print("Game cancelled.")
            Table_Manager()
        else:
            print("Invalid input. Enter s or x.")







archive = Import_JSON()
games_list = archive
# Main_Menu()
New_Game("05")