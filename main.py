import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()
screen.title('Turtle Crossing Game')
player = Player()
score_board = Scoreboard()
car_manager = CarManager()

screen.onkeypress(player.move_up, 'Up')
screen.onkeypress(player.move_down, 'Down')

game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move_cars()
    for car in car_manager.all_cars:
        if player.distance(car) < 20:
            score_board.game_over()
            game_is_on = False
    if player.ycor() > player.get_finish_line():
        score_board.next_level()
        car_manager.increase_speed()
        player.goto(player.get_starting_position())

screen.exitonclick()