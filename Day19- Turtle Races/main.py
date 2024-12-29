import turtle
from turtle import Turtle, Screen
import random

is_Race_on = False
screen = Screen()
screen.setup(width=500, height=500)
user_bet = screen.textinput(title='Make a bet', prompt= 'Which turtle will win the race? Choose a color(red,orange,yellow,green,blue,purple!')
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
y_positions = [-110, -70, -30, 10, 50, 90]
all_turtles = []

for turtle_index in range(0, 6):
    new_turtle = Turtle(shape='turtle')
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(x=-220, y=y_positions[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    is_Race_on = True

while is_Race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 220:
            is_Race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"Congratulations! You've won. {winning_color} turtle won the race")
            else:
                print(f"You lost! {winning_color} turtle won the race. ")

        random_dist = random.randint(0, 10)
        turtle.forward(random_dist)

screen.exitonclick()
