import turtle as t
G = -300.01  # ускорение свободного падения
dt = 0.01  # точность просчёта траектории (чем меньше - тем лучше)
vx = 100  # начальная скорость по горизонтали
vy = 250  # начальная скорость по вертикали
y_earth = -300  # координата пола
y0 = y_earth  # начальная высота
x0 = -200  # начальная координата x


def setup_canvas():
    t.speed(0)
    t.width(5)
    t.penup()
    t.goto(-1000, y_earth)
    t.pendown()
    t.goto(1000, y_earth)
    t.penup()
    t.goto(300, y_earth)
    t.pendown()
    t.goto(300, 1000)
    t.penup()
    t.goto(-300, y_earth)
    t.pendown()
    t.goto(-300, 1000)
    t.penup()
    t.goto(x0, y0)
    t.pendown()
    t.width(1)


setup_canvas()
x = x0
y = y0
for i in range(1, 1000001):
    if y < y_earth:
        vy *= -1
    if x > 300:
        vx *= -1
    if x < -300:
        vx *= -1
    x += vx * dt
    y += vy * dt
    vy += G * dt
    t.goto(x, y)
