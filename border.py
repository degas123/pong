from turtle import Turtle

class Borders(Turtle):

     def outline(self):
        line=Turtle()
        line.speed("fastest")
        line.hideturtle()
        line.color("red")
        line.penup()
        line.setpos(550,-410)
        line.pendown()
        line.setpos(550,410)
        line.setpos(-550,410)
        line.setpos(-550,-410)
        line.setpos(550,-410)
