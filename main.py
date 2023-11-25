import turtle

# Установка экрана
screen = turtle.Screen()
screen.title("Мой смайлик")

# Создание объекта черепахи
pen = turtle.Turtle()
pen.speed(1)

# Рисуем лицо
pen.color("yellow")
pen.begin_fill()
pen.circle(100)
pen.end_fill()

# Рисуем глаза
pen.penup()
pen.goto(-40, 120)
pen.pendown()
pen.color("black")
pen.begin_fill()
pen.circle(20)
pen.end_fill()

pen.penup()
pen.goto(40, 120)
pen.pendown()
pen.begin_fill()
pen.circle(20)
pen.end_fill()

# Рисуем улыбку
pen.penup()
pen.goto(-40, 85)
pen.pendown()
pen.right(90)
pen.circle(40, 180)

# Завершение
pen.hideturtle()
screen.mainloop()
