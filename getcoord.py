import turtle

screen = turtle.Screen()
screen.title("U.S States Game")

# path to image
image = "blank_states_img.gif"
screen.addshape(image)

# Create turtle w screen shape
turtle.shape(image)


# Create function to get x,y from screen on click so you know where states are
def get_mouse_click_coor(x, y):
    print(x, y)

# tell turtle to record coordinates when clicked
turtle.onscreenclick(get_mouse_click_coor)

# Keep screen open while clicking
turtle.mainloop()



