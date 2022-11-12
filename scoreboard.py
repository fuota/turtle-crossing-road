from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.color("black")
        self.goto(-250, 250)
        self.write(f"Level: {self.level}", font=FONT)

    def increase_level(self):
        self.level +=1
        self.clear()
        self.write(f"Level: {self.level}", font=FONT)

    def game_over(self):
        self.goto(-60, 0)
        self.write("GAME OVER", font=FONT)
