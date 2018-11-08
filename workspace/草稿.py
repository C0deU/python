import turtle as t
size = 120
for jd in (120, 240, 0):
    t.seth(60)   #使指针的朝向与x轴成60°
    t.fd(size)
    t.rt(120)
    t.fd(size)
    t.rt(120)
    t.fd(size)

    t.penup() #指针抬起
    t.rt(jd)  #右转角度
    t.fd(size)  #前进距离
    t.pendown()     #指针放下
