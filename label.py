from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Calibri", 12, "normal")


class Label(Turtle):
    def __init__(self, st_name, label_x, label_y):
        super().__init__()
        self.st_name = st_name
        self.penup()
        self.hideturtle()
        self.goto(label_x, label_y)
        self.add_label()

    def add_label(self):
        self.write(self.st_name, align=ALIGNMENT, font=FONT)
