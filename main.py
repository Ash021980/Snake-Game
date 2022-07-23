from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

# Set up game screen
screen = Screen()
screen.setup(height=600, width=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

# Create the initial snake object
snake = Snake()

# Initialize the food object
food = Food()

# Initialize the scoreboard
scoreboard = Scoreboard()

# Set the movement buttons to control the snake
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

# Start the game
game_on = True

while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect collision with the food and refresh the food's location and extends the size of the snake.
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    # Detect collision with the wall.
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        scoreboard.reset_scoreboard()
        snake.reset()

    # Detect collision with the snakes body
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.reset_scoreboard()
            snake.reset()

screen.exitonclick()
