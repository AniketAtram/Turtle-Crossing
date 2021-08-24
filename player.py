from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("turtle")
        self.color("darkgreen")
        self.setheading(90)
        self.goto(STARTING_POSITION)

    def move_forward(self):
        if self.ycor() < FINISH_LINE_Y:
            self.forward(MOVE_DISTANCE)
        else:
            print("Can't go forward! Limit reached")

    def reset_player_position(self):
        self.goto(STARTING_POSITION)