a = int(input("请输入工资:"))

products = [ ['Iphone8',6888],['MacPro',14800], ['小米6',2499],['Coffee',31],['Book',80],['Nike Shoes',799] ]

buy =[]
index = 0
exit_flag = False
print('---------商品列表----------')
for p in products:
    print("%s. %s    %s" % (index, p[0], p[1]))
    index += 1
while not exit_flag:

    print('您的余额为:', a)
    print(len(products))

    choice = input('请输入购买商品编号:')
    if choice.isdigit():
        choice = int(choice)
        if choice >= 0 & choice < 6:
            if a > int(products[int(choice)][1]):
                buy.append(products[int(choice)])
                a = a-int(products[int(choice)][1])
            else:
                print("-------------余额不足!-------------")
                continue
        else:
            print("商品不存在")

    elif choice == 'q':
        if len(buy) >0:
            print("-------你已购买以下商品---------")
            for index,p in enumerate(buy):
                print("%s. %s   %s" % (index, p[0], p[1]))
            print('您的余额为:', a)
        exit_flag = True

