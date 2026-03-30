# IMPORTS
from turtle import Turtle
# CONSTANTS
MOVE = False
ALIGN = "center"
FONT = ("Courier", 12, "bold")
class AutoStateWriter(Turtle):
    def __init__(self, states_correctly_guessed, us_states_list, us_states_dataframe):
        super().__init__()
        self.penup()
        self.color("red")
        self.hideturtle()
        self.states_correctly_guessed = states_correctly_guessed
        self.us_states_list = us_states_list
        self.us_states_dataframe = us_states_dataframe
        self.states_missed = list(set(self.us_states_list) ^ set(self.states_correctly_guessed))
        self.auto_write_state_on_map()
    def auto_write_state_on_map(self):
        for each_state_missed in self.states_missed:
            state_data = self.us_states_dataframe[self.us_states_dataframe["state"] == each_state_missed]
            state_name = state_data.state.to_string(index=False)
            state_x_coordinate = int(state_data.x.to_string(index=False))
            state_y_coordinate = int(state_data.y.to_string(index=False))
            self.setposition(state_x_coordinate, state_y_coordinate)
            self.write(f"{state_name}",align=ALIGN,font=FONT)
    def states_missed(self):
        return self.states_missed.sort()
