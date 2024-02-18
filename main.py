from turtle import Turtle, Screen
import random
import os

os.system("cls")

screen = Screen()
screen.setup(width=500, height=400)

user_bet = screen.textinput(
    title="Make your bet", prompt="Which turtle will win the race? "
)

colors = ["blue", "red", "green", "yellow", "black"]
positions = [-100, -50, 0, 50, 100]

turtles = []

for color, position in zip(colors, positions):
    turtle = Turtle(shape="turtle")
    turtle.color(color)
    turtle.penup()
    turtle.goto(x=-240, y=position)
    turtles.append(turtle)

is_race_on = False

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in turtles:
        if turtle.xcor() > 230:
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You have won ! The {winning_color} is the winner ")
                is_race_on = False
            else:
                print(f"You have lost! and the winner is {winning_color}")
                is_race_on = False
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)


screen.exitonclick()
