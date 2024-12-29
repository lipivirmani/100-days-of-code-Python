import turtle as t
import random

t.colormode(255)
tim= t.Turtle()

dots_count=100
color_list= [(23, 16, 94), (232, 43, 6), (153, 14, 30), (41, 181, 158), (127, 253, 206), (237, 71, 166), (209, 179, 208), (246, 218, 21), (40, 133, 242), (244, 247, 253), (246, 218, 5), (207, 148, 178), (126, 155, 204), (106, 189, 174), (224, 134, 117), (81, 87, 136), (150, 64, 75), (209, 87, 66), (49, 44, 100), (244, 168, 154), (175, 184, 222), (111, 9, 23), (179, 30, 10)]

tim.speed('fastest')
tim.hideturtle()
tim.setheading(230)
tim.penup()
tim.forward(300)
tim.setheading(0)

for dot_count in range(1, dots_count+1 ):
    tim.dot(20,random.choice(color_list))
    # tim.penup()
    tim.forward(50)
    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)
screen= t.Screen()
screen.exitonclick()


# import colorgram
#
# rgb_colors= []
# colors = colorgram.extract('image.jpg', 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color= (r, g, b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)
