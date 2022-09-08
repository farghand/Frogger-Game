from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__(visible=False)
        self.penup()
        self.color("teal")
        self.shapesize(0.5)
        self.goto(-280, 260)
        self.level_number = 0
        self.update_level()

    def increase_level(self):
        self.level_number += 1
        self.update_level()

    def update_level(self):
        self.clear()
        self.write(f"Level: {self.level_number}", align="left", font=FONT)

    def game_over(self):
        self.home()
        self.write("GAME OVER", align="center", font=FONT)


