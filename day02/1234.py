# n = int(input())
# a = input().split()
# x = int(a[1])/int(a[0])
# data = []
# for i in range(n-1):
#     b = input().split()
#     y = int(b[1]) / int(b[0])
#     if y - x > 0.05:
#         data.append("better")
#     elif x - y > 0.05:
#         data.append("worse")
#     else:
#         data.append("same")
# for el in dat
# # for i in range(n):
# #     b = input(a:
#     print(el)
# # n = int(input())
# # data = []).split()
# #     data.append(int(b[1]) / int(b[0]))
# # for i in range(1, n):
# #     if data[i] - data[0] > 0.05:
# #         print("better")
# #     elif data[0] - data[i] > 0.05:
# #         print("worse")
# #     else:
# #         print("same")
# #
# data.reverse()
# a = 0
# b = 2
#
#
# def func1():
#     a = 1
#     print(a)
#
#     def func2():
#         b = 3
#         print(b)
#
#
#     print(666)
#     func2()
#     print(111)
# func1()
# print(b)
# print(a)


def outer(x):
    def inner(y):
        return x + y
    return inner


print(outer(2))
