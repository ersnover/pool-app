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
    print(f"\nGame ID: {index}\nUser: {username}\nTable: {table_number}\n\nPress s to Start Game\nPress x to cancel and return to Table Manager")
    confirm = input(">> ")
    valid_input = False
    while valid_input == False:
        if confirm == 's' or confirm == 'S':
            new_game.Open_Game()
            games_list.append(new_game)
            current_games.append(new_game)
            valid_input = True
        elif confirm == 'x' or confirm == 'X':
            valid_input = True
            print("Game cancelled.")
            Table_Manager()
        else:
            print("Invalid input. Enter s or x.")

def Format_Time(time):
    total_minutes = int(time / 60)
    minutes = total_minutes % 60
    hours = int(total_minutes / 60)
    format_time = f"{str(hours)}:{str(minutes)}"
    return format_time

def Close_Game(table_number):
    for item in current_games:
        if item.table_number == table_number:
            game = item
            break
    print(f"Close game on Table {table_number}? (y/n)")
    valid_input = False
    while valid_input == False:
        confirm = input(">> ")
        if confirm == 'y' or confirm == 'Y':
            end_time = time.time()
            game.Close_Game(end_time)
            dicto = game.Game_to_Dict
            games_list[game.index] = dicto
            for i in range(0,len(current_games)):
                if current_games[i].table_number == table_number:
                    del current_games[i]
            valid_input = True
        elif confirm == 'n' or confirm == 'N':
            valid_input = True
            print("Returning to Table Manager.")
            Table_Manager()
        else:
            print("Invalid input. Enter y or n.")
    
   
    






archive = Import_JSON()
games_list = archive
current_games = []
# Main_Menu()
New_Game("05")
print("games list\n", games_list[0])
print("current games\n", current_games[0])
time.sleep(15)
Close_Game("05")
print("games list\n", games_list[0]["start_time"])
print("games list\n", games_list[0]["cost"])