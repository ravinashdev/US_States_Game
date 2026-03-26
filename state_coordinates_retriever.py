import turtle
# Function to print (x,y) coordinate in console when clicking and not closing the screen to record state x,y coordinates and store them
def get_mouse_click_coordinate(x,y):
    print(x,y)
turtle.onscreenclick(get_mouse_click_coordinate)
# Keeps the window open
turtle.mainloop()