from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen= Screen()
screen.bgcolor("black")
screen.setup(1000,800)
screen.title("PING PONG")
screen.tracer(0)

l_paddle = Paddle((-450, 0))
r_paddle= Paddle((450, 0))
ball = Ball()
score = Scoreboard()


screen.listen()
screen.onkey(key='Up', fun=r_paddle.go_up)
screen.onkey(key='Down', fun=r_paddle.go_down)
screen.onkey(key='w', fun=l_paddle.go_up)
screen.onkey(key='s', fun=l_paddle.go_down)

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # detecting collision
    if ball.ycor() > 380 or ball.ycor() < -380:
        ball.bounce_y()

    # detecting collision with the paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 430 or ball.distance(l_paddle) < 50 and ball.xcor() < -430:
        ball.bounce_x()

    # detecting if right paddle missed the ball
    if ball.xcor() > 480 :
        ball.reset_pos()

        score.l_point()
    # detecting if left paddle missed ball
    if ball.xcor() < -480:
        ball.reset_pos()
        score.r_point()


screen.exitonclick()
