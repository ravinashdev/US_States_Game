# IMPORTS
import pandas as pd
import turtle
import time
# CONSTANTS
DEFAULT_SCREEN_TITLE = "US_States_Game"
DEFAULT_IMAGE = "blank_states_img.gif"
DEFAULT_SLEEP_TIME = 0.1

# Initialize Screen Object
screen = turtle.Screen()
screen.title(DEFAULT_SCREEN_TITLE)
# Add shape to turtle class
screen.addshape("blank_states_img.gif")
# Set entire shape of screen to image
turtle.shape(DEFAULT_IMAGE)
screen.tracer(0)

# Ask user for input via a screen popup text input
user_answer = screen.textinput(title="Guess A State Name" ,prompt="State Name?")


# Pandas Read CSV
us_states = pd.read_csv('50_states.csv')
us_states_list = us_states['state'].values.tolist()
print(us_states_list)

# Initialize Game
game_on = True
while game_on:
    screen.update()
    time.sleep(DEFAULT_SLEEP_TIME)


# Screen exit on click
screen.exitonclick()