from turtle import Screen
from scoreboard import Scoreboard
from snake import Snake
from food import Food
import time


screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.bgcolor("black")
screen.title("Snake Game")

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    # detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -300 or snake.head.ycor() > 300 or snake.head.ycor() < -280:
        scoreboard.reset()
        snake.reset()

    # detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()


screen.exitonclick()
