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

#-----------------------------------------------MOVEMENT DEF---------------------------------

def go_fw() :
    for snakes in snake:
        snakes.forward(10)


def go_bk() :
    for snakes in snake:
        snakes.back(10)

def go_left() :
    for snakes in snake:
        snakes.left(90)
        snakes.forward(10)
def go_right() :
    for snakes in snake:
        snakes.right(90)
        snakes.forward(10)

#-----------------------------------PLAYING-----------------------------------------

screen.listen()
screen.onkeyrelease(go_left, "Left")
screen.onkeyrelease(go_bk, "Down")
screen.onkeyrelease(go_fw, "Up")
screen.onkeyrelease(go_right, "Right")

























screen.exitonclick()