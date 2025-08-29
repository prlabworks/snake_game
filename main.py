# classic game of Snake

from turtle import Turtle, Screen
from snake import Snake
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake")
screen.tracer(0)  # Turn off automatic screen updates

# starting_positions = [(0, 0), (-20, 0), (-40, 0)]
# segments = []
# for position in starting_positions:
#     new_segment = Turtle("square")
#     new_segment.color("white")
#     new_segment.penup()
#     new_segment.goto(position)
#     segments.append(new_segment)

my_snake = Snake()
segments = my_snake.segments 


game_is_on = True

while game_is_on:
    
    screen.update()
    time.sleep(0.1)
    
    my_snake.move()
    
screen.exitonclick()