# IMPORTS
from turtle import Turtle
# CONSTANTS
DEFAULT_ALIGN = "center"
DEFAULT_FONT = ("Courier", 24, "bold")


class CountDownTimer(Turtle):
    def __init__(self, seconds):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.setposition(0,300)
        self.color("black")
        self.seconds = seconds
        self.countdown(self.seconds)
    def countdown(self, seconds):
        self.clear()
        if seconds > 0:
            # Display current time
            self.write(seconds, align=DEFAULT_ALIGN, font=DEFAULT_FONT)
            # Schedule the next update in 1000ms (1 second)
            self.screen.ontimer(lambda: self.countdown(seconds - 1), 1000)
        else:
            self.write("TIME'S UP!", align="center", font=("Arial", 48, "bold"))
