# IMPORTS
from turtle import Turtle
import config
from config import GAME_ON

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
            # Using divmod to return minutes_left and seconds_left in a tuple
            minutes_left, seconds_left = divmod(seconds, 60)
            # Display current time with a 1 leading zero in seconds and minutes
            self.write(f"Time Left: {minutes_left:02}:{seconds_left:02}", align=DEFAULT_ALIGN, font=DEFAULT_FONT)
            # Schedule the next update in 1000ms (1 second)
            self.screen.ontimer(lambda: self.countdown(seconds - 1), 1000)
        else:
            self.write("TIME'S UP!", align="center", font=("Arial", 48, "bold"))
            # Change config GAME_ON so game ends
            config.GAME_ON = False

