n = 1
while 1:
    i = []
    j = []
    a, b = 0, 0
    x = n
    while 1:
        if x // 7 > 0:
            i.append(str(x % 7))
            x = x // 7
            a += 1
        else:
            i.append(str(x))
            a += 1
            break
    x = n
    while 1:
        if x // 9 > 0:
            j.append(str(x % 9))
            x = x // 9
            b += 1
        else:
            j.append(str(x))
            b += 1
            break
    if i[::] == j[::-1] and a == 3 and b == 3:
        break
    n += 1
print(n)
print(int(''.join(i[::-1])))
print(int(''.join(j[::-1])))
