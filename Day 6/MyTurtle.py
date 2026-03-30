from turtle import Turtle

class MyTurtle(Turtle):
    def __init__(self):
        super().__init__()

    def go_left(self,left_angle,forward_distance):
        self.left(left_angle)
        self.forward(forward_distance)
    def go_right(self,right_angle,forward_distance):
        self.right(right_angle)
        self.forward(forward_distance)