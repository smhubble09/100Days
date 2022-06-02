# import colorgram
from random import choice
import turtle as t
t.colormode(255)

# colors = colorgram.extract('./Day18/image.jpg', 30)
# rgb_colors = []
# for color in colors:
#     rgb_colors.append((color.rgb[0], color.rgb[1], color.rgb[2]))

# print(rgb_colors)

color_list = [(213, 151, 106), (248, 247, 74), (87, 244, 200), (41, 12, 179), (224, 115, 161), (160, 10, 76), (17, 181, 76), (31, 6, 90), (223, 49, 138), (151, 88, 43), 
(118, 98, 228), (84, 34, 13), (9, 97, 45), (85, 6, 38), (183, 182, 241), (71, 216, 90), (178, 45, 104), (47, 16, 249), (34, 142, 47), (155, 134, 215), (173, 9, 7), (75, 244, 249), 
(228, 166, 205), (234, 47, 43), (87, 74, 148), (6, 96, 100)]

#10x10 grid of dots
hirst = t.Turtle()
hirst.hideturtle()
hirst.speed(0)
hirst.penup()

y_coord = -300

for y in range(10): #vertical line
    hirst.setx(-300)
    hirst.sety(y_coord)
    y_coord += 50
    for x in range(10): #horizontal line
        hirst.dot(20, choice(color_list))
        hirst.forward(50)

screen = t.Screen()
screen.exitonclick()