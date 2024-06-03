import turtle
import pandas as pd

ALIGNMENT = "center"
FONT = ("Calibri", 12, "normal")

screen = turtle.Screen()
screen.title("U.S States Game")

image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)

df = pd.read_csv("50_states.csv")
states = df["state"]
# print(type(states))

correct_states = 0

while correct_states == 0:
    choice = screen.textinput(title="Guess the State", prompt="Name a state!").title().strip()
    for state in states:

        if choice == state:
            # print(f"Correct: {choice}")
            label_x = int(df[df['state'] == state]['x'])
            label_y = int(df[df['state'] == state]['y'])
            label = turtle.Turtle()
            label.penup()
            label.hideturtle()
            label.goto(label_x, label_y)
            label.write(state, align=ALIGNMENT, font=FONT)
            correct_states += 1

    #print(f"States: {states}")

while 0 < correct_states < 50:
    choice = screen.textinput(title=f"{correct_states}/50 Guessed Correctly", prompt="Name a state!").title().strip()
    for state in states:

        if choice == state:
            # print(f"Correct: {choice}")
            label_x = int(df[df['state'] == state]['x'])
            label_y = int(df[df['state'] == state]['y'])
            label = turtle.Turtle()
            label.penup()
            label.hideturtle()
            label.goto(label_x, label_y)
            label.write(state, align=ALIGNMENT, font=FONT)
            correct_states += 1
    # print(correct_states)



screen.exitonclick()