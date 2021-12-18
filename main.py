from turtle import Turtle ,Screen
from players import Players
from ball import Ball
from scoreborad import Score
from border import Borders
import time
STARTING_POSITIONS = [(500, 0), (-500, 0),]

screen=Screen()
screen.setup(width=1200,height=1000)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)
score = Score()
border = Borders()
border.outline()
score.score()
ball = Ball()

player_1 = Players(STARTING_POSITIONS[0])
player_2 = Players(STARTING_POSITIONS[1])


screen.listen()
screen.onkey(fun=player_1.go_up, key="Up")
screen.onkey(fun=player_1.go_down, key="Down")
screen.onkey(fun=player_2.go_up, key="w")
screen.onkey(fun=player_2.go_down, key="s")


def play_game():
    game_is_on=True

    while game_is_on:
        screen.update()
        ball.move()
        time.sleep(ball.time_delay)


        if ball.xcor() > 540:
            score.add_score_2()
            score.score()
            ball.reset_position()
            player_1.player_reset_1()
            player_2.player_reset_2()
            ball.bounce_back()

        if ball.xcor() < -540:
            score.add_score_1()
            score.score()
            ball.reset_position()
            player_1.player_reset_1()
            player_2.player_reset_2()
            ball.bounce_back()



        if ball.ycor() > 390 or ball.ycor() < -390:
            ball.bounce()


        if ball.xcor() > 475 and ball.distance(player_1) < 50 or ball.xcor()< -475 and ball.distance(player_2)<50 :
            ball.bounce_back()

play_game()






























screen.exitonclick()
