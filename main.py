# classic game of Snake

from turtle import Screen
from snake import Snake
import time

screen = Screen()
screen.setup(width=600, height=600, startx=650, starty=300)

screen.bgcolor("black")
screen.title("Snake")
screen.tracer(0)  # Turn off automatic screen updates

snake = Snake()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

segments = snake.segments 

game_is_on = True

while game_is_on:
    
    screen.update()
    time.sleep(0.3)
    
    snake.move()
    
screen.exitonclick()