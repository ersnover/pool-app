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

def Session_Init():
    archive = Import_JSON()
    games_list = archive
    current_games = []
    for i in range(0,12):
        current_games.append('Open')
    return archive, games_list, current_games

def Print_Menu():
    print("\nChoose an option:\n1 -- Table Manager\n2 -- Create Report\n3 -- Export Report\nq -- Quit")

def Get_Menu_Choice():
    valid_choice = False
    while valid_choice == False:
        menu_choice = input(">> ")
        if menu_choice == 'q' or menu_choice == 'Q':
            Menu_Quit()
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
    print("\n-----Table Manager-----")
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
    game_id = len(games_list)
    username = input("Enter username: ")
    new_game = Game(game_id, username, table_number)
    print(f"\nGame ID: {game_id}\nUser: {username}\nTable: {table_number}\n\nPress s to Start Game\nPress x to cancel and return to Table Manager")  
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

#Converts total time (in seconds) to HH:MM string for printing
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
            games_list[game.game_id] = dicto
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

def Menu_Quit():
    games_open = Open_Game_Check()
    if games_open == True:
        print("\nCannot quit while games are still open.\nm -- Main Menu\nf -- FORCE CLOSE all open games (will print game receipts).")
        valid_input = False
        while valid_input == False:
            confirm = input(">> ")
            if confirm == 'm' or confirm == 'M':
                valid_input = True
                Main_Menu()
            elif confirm == 'f' or confirm == 'F':
                valid_input = True
                FC_Interface()
            else:
                print("Invalid input. Enter m or f.")
    print("\nGoodbye!")
    archive = games_list
    Write_JSON()
    quit()


def Open_Game_Check():
    games_open = False
    for game in current_games:
        if game != 'Open':
            games_open = True
            break
    return games_open
    
def FC_Interface():
    open_games = []
    for i in range(12):
        if current_games[i] != 'Open':
            open_games.append(current_games[i])
    num = str(len(open_games))
    print(f'Force Close {num} open games? (y/n)')
    valid_input = False
    while valid_input == False:
        confirm = input(">> ")
        if confirm == 'y' or confirm == 'Y':
            valid_input = True
            Force_Close(open_games)
        elif confirm == 'n' or confirm == 'N':
            valid_input = True
            Menu_Quit()
        else:
            print("Invalid input. Enter y or n.")

def Force_Close(games):
    counter = 1
    for game in games:
        table_number = game.table_number
        table_index = Table_to_Index(table_number)
        end_time = time.time()
        game.Close_Game(end_time)
        dicto = game.Game_to_Dict()
        games_list[game.game_id] = dicto
        current_games[table_index] = 'Open'
        if counter < len(games):
            input("\nPress any button to close next table")
            counter += 1
        else:
            print("\nAll games Closed.")





    






archive, games_list, current_games = Session_Init()

# game1 = Game(0,"ESNOVER","04")
# game1.Open_Game()
# games_list.append(game1)
# current_games[3] = game1

# game2 = Game(1,"CCUSTER","09")
# game2.Open_Game()
# games_list.append(game2)
# current_games[8] = game2

# game3 = Game(2,"GSNOVER","01")
# game3.Open_Game()
# games_list.append(game3)
# current_games[0] = game3

Main_Menu()
