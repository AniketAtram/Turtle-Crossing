from turtle import Turtle
FONT = ("Courier", 14, "bold")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.player_score = 1
        self.penup()
        self.hideturtle()
        self.goto(-290, 270)

    def display_score(self):
        self.write(f"Level: {self.player_score}", font=FONT, align="left")

    def update_score(self):
        self.clear()
        self.player_score += 1
        self.write(f"Level: {self.player_score}", font=FONT, align="left")

    def game_over(self):
        self.clear()
        self.goto(0, 0)
        self.write(f"Game Over!", font=FONT, align="center")