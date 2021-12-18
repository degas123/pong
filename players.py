from turtle import Turtle
UP = 90
DOWN = 270
STARTING_POSITIONS = [(500, 0), (-500, 0),]
MOVE_DIS = 20
class Players(Turtle):

    def __init__(self,pos):
        super().__init__()
        self.shape("square")
        self.color("green")
        self.penup()
        self.hideturtle()
        self.setpos(pos)
        self.shapesize(stretch_wid=5,stretch_len=1)
        self.showturtle()

    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)


    def player_reset_1(self):
        self.setpos(STARTING_POSITIONS[0])


    def player_reset_2(self):
        self.setpos(STARTING_POSITIONS[1])


































    #
    # def __init__(self):
    #     self.snake_length = 3
    #     self.snake_sections = []
    #     self.create_player_one()
    #
    #
    # def create_player_one(self):
    #     for snakes_pos in STARTING_POSITIONS:
    #         self.add_segment(snakes_pos)
    #
    # def add_segment(self,snakes_pos):
    #     sections = Turtle("square")
    #     sections.color("red")
    #     sections.penup()
    #     sections.setpos(snakes_pos)
    #     self.snake_sections.append(sections)
    #
    # def extend(self):
    #     self.add_segment(self.snake_sections[-1].position())
    #     self.snake_length += 1
    #
    # def move(self):
    #     for part_num in range(self.snake_length - 1, 0, -1):
    #         new_x = self.snake_sections[part_num - 1].xcor()
    #         new_y = self.snake_sections[part_num - 1].ycor()
    #         self.snake_sections[part_num].goto(new_x, new_y)
    #     self.head.forward(MOVE_DIS)
    #
    # def up(self):
    #     if self.head.heading() != DOWN:
    #         self.head.seth(UP)
    #
    # def down(self):
    #     if self.head.heading() != UP:
    #         self.head.seth(DOWN)
    #
    # def right(self):
    #     if self.head.heading() != LEFT:
    #         self.head.seth(RIGHT)
    #
    # def left(self):
    #     if self.head.heading() != RIGHT:
    #         self.head.seth(LEFT)
