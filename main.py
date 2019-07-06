import json
from functions import *
from poolclasses import Game
import time

price_per_hour = 30.00
archive = Import_JSON()
games_list = archive
current_games = CG_Init()
Main_Menu()

