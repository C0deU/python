# __author__ = "wyb"
# date: 2018/4/18


# 用户信息
user_info = {
    'wyb': '666',
}

# 打开文件读取第一行数据， 即为用户工资
f = open("money.txt", "r", encoding="utf-8")
salary = int(f.readline())
f.close()

# 商品列表
goods = [
    {"name": "电脑", "price": 1999},
    {"name": "鼠标", "price": 10},
    {"name": "游艇", "price": 20},
    {"name": "美女", "price": 998},
]

# 购物车列表 -> [{"name": "电脑", "price": 1999, "number": 1}...]
# 升级需求 -> 存入文件中
shopping_cart = []


# 高亮输出字符串
def output_highlight(s):
    print('\033[1;31;40m%s\033[0m' % s)


# 打印商品列表
def output_info():
    print("商品列表".center(36, '*'))
    print("\t\t%s\t%s" % ("name", "price"))
    for index, item in enumerate(goods):
        print("\t%d.  %s\t\t%d " % (index+1, item['name'], item['price']))
    print("end".center(36, '*'))


# 退出之前将购物车的数据以添加的方式写入文件中
def before_exit():
    file = open("shopping_cart.txt", "a+", encoding="utf-8")
    for item in shopping_cart:
        file.write(str(item)+"\n")
    file.close()


# 打印购物记录
def output_shopping_records():
    file = open("shopping_cart.txt", "r", encoding="utf-8")
    s = file.readlines()
    print("购物记录如下: ")
    if not s:
        print("无购物记录")
    else:
        print("商品 单价 数量")
        for item in s:
            item = eval(item.strip())
            # print(type(item))
            print(item['name'], str(item['price'])+"元", item['number'])
    output_highlight("你还有%d元钱" % salary)
    file.close()


# 退出时打印已购买商品和余额
def output_shopping_salary():
    # 打印余额
    output_highlight('\t\t你还剩下: %d元\033[0m' % salary)
    # 将余额存入文件中
    f1 = open("money.txt", "w", encoding="utf-8")
    f1.write(str(salary))
    f1.close()
    # 打印已购买商品
    print("shopping_cart".center(36, '-'))
    print("\t\t%s\t%s\t%s" % ("name", "price", "number"))
    for index, item in enumerate(shopping_cart):
        print("%5d.%4s%8d%8d " % (index + 1, item['name'], item['price'], item['number']))
    print("end".center(36, '-'))


# 选择函数，专门负责输入处理
def input_choice(string):
    choices = input(string).strip()
    if choices == 'q':
        # 退出之前
        before_exit()
        # 退出时，打印已购买商品和余额
        output_shopping_salary()
        exit()

    return choices


# 登录验证程序:
def login():
    count = 0
    while True:
        count += 1
        username = input_choice("username: ")
        password = input_choice("password: ")
        # 当输入3次并且第3次也错误的情况下用户不能再登录
        if count >= 3 and user_info.get(username, None) != password:
            print("你已经错了太多次了!不能再试了!")
            exit()
        if user_info.get(username, None) == password:
            print("登录成功!")
            return 0
        else:
            print("用户名或密码错误!")
            continue


# 主函数:

# 登录:
print("购物车系统:  在任意地方输入q将退出系统")
c = input("输入c查询之前的购物记录, 输入q退出系统，输入其他继续访问: ")
if c == 'c':
    output_shopping_records()
    exit()
elif c == 'q':
    exit()
else:
    login()

# 输入工资
if salary == 0:
    salary = input_choice("输入你的工资: ")
    salary = int(salary)

# 打印商品列表及工资
output_info()
output_highlight("你还有%d元钱" % salary)

# 购买商品
while True:
    # 输入商品序号
    good_choice = int(input_choice("请输入想购买的商品的序号: "))
    # 获取商品字典和商品价格
    good_dict = goods[good_choice - 1]
    price = good_dict['price']

    # 没钱了:
    if salary == 0:
        # 高亮输出花完了钱
        output_highlight("你的工资已经花完了!")
        break

    # 可以买的情况:
    elif price <= salary:
        # 获取商品名字
        name = good_dict['name']
        # 遍历购物车，如果购物车中已有该商品把商品数直接加一，否则就加入商品
        for index, shopping_good in enumerate(shopping_cart):
            # 找到商品，商品数加一
            if shopping_good['name'] == name:
                shopping_good['number'] += 1
                break
        else:
            # 加入商品
            good_dict['number'] = 1
            shopping_cart.append(good_dict)
        # 在薪水中减去花的钱
        salary -= price
        # 高亮显示余额及加入购物车
        output_highlight("%s已加入购物车" % name)
        output_highlight("你还有%d元钱" % salary)
        continue
    # 不可以买的情况:
    else:
        # 高亮输出余额不足
        output_highlight("余额不足，请换一件商品或退出系统!")
        continue

# 退出之前
before_exit()

# 退出时，打印已购买商品和余额
output_shopping_salary()