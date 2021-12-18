from turtle import Turtle
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("cyan")
        self.penup()
        self.x_move=10
        self.y_move=10
        self.time_delay=0.1





    def move(self):
        self.speed("slow")
        self.new_y=self.ycor()+self.y_move
        self.new_x=self.xcor()+self.x_move
        self.setx(self.new_x)
        self.sety(self.new_y)

    def bounce(self):
        self.y_move *= -1


    def bounce_back(self):
        self.x_move *= -1
        self.time_delay *=0.9
    def reset_position(self):
        self.goto(0,0)
        self.time_delay=0.1
        self.bounce_back()

