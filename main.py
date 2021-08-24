import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
score_board = Scoreboard()


screen.listen()
screen.onkey(player.move_forward, "Up")
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    score_board.display_score()
    car_manager.create_car()
    car_manager.move_cars()

    # detect collision with cars
    for car in car_manager.cars_list:
        if car.distance(player) < 20:
            game_is_on = False
            score_board.game_over()

    # detect if the turtle has reached the end of the line
    if player.ycor() == 280:
        score_board.update_score()
        player.reset_player_position()
        car_manager.increase_car_speed()
screen.exitonclick()