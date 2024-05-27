from turtle import Turtle
UP = 0
DOWN = 180
SHAPE = "square"
COLOUR = "white"
MOVE_DISTANCE = 20
STOP_DISTANCE = 0


class Paddle(Turtle):
    def __init__(self, player, position):
        super().__init__()
        self.player = player
        self.shape(SHAPE)
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.color(COLOUR)
        self.penup()
        self.goto(position)

    def up(self):
        if self.ycor() <= 230:
            new_y = self.ycor() + MOVE_DISTANCE
            self.goto(self.xcor(), new_y)

    def down(self):
        if self.ycor() >= -230:
            new_y = self.ycor() - MOVE_DISTANCE
            self.goto(self.xcor(), new_y)

    def stop(self):
        self.forward(STOP_DISTANCE)
