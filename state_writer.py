# IMPORTS
from turtle import Turtle
# CONSTANTS
MOVE = False
ALIGN = "center"
FONT = ("Courier", 12, "bold")
class StateWriter(Turtle):
    def __init__(self,x_coordinate,y_coordinate,state_name):
        super().__init__()
        self.penup()
        self.color("green")
        self.x = x_coordinate
        self.y = y_coordinate
        self.state_name = state_name
        self.write_state()
    def write_state(self):
        self.write(f"{self.state_name}",align=ALIGN,font=FONT)
        self.setposition(self.x,self.y)