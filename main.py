# IMPORTS
import pandas as pd
import turtle
import time
from state_writer import StateWriter
from count_down_timer import CountDownTimer
# CONSTANTS
DEFAULT_SCREEN_TITLE = "US_States_Game"
DEFAULT_IMAGE = "blank_states_img.gif"
DEFAULT_SLEEP_TIME = 0.1
DEFAULT_GAME_TIME = 300

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
# Count the number of states to keep score
number_of_states = int(len(us_states_list))

# Initialize Game
game_on = True
states_correctly_guessed = 0
countdown = CountDownTimer(30)
while game_on:
    screen.update()
    time.sleep(DEFAULT_SLEEP_TIME)
    # Ask user for input via a screen popup text input and use title method to capitalize each word
    user_answer = screen.textinput(title=f"Guess A State Name {states_correctly_guessed} / {number_of_states}", prompt="State Name?").title()
    # Check the condition if user_answer is within the us_states_list created from the dataframe
    if user_answer in us_states_list:
        state_data = us_states_dataframe[us_states_dataframe["state"] == user_answer]
        # Retrieve the variables needed to create the StateWriter object with the correct arguments passed in
        state_name = state_data.state.to_string(index=False)
        state_x_coordinate = int(state_data.x.to_string(index=False))
        state_y_coordinate = int(state_data.y.to_string(index=False))
        StateWriter(state_name,state_x_coordinate,state_y_coordinate)
        states_correctly_guessed += 1
# Screen exit on click
screen.mainloop()
screen.exitonclick()