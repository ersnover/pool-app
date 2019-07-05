#open table creates Game object, close table converts Game object to dictionary and saves to .json file
import json
import time
price_per_hour = 30.00

class Game:
    def __init__(self, index, username, table_number):
        self.index = index
        self.username = username
        self.table_number = table_number
        self.start_time = ""
        self.end_time = ""
        self.total_time = ""
        self.cost = ""

    def Open_Game(self):
        self.start_time = round(time.time(),2)
        print(f"Table {self.table_number} opened.\nGame ID: {self.index}\nStart Time: {self.start_time}")

    def Close_Game(self):
        self.end_time = time.time()
        self.total_time = (self.end_time - self.start_time)
        self.cost = (self.total_time * price_per_hour)
        game_dict = self.__dict__

