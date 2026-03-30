from turtle import Turtle, Screen ,colormode
from ColorExtractor import ColorExtractor
from random import randint
from MyTurtle import MyTurtle
screen = Screen()
screen.screensize(800,800)
screen.setup(800,800)
colormode(255)
timmy = MyTurtle()
timmy.shape("arrow")
col_extractor = ColorExtractor()
colors = col_extractor.extract_colors("urlo di munch.jpg",30)
gap = 50
dot_size = 20
index = 0
start_y = -(screen.window_height() / 4)
for y in range (10):
    start_x = -(screen.window_width() / 4)
    for x in range(10):
        timmy.teleport(start_x, start_y)
        timmy.dot(dot_size,colors[randint(0,len(colors)-1)])
        start_x += gap
        index += 1
    start_y += gap




screen.exitonclick()

