# IMPORTS
import pandas as pd
import turtle
import time
# CONSTANTS
DEFAULT_SCREEN_TITLE = "US_States_Game"
DEFAULT_IMAGE = "blank_states_img.gif"

# Initialize Screen Object
screen = turtle.Screen()
screen.title(DEFAULT_SCREEN_TITLE)
screen.addshape("blank_states_img.gif")
turtle.shape(DEFAULT_IMAGE)
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