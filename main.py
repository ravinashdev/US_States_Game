# IMPORTS
import pandas as pd
from turtle import Turtle, Screen
import time
# CONSTANTS
DEFAULT_SCREEN_WIDTH = 750
DEFAULT_SCREEN_HEIGHT = 450
DEFAULT_SCREEN_COLOR = "white"
DEFAULT_SCREEN_TITLE = "US_States_Game"

# Initialize Screen Object
screen = Screen()
screen.setup(DEFAULT_SCREEN_WIDTH, DEFAULT_SCREEN_HEIGHT)
screen.bgcolor(DEFAULT_SCREEN_COLOR)
screen.title(DEFAULT_SCREEN_TITLE)
screen.bgpic("blank_states_img.gif")
screen.tracer(0)

# Pandas Read CSV
us_states = pd.read_csv('50_states.csv')
us_states_list = us_states['state'].values.tolist()
print(us_states_list)

# Initialize Game
game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)

# Screen exit on click
screen.exitonclick()