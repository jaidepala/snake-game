from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 18, "normal")

class Scorecard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0

        self.goto(220, 270)
        self.hideturtle()
        self.color("white")
        self.show_scorecard()

    def show_scorecard(self):
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def increment_score(self):
        self.score += 1
        self.clear()
        self.show_scorecard()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)
