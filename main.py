from turtle import Screen
from paddle import Paddle
from ball import Ball
from score import Score
import time

# Create screen
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

game_on = True
player1 = Paddle("player1", (350, 0))
player2 = Paddle("player2", (-350, 0))
ball = Ball()
scoreboard = Score()

screen.listen()

screen.onkeypress(player1.up, "Right")
screen.onkeypress(player1.down, "Left")
screen.onkeypress(player2.up, "d")
screen.onkeypress(player2.down, "a")


while game_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()
# Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce("wall")
# Detect collision with paddle
    if (ball.distance(player1) < 50 and ball.xcor() > 330) or (ball.distance(player2) < 50 and ball.xcor() < -330):
        ball.bounce("paddle")
# Detect when paddle misses
    # Player 1 misses
    if ball.xcor() > 370:
        ball.reset_ball("player2")
        scoreboard.point("player2")
    # Player 2 misses
    if ball.xcor() < -370:
        ball.reset_ball("player1")
        scoreboard.point("player1")
# Detect a winner
    if scoreboard.l_score >= 5 or scoreboard.r_score >=5:
        game_on = False
        scoreboard.gameover()

screen.exitonclick()
