import turtle
import pandas as pd
from label import Label


screen = turtle.Screen()
screen.title("U.S States Game")

image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)

df = pd.read_csv("50_states.csv")
states = df["state"]

correct_states = 0

while correct_states < 50:
    if correct_states == 0:
        choice = screen.textinput(title="Guess the State", prompt="Name a state!").title().strip()
    else:
        choice = screen.textinput(title=f"{correct_states}/50 Guessed Correctly",
                                  prompt="Name a state!").title().strip()
    for state in states:
        if choice == state:
            label_x = int(df[df['state'] == state]['x'])
            label_y = int(df[df['state'] == state]['y'])
            label = Label(state, label_x, label_y)
            correct_states += 1


screen.exitonclick()
