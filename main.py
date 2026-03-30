# IMPORTS
import pandas as pd
import turtle
import time
from state_writer import StateWriter
from auto_state_writer import AutoStateWriter
from count_down_timer import CountDownTimer
# Import CONSTANTS from a global config file
import config
# CONSTANTS
DEFAULT_SCREEN_TITLE = config.DEFAULT_SCREEN_TITLE
DEFAULT_IMAGE = config.DEFAULT_IMAGE
DEFAULT_SLEEP_TIME = config.DEFAULT_SLEEP_TIME
DEFAULT_GAME_TIME = config.DEFAULT_GAME_TIME

# Initialize Screen Object
screen = turtle.Screen()
screen.title(DEFAULT_SCREEN_TITLE)
# Add shape to turtle class
screen.addshape(DEFAULT_IMAGE)
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

states_correctly_guessed = []
countdown = CountDownTimer(DEFAULT_GAME_TIME)

while config.GAME_ON:
    screen.update()
    time.sleep(DEFAULT_SLEEP_TIME)
    # Ask user for input via a screen popup text input and use title method to capitalize each word and strip miscellaneous spaces
    user_answer = screen.textinput(title=f"Guess A State Name {len(states_correctly_guessed)} / {number_of_states}", prompt="State Name?").title().strip()
    # Check the condition if user_answer is within the us_states_list created from the dataframe and not in
    # states already guessed to prevent getting double points for answering the same correct state twice
    if (user_answer in us_states_list) and (user_answer not in states_correctly_guessed):
        state_data = us_states_dataframe[us_states_dataframe["state"] == user_answer]
        # Retrieve the variables needed to create the StateWriter object with the correct arguments passed in
        state_name = state_data.state.to_string(index=False)
        state_x_coordinate = int(state_data.x.to_string(index=False))
        state_y_coordinate = int(state_data.y.to_string(index=False))
        StateWriter(state_name,state_x_coordinate,state_y_coordinate)
        states_correctly_guessed.append(state_name)
# Display all states missed when game has ended
auto_state_writer = AutoStateWriter(states_correctly_guessed, us_states_list, us_states_dataframe)
# Display a CSV report of all states missed, convert ot a dataframe and export as a CSV
states_missed_report = pd.DataFrame(auto_state_writer.states_missed, columns=["States Missed"])
states_missed_report.to_csv("states_missed.csv")
# Mainloop for timer to work independently
screen.mainloop()
# Screen exit on click
screen.exitonclick()