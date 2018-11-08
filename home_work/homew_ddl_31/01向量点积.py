n = int(input())
c = 0
for i in map(lambda x, y: int(x)+int(y), input().split(), input().split()):
    c += i
print(c)


n = int(input())
a = input().split()
b = input().split()
c = 0
for i in map(lambda x, y: int(x)+int(y), a, b):
    c += i
print(c)