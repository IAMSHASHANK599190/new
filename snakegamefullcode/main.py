import turtle
from score import Score
from food import *
from gameover import *
from operation import *
from turtle import Turtle, Screen
import random
import time

screen = Screen()
screen.setup(width=700, height=700)

screen.bgcolor("black")
screen.tracer(0)
snake = Snake()
food = Food()
score = Score()
gamedone = Gameover()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
code = True
while code:
    screen.update()
    time.sleep(0.1)
    snake.move()
    # DETECT COLLISION WITH FOOD
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.scoretrack()
    # DETECT THE COLLISION WITH THE WALL
    if snake.head.xcor() > 350 or snake.head.xcor() < -350 or snake.head.ycor() > 350 or snake.head.ycor() < -350:
        code = False
        gamedone.gameoverupdate()
    for segment in snake.segments[1:]:
         if snake.head.distance(segment)<10:
            code=False
            gamedone.gameoverupdate()


#
#
# direction = [90, 180, 270, 360]
# code = True
# while code:
#     line.color(random_oolor())
#     line.forward(50)
#     line.setheading(random.choice(direction))


screen.exitonclick()
