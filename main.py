# classic game of Snake
# Author: Rackley, Date: 2024-06-15
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

# Set up the screen for the game with specified dimensions and background color
screen = Screen()
screen.setup(width=600, height=600, startx=650, starty=300)
screen.bgcolor("black")
screen.title("Snake")
screen.tracer(0)  # Turn off automatic screen updates

snake = Snake()
food = Food()
score = Scoreboard()

# Set up key bindings for controlling the snake
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


segments = snake.segments 

# Initialize the game loop control variable
game_is_on = True

# Main game loop to keep the game running and update the screen
while game_is_on:
    
    screen.update()
    time.sleep(0.3)
    snake.move()
    
    # Check for collision with food
    if snake.head.distance(food) < 15:
        score.increase_score()
        food.refresh()
        # snake.add_segment(snake.segments[-1].position())    
        
screen.exitonclick()