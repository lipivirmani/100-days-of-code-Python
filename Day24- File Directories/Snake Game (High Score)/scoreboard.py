from turtle import Turtle
ALIGNMENT = 'center'
FONT = ('Courier New', 20, 'bold')


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as data:
            self.high_score = int(data.read())
        self.color('white')
        self.penup()
        self.goto(x=0, y=275)
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f'Score : {self.score} High Score: {self.high_score}', align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode='w') as data:
                data.write(f'{self.high_score}')
        self.score = 0
        self.update_score()

    def increase_score(self):
        self.score += 1
        self.update_score()
