# import colorgram

# rgb_colors = []
# colors = colorgram.extract('hirst.jpg', 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     newcolor = (r,g,b)
#     rgb_colors.append(newcolor)
# print(rgb_colors)

color_list = [(226, 231, 235), (54, 108, 149), (225, 201, 108), (134, 85, 58), (229, 235, 234), (224, 141, 62), (197, 144, 171), (143, 180, 206), (137, 82, 106), (210, 90, 68), (232, 226, 194), (188, 78, 122), (69, 101, 86), (132, 183, 132), (65, 156, 86), (137, 132, 74), (48, 155, 195), (183, 191, 202), (232, 221, 225), (58, 47, 41), (47, 59, 96), (38, 44, 64), (106, 46, 54), (41, 
55, 48), (12, 104, 95), (118, 125, 145), (182, 194, 199), (215, 176, 187), (223, 178, 168), (54, 45, 52)]

import random
from turtle import Turtle, Screen, colormode
carl = Turtle()
colormode(255)      #setting rgb mode 255

carl.pensize(20)            # simply rearranging starting position 
carl.penup()
carl.backward(300)
carl.right(90)
carl.forward(220)
carl.left(90)

carl.pendown()
def strokeLine():
    for i in range(0, 11):
        carl.pencolor(random.choice(color_list))
        carl.penup()
        carl.forward(50)
        carl.pendown()
        carl.forward(0)

def nextline():
    carl.penup()
    carl.left(90)
    carl.forward(50)
    carl.left(90)
    carl.forward(50*11)
    carl.left(180)
    
for i in range(0,10):
    strokeLine()
    nextline()






screen = Screen()

screen.exitonclick()