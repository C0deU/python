c = []
flag = 1
s = input().split()
if len(s) == 25:
    s = [int(el) for el in s]
    for i in range(5):
        c.append(s[i*5:(i*5)+5])
else:
    x = [int(el) for el in s]
    c.append(x)
    for i in range(4):
        a = input().split()
        a = [int(el) for el in a]
        c.append(a)
for i in range(5):
    m = max(c[i])
    d = c[i].index(m)
    b = []
    for i in range(5):
        b.append(c[i][d])
    n = min(b)
    e = b.index(n)
    if n == m:
        print(d+1, e+1, m)
        flag = 0
if flag == 1:
    print('not found')
