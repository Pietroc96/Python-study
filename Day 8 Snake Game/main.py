from turtle import Screen, Turtle

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
snake_part_distance = 20
snake = []
#------------------------------------SNAKE CREATION ----------------------------------
for i in range (3):
    snake_part = Turtle()
    snake_part.shape("square")
    snake_part.color("white")
    snake_part.penup()
    snake_part.goto(y = 0,x= 0 -(i * snake_part_distance))
    snake.append(snake_part)

#-----------------------------------------------MOVEMENT---------------------------------

def go_fw() :
    snake.f(10)





























screen.exitonclick()