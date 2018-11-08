n = int(input())
a = 0
for i in range(0, n):
    a += int(input())
print('%d %.5f' % (a, a/n))


# n = input()
# a = 0
# i = 0
# if n.isdigit():
#     n = int(n)
#     if 1 <= n <= 10000:
#         while i < n:
#             s = int(input())
#             if -10000 <= s <= 10000:
#                 a += s
#                 i += 1
#         print(a, '%.5f' % (a/n))
