s = input().split()
m = int(s[0])
n = int(s[1])
c = []
for i in range(m):
    a = input().split()
    c.append(a)
for i in range(n):
    d = []
    for j in range(m):
        d.append(c[j][i])
    print(' '.join(d))
