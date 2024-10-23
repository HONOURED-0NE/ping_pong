from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
import random
import time
from scoreboard import Scoreboard
screen = Screen()
screen.setup(width = 800, height = 600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    
    #Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    #Detect collision with r_paddle
    if ball.distance(r_paddle) < 60 and ball.xcor() > 320 or ball.distance(l_paddle) < 60 and ball.xcor() < -320:
        print (ball.distance(r_paddle))
        ball.bounce_x()
        ball.move_speed *= 0.9

    #Detect when rightpaddle misses
    if ball.xcor() > 380:
        ball.reset()
        ball.move_speed = 0.1
        scoreboard.l_point()        
    #Detect when left padlle misses
    if ball.xcor() < -380:
        ball.reset()
        scoreboard.r_point()
















screen.exitonclick()