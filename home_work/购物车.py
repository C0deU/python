c = {'woshiyuangong':'woshimima'}
j = 0
flag = True
while flag == True:
    if j == 3:
        flag = False
        break
    a = input('请输入账号:')
    if a in c:
        while j < 3:
            b = input('请输入密码:')
            if c.get(a) == b:
                print("登陆成功")
                flag = False
                break
            else:
                print('密码错误请重新输入')
                j += 1
    else:
        print('账号不存在')
