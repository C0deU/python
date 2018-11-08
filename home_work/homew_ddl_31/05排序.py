n = int(input())
l = []
for i in range(n):
    l.append(input().split())
c = sorted(l, key=lambda x: x[0])
b = sorted(c, key=lambda x: int(x[1]), reverse=True)
for i in b:
    print(i[0], i[1])
