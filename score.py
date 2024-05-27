from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 75, "normal")


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.l_score, align=ALIGNMENT, font=FONT)
        self.goto(100, 200)
        self.write(self.r_score, align=ALIGNMENT, font=FONT)

    def point(self, player):
        if player == "player1":
            self.r_score += 1
        elif player == "player2":
            self.l_score += 1
        self.update_score()

    def gameover(self):
        gameover_message = Turtle()
        gameover_message.color("white")
        gameover_message.penup()
        gameover_message.hideturtle()
        gameover_message.goto(-250, 0)
        gameover_message.write("GAME OVER", font=FONT)
