import turtle

screen = turtle.Screen()
screen.title("U.S States Game")

image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)

# Create function to get x,y from screen on click
def get_mouse_click_coor(x, y):
    print(x,y)


turtle.onscreenclick(get_mouse_click_coor)

# Keep screen open while clicking
turtle.mainloop()



