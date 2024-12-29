from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard

import time
screen= Screen()
screen.setup(600,600)
screen.bgcolor('black')
screen.title('SNAKE GAME')
screen.tracer(0)

snake = Snake()
food = Food()
score = Scoreboard()


screen.listen()
screen.onkey(key='Up', fun= snake.up)
screen.onkey(key='Down', fun=snake.down)
screen.onkey(key='Left', fun=snake.left)
screen.onkey(key='Right', fun=snake.right)
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    # buffering screen to make it slower and make snake look one piece only
    snake.move()
    # Detecting collision of food and Snake
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.increase_score()
    # Detect collision with wall
    if snake.head.xcor()> 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        game_is_on= False
        score.game_over()
    # Detecting collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on= False
            score.game_over()

screen.exitonclick()
