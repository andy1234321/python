# from random import randint
# from random import *
# import random as r
#
# x = r.randint(0, 100)
# lst = [0, 1, 2, 3, 4, 5]
# element_random = r.choice(lst)
# r.shuffle(lst)
#
# print(x)
# print(element_random)
# print(lst)

import turtle

t = turtle.Turtle()
t.shape("turtle")
t.penup()
t.goto(-300, 250)
t.pendown()
screen = turtle.Screen()
t.color("green", "purple")
t.pensize(10)
t.speed(8)
t.begin_fill()
t.forward(310)
t.right(90)
t.forward(210)
t.right(90)
t.forward(310)
t.right(90)
t.forward(210)
t.right(90)
t.end_fill()
t.penup()
t.goto(-200, 200)
t.pendown()
t.forward(50)
t.write("movavi", font=("Arial black", 50, "normal"))
screen.exitonclick()
