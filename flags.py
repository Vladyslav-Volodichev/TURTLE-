import turtle
import time
import math

t = turtle.Turtle()
screen = turtle.Screen()
screen.bgcolor('black')
t.speed("fastest")


def square(color):
    t.up()
    t.goto(0, -140)
    t.down()
    t.color(color)
    t.begin_fill()
    t.left(180)
    t.forward(300)
    t.right(90)
    t.forward(275)
    t.right(90)
    t.forward(600)
    t.right(90)
    t.forward(275)
    t.right(90)
    t.forward(300)
    t.end_fill()
    t.hideturtle()
    t.home()


square('blue')


def stars(color, size_factor):
    t.color(color)
    t.up()

    # Рассчитываем координаты для распределения по кругу
    x = 90 * math.cos(math.radians(angle))
    y = 90 * math.sin(math.radians(angle))
    t.goto(x, y)

    t.down()
    t.begin_fill()

    for _ in range(5):
        t.forward(40 * size_factor)
        t.right(144)
        t.forward(40 * size_factor)
        t.left(72)

    t.end_fill()
    t.up()
    t.home()


# Распределяем 12 звезд по кругу
for i in range(12):
    angle = i * (360 / 12)  # Равномерно распределяем углы для 12 звезд
    stars('yellow', 0.25)

time.sleep(100)
