from turtle import Turtle


ALIGNMENT = "center"
FONT = ('courier', 40, 'normal')


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.scoreboard_update()


    def scoreboard_update(self):
        self.goto(-100, 200)
        self.write(self.l_score, align=ALIGNMENT, font=FONT)
        self.goto(100, 200)
        self.write(self.r_score, align=ALIGNMENT, font=FONT)


    def r_point(self):
        self.clear()
        self.r_score += 1
        self.scoreboard_update()


    def l_point(self):
        self.clear()
        self.l_score += 1
        self.scoreboard_update()


    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER!", align=ALIGNMENT, font=FONT)
