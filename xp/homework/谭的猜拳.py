s = input().split()
a = input().split()
b = input().split()
A, B, C = 0, 0, 0
if len(a) < int(s[0]):
    a = a * (int(s[0])//len(a) + 1)
if len(b) < int(s[0]):
    b = b * (int(s[0])//len(b) + 1)
for i in range(int(s[0])):
    el = int(a[i]) - int(b[i])
    if el in [-2, -3, 5]:
        A += 1
    elif el in [2, 3, -5]:
        B += 1
    else:
        C += 1
if A == B:
    print('draw')
elif A > B:
    print('A')
else:
    print('B')