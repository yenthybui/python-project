from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title("My Pong Game")
screen.tracer(0) # to turn off animation, but need to update screen

r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))

ball = Ball()
scoreboard = Scoreboard()

#set up the control
screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_is_on = True
while game_is_on: #for every refresh of the screen
    time.sleep(0.1) #to sleep between each update
    screen.update()
    ball.move()
    
    #detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
        
    #dectect collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()
        
    #detect right paddle miss
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.score_for_left()
        
    #detect left paddle miss
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.score_for_right()

screen.exitonclick()