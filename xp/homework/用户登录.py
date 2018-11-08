f = open('_user_information.txt', 'r', encoding='utf-8')
_user = f.read()
_user = eval(_user)
f.close()
n = 0
lst = []
while n < 3:
    user = input('请输入账户：')
    passward = input('请输入密码：')
    if user in _user.keys():
        if _user[user][1] == 0:
            if _user[user][0] == passward:
                print('登陆成功！欢迎您！')
                break
            else:
                print('密码错误！请重新输入')
        else:
            print('账户锁定！')
            break
    else:
        print('账户不存在！请重新输入!')
    lst.append(user)
    n += 1
else:
    if lst[0] == lst[1] == lst[2]:
        _user[lst[0]][1] = 1
        print('三次输入错误，账户锁定！')
f1 = open('_user_information', 'w', encoding='utf-8')
f1.write(str(_user))
f1.flush()
f1.close()
