age = 26
while True:
    count = 0
    while count < 3:
        num = int(input("请输入年龄:"))
        if num == age:
            print("回答正确")
            break
        else:
            print("回答错误")
        count += 1
    choese =input("还要玩一次:y or n")
    if choese == "y":
        continue
    else:
        break

