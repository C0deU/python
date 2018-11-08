x = int(input())
a = []
b = []
n = x
while 1:
    s = n // 7
    i = n % 7
    if i == 0:
        break
    a.append(str(i))
    n = s
n = x
while 1:
    s = n // 9
    i = n % 9
    if i == 0:
        break
    b.append(str(i))
    n = s
c = ''
a.reverse()
x = c.join(a)
print(x)

#
# x = int(input())
# a = []
# b = []
# t = [7, 9]
# for el in t:
#     n = x
#     while 1:
#         s = n // el
#         i = n % el
#         if i == 0:
#             break
#         a.append(str(i))
#         n = s
#     a.append("-")
# c = ''
# a.reverse()
# a.
# x = c.join(a)
# print(x)
