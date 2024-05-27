from turtle import Turtle
import random
SHAPE = "circle"
COLOUR = "white"
MOVE_DISTANCE = 5


def rand_direction():
    return random.randint(0, 359)


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape(SHAPE)
        self.color(COLOUR)
        self.penup()
        self.setheading(rand_direction())
        self.move_speed = 0.01

    def move(self):
        self.forward(MOVE_DISTANCE)

    def bounce(self, collision_type):
        collision_angle = self.heading() % 180
        if collision_type == "wall":
            new_heading = 360 - self.heading()
        elif collision_type == "paddle":
            if self.heading() > 180:
                new_heading = 360 - collision_angle
            else:
                new_heading = 180 - collision_angle
        self.setheading(new_heading)
        self.move_speed *= 0.9

    def reset_ball(self, to_player):
        self.goto(0, 0)
        direction = rand_direction()
        if to_player == "player1":
            if not (0 <= direction < 90 or 270 < direction < 360):
                direction += 180
        elif to_player == "player2":
            if not (90 <= direction <= 270):
                direction += 180
        self.setheading(direction)
        self.move_speed = 0.01

    def increase_speed(self):
        self.move_speed = self.move_speed / 10
