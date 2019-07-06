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
        json.dump(games_list,file)

def CG_Init():
    current_games = []
    for i in range(0,12):
        current_games.append('Open')
    return current_games

def Print_Menu():
    print("\nChoose an option:\n1 -- Table Manager\n2 -- Create Report\n3 -- Export Report\nq -- Quit")

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


def Print_Tables():
    for i in range (0,12):
        if i < 9:
            if current_games[i] == 'Open':
                print(f"Table 0{i + 1}: OPEN")
            else:
                print(f"Table 0{i + 1}: IN USE")
        else:
            if current_games[i] == 'Open':
                print(f"Table {i + 1}: OPEN")
            else:
                print(f"Table {i + 1}: IN USE")
    
def Get_Table_Choice():
    valid_choice = False
    while valid_choice == False:
        table_choice = input(">> ")
        if table_choice == 'm' or table_choice == 'M':
            Main_Menu()
        try:
            table_choice = int(table_choice)
            if table_choice >= 1 and table_choice <=12:
                valid_choice = True
            else:
                print("Please select a valid option")
        except ValueError:
            print("Please enter a number, or m to return to menu.")
    return table_choice

def Table_Manager():
    print("-----Table Manager-----")
    Print_Tables()
    print("\nEnter Table Selection\nm -- Return to Main Menu")
    choice = Get_Table_Choice()
    index = Table_to_Index(choice)
    View_Table(index)

def View_Table(table_index):
    table_number = Index_to_Table(table_index)
    if current_games[table_index] == 'Open':
        print(f"Start game on Table {table_number}? (y/n)")
        valid_input = False
        while valid_input == False:
            confirm = input(">> ")
            if confirm == 'y' or confirm == 'Y':
                valid_input = True
                New_Game(table_index)          
            elif confirm == 'n' or confirm == 'N':
                valid_input = True
                Table_Manager() 
            else:
                print("Invalid input. Enter s or x.")
    else:
        game = current_games[table_index]
        index = game.index
        username = game.username
        start_time = game.format_start_time
        current_duration = Format_Time(time.time() - game.start_time)
        print(f"--- Table {table_number} ---\nGame ID: {index}\nUser: {username}\nStart Time: {start_time}\nCurrent Duration: {current_duration}")
        print("Enter x to close game, or m to return to Table Manager.")
        valid_input = False
        while valid_input == False:
            confirm = input(">> ")
            if confirm == 'x' or confirm == 'X':
                valid_input = True
                Close_Game(table_index)          
            elif confirm == 'm' or confirm == 'M':
                valid_input = True
                Table_Manager() 
            else:
                print("Invalid input. Enter x or m.")


def Table_to_Index(table):
    index = int(table) - 1
    return index

def Index_to_Table(index):
    if index < 9:
        table = f"0{index + 1}"
    else:
        table = str(index + 1)
    return table
    

def New_Game(table_index):
    table_number = Index_to_Table(table_index)
    print(f"\nOpening New Game on Table {table_number}\n" + "-"*28)
    index = len(games_list)
    username = input("Enter user's first initial and last name: ")
    new_game = Game(index, username, table_number)
    print(f"\nGame ID: {index}\nUser: {username}\nTable: {table_number}\n\nPress s to Start Game\nPress x to cancel and return to Table Manager")  
    valid_input = False
    while valid_input == False:
        confirm = input(">> ")
        if confirm == 's' or confirm == 'S':
            new_game.Open_Game()
            games_list.append(new_game)
            current_games[table_index] = new_game
            valid_input = True
            Table_Manager()
        elif confirm == 'x' or confirm == 'X':
            valid_input = True
            print("Game cancelled.")
            Table_Manager()
        else:
            print("Invalid input. Enter s or x.")

def Format_Time(time):
    total_minutes = int(time / 60)
    minutes = str(total_minutes % 60)
    if len(minutes) < 2:
        minutes = "0" + minutes
    hours = str(int(total_minutes / 60))
    if len(hours) < 2:
        hours = "0" + hours
    format_time = f"{hours}:{minutes}"
    return format_time

def Close_Game(table_index):
    table_number = Index_to_Table(table_index)
    game = current_games[table_index]
    print(f"Close game on Table {table_number}? (y/n)")
    valid_input = False
    while valid_input == False:
        confirm = input(">> ")
        if confirm == 'y' or confirm == 'Y':
            end_time = time.time()
            game.Close_Game(end_time)
            dicto = game.Game_to_Dict()
            games_list[game.index] = dicto
            current_games[table_index] = 'Open'
            valid_input = True
            print(f"Return to Table Manager? (y/n)")
            valid_input2 = False
            while valid_input2 == False:
                confirm = input(">> ")
                if confirm == 'y' or confirm == 'Y':
                    valid_input2 = True
                    Table_Manager()
                elif confirm == 'n' or confirm == 'N':
                    time.sleep(5)
                    print(f"Ready yet? (y/n)")
                else:
                    print("Invalid input. Enter y or n.")
        elif confirm == 'n' or confirm == 'N':
            valid_input = True
            print("Returning to Table Manager.")
            Table_Manager()
        else:
            print("Invalid input. Enter y or n.")
    
   
    






archive = Import_JSON()
games_list = archive
current_games = CG_Init()
Main_Menu()
