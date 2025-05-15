import time
from turtle import Screen
from snake import Snake
from scorecard import Scorecard
from food import Food

screen = Screen()
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.tracer(0)
screen.bgcolor('black')
screen.title("My Snake Game!")

snake = Snake()
food = Food()
score = Scorecard()

screen.listen()
screen.onkey(snake.up, "w")
screen.onkey(snake.down, "s")
screen.onkey(snake.left, "a")
screen.onkey(snake.right, "d")
screen.onkey(snake.add_segment, "x")

game_is_on = True
while game_is_on:

    screen.update()
    time.sleep(0.1)

    if snake.head.distance(food) < 15:
        food.refresh()
        score.increment_score()
        snake.add_segment()

    if snake.is_snake_out_of_bounds() or snake.is_tail_touched():
        print("Out of bounds!")
        score.game_over()
        game_is_on = False

    snake.move()
# screen.onkey(key='c', fun=clear)


screen.exitonclick()