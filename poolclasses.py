#open table creates Game object, close table converts Game object to dictionary and saves to .json file
import json
import time

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

price_per_hour = 30.00
price_per_second = price_per_hour / 3600

class Game:
    def __init__(self, index, username, table_number):
        self.index = index
        self.username = username
        self.table_number = table_number
        self.start_time = ""
        self.format_start_time = ""
        self.end_time = ""
        self.format_end_time = ""
        self.total_time = ""
        self.format_total_time = ""
        self.cost = ""

    def Open_Game(self):
        self.start_time = round(time.time(),2)
        self.format_start_time = time.strftime("%I:%M %p")
        print(f"\nTable {self.table_number} opened.\nGame ID: {self.index}\nStart Time: {self.format_start_time}")

    def Game_to_Dict(self):
        dicto = {
            "index": self.index,
            "username": self.username,
            "table_number": self.table_number,
            "start_time": self.start_time,
            "end_time": self.end_time,
            "total_time": self.total_time,
            "cost": self.cost
            }
        return dicto

    def Close_Game(self, end_time):
        self.end_time = end_time
        self.format_end_time = time.strftime("%I:%M %p")
        self.total_time = self.end_time - self.start_time
        self.format_total_time = Format_Time(self.total_time)
        self.cost = round(self.total_time * price_per_second,2)
        print(f"Closing Table {self.table_number}" + "-" * 14, f"\nGame ID:{self.index}\nStart Time: {self.format_start_time}\nEnd Time: {self.format_end_time}\nTotal Time: {self.format_total_time}\nAmount Due: ${self.cost}")


