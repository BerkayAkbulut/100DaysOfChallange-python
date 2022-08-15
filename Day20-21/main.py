from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import ScoreBoard

screen=Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake=Snake()
food = Food()
score = ScoreBoard(screen)

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")


game_is_on=True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    if snake.head_of_snake.distance(food) <15:
        food.reflesh_coor()
        snake.extend()
        score.reflesh_score()

    if snake.head_of_snake.xcor() > 265 or snake.head_of_snake.xcor()<-280 or snake.head_of_snake.ycor() >280 or snake.head_of_snake.ycor() < -265:
        game_is_on=False
        score.game_over()

    for cell in snake.snake[1:]:
        if snake.head_of_snake.distance(cell)<10:
            game_is_on=False
            score.game_over()

    snake.move()

screen.exitonclick()




