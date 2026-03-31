import turtle
from turtle import Screen,Turtle
from random import randint
screen = Screen()
screen.setup(width=800,height=600)
colors = ["red","yellow","green","blue","purple"]
turtle_names = ["Federico","Alberto","Pietro","Davide","Eleonora"]
y_positioning = [-200,-100,-0,100,200]
turtles_group= []
#---------------------------------- TURTLES ------------------------------------------------------
index1 = 0
for turtles in range(5):
    turtles = Turtle(shape="turtle")
    turtles.color(colors[index1])
    turtles.teleport(-(screen.window_width()/3),y_positioning[index1])
    turtles.penup()
    turtles_group.append(turtles)
    index1 += 1
#------------------------------------TURTLES NAME----------------------------------------------------------------------

for i in range(0,5):
    turtles_group[i].name = turtle_names[i]
#-------------------------------------PLACE BET------------------------------------------------------
user_bet=turtle.textinput(title="Place your bet",prompt="Who's gonna win, make your choice")
#---------------------------------------FINISH LINE----------------------------------------------------
finish_line = Turtle()
finish_line.color = "black"
finish_line.teleport(x = 380, y = -300)
finish_line.goto(x=380, y=300)
finish_line.hideturtle()
#---------------------------------------GAME ON--------------------------------------------
game_on = True

while game_on:
    for turtles in turtles_group:
        turtles.forward(randint(0,20))
        if turtles.xcor() > 380 :
            print(f"Game Over , the {turtles.pencolor()} turtle named {turtles.name} has won the game")
            game_on = False
if user_bet == turtles.color:
    print("You won , congrats!")
else:
    print("You lost")



screen.exitonclick()