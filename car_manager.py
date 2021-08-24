from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 2


class CarManager:
    def __init__(self):
        self.cars_list = []
        self.create_car()
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        random_sequence = random.randint(1, 6)
        if random_sequence == 1:
            new_car = Turtle("square")
            new_car.penup()
            new_car.color(random.choice(COLORS))
            new_car.shapesize(stretch_len=2, stretch_wid=1)
            new_y = random.randint(-250, 250)
            new_car.goto(300, new_y)
            self.cars_list.append(new_car)

    def move_cars(self):
        for car in self.cars_list:
            car.back(self.car_speed)

    def increase_car_speed(self):
        self.car_speed += MOVE_INCREMENT