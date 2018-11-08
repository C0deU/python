import turtle as t
size = int(input())
n = int(input())

t.setup(1600, 1000, -300, 0)
t.pensize(1)
t.speed(10)


def func(size, n):
    if n == 1:
        t.seth(60)
        t.fd(size)
        t.rt(120)
        t.fd(size)
        t.rt(120)
        t.fd(size)
    else:
        for jd in (120, 240, 0):
            func(size/2, n-1)
            t.penup()
            t.rt(jd)
            t.fd(size/2)
            t.pendown()


size = int(input())
n = int(input())
func(size, n)
t.done()

