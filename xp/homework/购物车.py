import time
f = open('shopcar.txt', mode='r+', encoding='utf-8')
goods = [
    {"name": "电脑", "price": 1999},
    {"name": "鼠标", "price": 10},
    {"name": "游艇", "price": 20},
    {"name": "美女", "price": 998},
]
_user_information = eval(f.read())
car = []
user = input('请输入用户名：')
password = input('请输入密码：')
cost = 0
c = []
money = 0
if user in _user_information:
    if _user_information[user]['code'] == password:
        print('欢迎登陆 \033[0;31;46m%s\033[0m' % user)
        flag = 1
        cost = 0
        money = _user_information[user]['money']
        s = input('请输入本次存入工资：')
        while not s.isdigit():
            s = input('请输入正确的数字：')
        money += int(s)
    else:
        print("\033[1;31;40m密码不正确！\033[0m")
        flag = 0
else:
    print("\033[1;31;40m用户不存在！\033[0m")
    flag = 0

while flag:
    print('---------商品列表----------')
    for index, p in enumerate(goods):
        print("%s. %s    %s" % (index + 1, p['name'], p['price']))
    print('余额为：', '\033[1;32;0m%s\033[0m' % money)
    buy = input('请输入购买商品编号：')
    if buy.isdigit():
        if 0 < int(buy) < 5:
            thing = goods[int(buy) - 1]
            if money < thing['price']:
                print('\033[1;33;40m余额不足！\033[0m')
                print('余额为：', '\033[1;32;0m%s\033[0m' % money)
            else:
                car.append(thing['name'])
                money -= thing['price']
                cost += thing['price']
                print('\033[1;36;40m商品 \033[1;31;40m%s\033[1;36;40m 已加入购物车\033[0m' % thing['name'])
                print('余额为：', '\033[1;32;0m%s\033[0m' % money)
        else:
            print('\033[1;31;40m请输入正确商品编号！\033[0m')
    elif buy.lower() == "q":
        break
    elif buy == 'check':
        if _user_information[user]['buy']:
            for el in _user_information[user]['buy'].items():
                print('\033[1;31;40m购买时间:\033[1;32;0m%s\033[0m' % el[0])
                print('\033[1;31;40m购买商品:\033[1;32;0m%s\033[0m' % ','.join(el[1][0]))
                print('\033[1;31;40m购买费用:\033[1;32;0m%s\033[0m' % el[1][1])
                print()
        else:
            print('\033[1;31;40m无记录:\033[0m')
    else:
        print('\033[1;31;40m请输入正确商品编号！\033[0m')

if flag:
    print('\033[1;36;0m---------已购买商品列表----------\033[0m')
    for index, el in enumerate(car):
        print('\033[1;31;40m%s  %s\033[0m' % (index + 1, el))
    print('本次消费总额:\033[1;32;0m%s\033[0m' % cost)
    print('余额为：\033[1;32;0m%s\033[0m' % money)
    if car:
        _user_information[user]['money'] = money
        c.append(car)
        c.append(cost)
        _user_information[user]['buy']['%s' % time.asctime(time.localtime(time.time()))] = c
    f.seek(0, 0)
    f.write(str(_user_information))
    f.flush()
f.close()
