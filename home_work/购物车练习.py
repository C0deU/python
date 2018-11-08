goods = [
{"name": "电脑", "price": 1999},
{"name": "鼠标", "price": 10},
{"name": "游艇", "price": 20},
{"name": "美女", "price": 998}
]
car = []
index = 0
enter_flag = True
exit_flag = False
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
                enter_flag = False
                break
            else:
                print('密码错误请重新输入')
                j += 1
    else:
        print('账号不存在')
if enter_flag == False:
    total_money = int(input('请输入工资:'))

    print('---------商品列表----------')
    for p in goods:
        print('%s.       %s         %s' % (index, p.get("name"), p.get("price")))
        index += 1
    print('您的余额为:', total_money)
    while not exit_flag:

        choice = input('请选择商品编号:')
        if choice.isdigit():
            choice = int(choice)
            if choice >= 0 & choice < len(goods):
                if total_money >= int(goods[choice].get("price")):
                    total_money -= int(goods[choice].get("price"))
                    car.append(goods[choice].get("name"))
                    print('\033[1;31;40m%s\033[0m' % "----------商品加入购物车----------")
                    print('------当前余额为:', '\033[1;35;40m%s\033[0m' % total_money, "------")
                else:
                    print("--------------当前余额不足---------------")
            else:
                print("商品超出范围")
        elif choice == "q" or choice == "Q":
            if len(car) > 0:
                print("-------你已购买以下商品---------")
                for index, p in enumerate(car):
                    print("%s. %s " % (index, p))
                print('-----您的余额为:', '\033[1;35;40m%s\033[0m' % total_money, '------')
            exit_flag = True
