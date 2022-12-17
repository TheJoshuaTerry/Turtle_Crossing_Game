from turtle import Turtle
FONT = ("Courier", 20, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.level = 1
        self.color('black')
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(-225, 270)
        self.write(f'Level: {self.level}', align='center', font=FONT)

    def next_level(self):
        self.level += 1
        self.update_score()

    def game_over(self):
        self.goto(0, 0)
        self.write('GAME OVER', align='center', font=FONT)