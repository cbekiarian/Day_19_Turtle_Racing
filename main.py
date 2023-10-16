from turtle import  Turtle,Screen
from random import randint
colors= [ "red", "orange", "yellow", "green", "blue", "purple"]


turtles = []
screen = Screen()
screen.setup(500,400)
is_race_on = False


def deo():
    pass


for i in range(0,6):
    turtles.append(Turtle("turtle"))
    turtles[i].penup()
    turtles[i].color(colors[i])
    turtles[i].goto((-200,-120 +i*50))

bet = screen.textinput("Make your bet", "Which turtle will win the race? Enter a color; ")
if bet:
    is_race_on = True
while is_race_on:
    for tur in turtles:
        tur.forward(randint(0,11))
        yo = tur.pos()
        if yo[0] > 230:
            is_race_on = False
            if tur.pencolor() == bet:
                print(f"You've won the {tur.pencolor()} is the winner")
            else:
                print(f"You've lost the {tur.pencolor()} is the winner")
            





screen.exitonclick()