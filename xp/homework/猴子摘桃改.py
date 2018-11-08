a = []
a1 = []
b1 = []
while True:
    s = input().split()
    if len(s) != 1 or s[0] != '-1':     # 因为有蜂蜜数这一个数字的输入，所以需要加上'-1'的判断
        a.append(s)
    else:
        break
    if s == ['-1', '-1']:
        a1.append(a)    # 每次遇到['-1', '-1']就把a加入a1存起来
        a = []          # 然后重置a
for j in a1:    # 遍历a1，也就是遍历每个案例(j就是存储每个案例的列表)
    b = []      # 重置用来存储每个案例各个情况的列表
    for i in range(1, len(j)-1):    # 排除每个案例的第一个数据，因为那是猴子持有的蜂蜜数
        c = int(j[0][0])    # 因为每个案例第一个是只有一个数字的列表储存的是猴子的蜂蜜数
        m = 0
        while True:
            c -= int(j[i][1])
            if c >= 0:
                m += int(j[i][0])
                i += 1
                if j[i][0] == "-1":
                    break
            if c < 0:
                break
        b.append(m)
    b1.append(max(b))   # 将每次案例的最大情况加入b1
for i in b1:    # 输出
    print(i)