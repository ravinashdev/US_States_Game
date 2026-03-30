# IMPORTS
from turtle import Turtle
# CONSTANTS
MOVE = False
ALIGN = "center"
FONT = ("Courier", 12, "bold")
class StateWriter(Turtle):
    def __init__(self,state_name,state_x_coordinate,state_y_coordinate):
        super().__init__()
        self.penup()
        self.color("green")
        self.hideturtle()
        self.x = state_x_coordinate
        self.y = state_y_coordinate
        self.state_name = state_name
        self.write_state_on_map()
    def write_state_on_map(self):
        self.setposition(self.x, self.y)
        self.write(f"{self.state_name}",align=ALIGN,font=FONT)


