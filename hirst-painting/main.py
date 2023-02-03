# import colorgram
# colors = colorgram.extract("image.jpeg", 96)
# rgb_colors = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)

import random
from turtle import Turtle, Screen
color_list = [(19, 112, 165), (217, 149, 94), (204, 68, 26), (185, 15, 41), (218, 74, 101), (225, 206, 101), (216, 126, 161), (168, 48, 87), (24, 39, 150), (22, 171, 197), (24, 188, 126), (118, 171, 201), (204, 154, 21), (22, 132, 47), (14, 13, 80), (212, 9, 6), (206, 86, 72), (228, 206, 9), (238, 164, 179), (112, 196, 160), (138, 222, 172), (7, 103, 23), (241, 168, 158), (7, 44, 17), (128, 110, 183), (140, 216, 225), (176, 181, 226), (107, 106, 7), (87, 13, 27), (97, 8, 6), (5, 110, 115), (251, 6, 20), (251, 10, 6)]

screen = Screen()
screen.colormode(255)

titty = Turtle()
titty.shape("turtle")
titty.speed(0)
titty.up()
titty.hideturtle()
titty.goto(-225, -225)
titty.seth(0)

for x in range(1,11):
    for y in range(10):
        titty.dot(20, random.choice(color_list))
        titty.forward(50)
    titty.goto(-225, -225+50*x)

screen.exitonclick()
