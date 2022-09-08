import random
import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.tracer(0)
screen.listen()
loop_count = 0

# Create player
player = Player()

# Create Car Manager (all cars are here)
cars = CarManager()

# Create scoreboard and text related info
scoreboard = Scoreboard()

# If up key is pressed on keyboard, then player moves up
screen.onkey(player.move, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    loop_count += 1

    # Set car creation functionality
    if loop_count % 6 == 0:
        cars.create_car()

    # Set car movement functionality
    cars.move()

    # Detect if turtle hits a car
    for car in cars.all_cars:
        if car.distance(player) < 20:
            scoreboard.game_over()
            game_is_on = False

    # Detect if turtle reached the other side successfully
    # Also increase level and car speed
    if player.ycor() > 280:
        player.next_level()
        scoreboard.increase_level()
        cars.increase_speed()

screen.exitonclick()
