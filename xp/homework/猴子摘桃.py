a = []
a1 = []
b1 = []
while True:
    s = input().split()
    if s == ['-1', '-1']:
        a1.append(a)
        a = []
    elif len(s) != 1 or s[0] != '-1':
        a.append(s)
    else:
        break
for j in a1:
    b = []
    for i in range(1, len(j)):
        c = int(j[0][0])
        m = 0
        for k in range(i, len(j)):
            c -= int(j[k][1])
            if c >= 0:
                m += int(j[k][0])
            if c < 0:
                break
        b.append(m)
    b1.append(max(b))
for i in b1:
    print(i)