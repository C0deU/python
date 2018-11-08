s = int(input())
while True:
    if s == 1:
        break
    if s % 2:
        a = s
        s = s * 3 + 1
        print('%d*3+1=%d' % (a, s))
    else:
        a = s
        s = s / 2
        print('%d/2=%d' % (a, int(s)))
print('END')

