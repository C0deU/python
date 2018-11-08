# def func(a, b):
#     if a >= b:
#         if b % (a % b) == 0:
#             return print(int(a % b))
#         else:
#             return func(b, a % b)
#     else:
#         if a % (b % a) == 0:
#             return print(int(b % a))
#         else:
#             return func(a, b % a)
#


def func(a, b):
    if a >= b:
        if a % b == 0:
            return print(b)
        else:
            return func(b, a % b)
    else:
        if b % a == 0:
            return print(a)
        else:
            return func(a, b % a)


n = input().split()
x, y = int(n[0]), int(n[1])
func(x, y)
