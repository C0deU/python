import turtle   #导入海龟包
import time     #导入时间包
turtle.speed(1)     #设置指针速度为9(范围1-10)(不重要)
x = 300             #设置三角形初始边长
turtle.left(120)    #因为画图指针初始为沿着x轴正向的,所以设置指针左转120°
for j in range(6):          #for循环.range(x,y-1)相当于一个从x到y的数组(只有一个数就是从零开始)
                            #相当于给j赋值,从x到y-1.循环y-x次
    for i in range(3):      #循环3次
        turtle.forward(x)   #指针向前移动X的距离
        turtle.left(120)    #指针左转向120°
    x = x/2                 #上面的循环画出了打的三角形,下个三角形的边长为上个三角形的一半.
    turtle.forward(x)       #沿着边移动到大三角形边的中点
    turtle.left(60)         #指针左转60°这步转向是为了调整小三角形初始画线的方向,
time.sleep(5)               #画完后延迟5秒关闭窗口(不重要)







# import turtle as t
# import time
# t.color("red", "yellow")
# t.speed(10)
# t.begin_fill()
# for _ in range(50):
#     t.forward(200)
#     t.left(170)
# turtle.end_fill()
# time.sleep(5)