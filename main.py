# IMPORTS
import pandas as pd
import turtle
import time
from state_writer import StateWriter
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

# Pandas Read CSV
us_states = pd.read_csv('50_states.csv')
us_states_dataframe = pd.DataFrame(us_states)
# Create a list from the dataframe of states
us_states_list = us_states_dataframe["state"].tolist()

# Initialize Game
game_on = True
while game_on:
    screen.update()
    time.sleep(DEFAULT_SLEEP_TIME)
    # Ask user for input via a screen popup text input and use title method
    user_answer = screen.textinput(title="Guess A State Name", prompt="State Name?").title()
    # Check the condition if user_answer is within the us_states_list created from the dataframe
    if user_answer in us_states_list:
        state_data = us_states_dataframe[us_states_dataframe["state"] == user_answer]
        # print(state_data.state.to_string(index=False))
        # print(state_data.x.to_string(index=False))
        # print(state_data.y.to_string(index=False))
        state_name = state_data.state.to_string(index=False)
        state_x_coordinate = int(state_data.x.to_string(index=False))
        state_y_coordinate = int(state_data.y.to_string(index=False))
        StateWriter(state_name,state_x_coordinate,state_y_coordinate)

# Screen exit on click
screen.exitonclick()