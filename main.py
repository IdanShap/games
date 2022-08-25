from time import sleep
from turtle import Screen
from snake import Snake
from food import Food
from score_board import ScoreBoard

# program window parameters
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)
screen.colormode(255)

# creating the objects
score_board = ScoreBoard()
snake = Snake()
food = Food()

# start to listen to keyboard presses
screen.listen()
screen.onkey(key="Left", fun=snake.left)
screen.onkey(key="Right", fun=snake.right)
screen.onkey(key="Up", fun=snake.up)
screen.onkey(key="Down", fun=snake.down)

# game loop
game_is_on = True
while game_is_on:
    screen.update()
    sleep(0.12)
    snake.move()

    # detect collision with food
    if snake.head.distance(food) < 15:
        score_board.increase_score()
        food.new_location()
        snake.extend(snake.tail_position())

    # detect collision with walls
    if snake.head.xcor() > 295 or snake.head.xcor() < -295 or snake.head.ycor() > 295 or snake.head.ycor() < -295:
        score_board.game_over()
        break

    # detect collision with tail
    if snake.collided():
        score_board.game_over()
        break










screen.exitonclick()