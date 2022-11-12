import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

turtle = Player()
scoreboard=Scoreboard()
screen.listen()
screen.onkey(turtle.move, "Up")

car_manager = CarManager()
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_cars()
    car_manager.move()
    for car in car_manager.all_cars:
        if car.distance(turtle) < 20:
            car_manager.increment = 0
            game_is_on = False
            scoreboard.game_over()


    if turtle.ycor() >= 280:
        turtle.reset_position()
        car_manager.increment += 1
        scoreboard.increase_level()


screen.exitonclick()



