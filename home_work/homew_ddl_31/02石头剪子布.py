n = input().split()
na = input().split()
nb = input().split()
sa = 1
sb = 1
A, B, C = 0, 0, 0
if int(n[1]) < int(n[0]) or int(n[2]) < int(n[0]):
    sa = int(n[0]) // int(n[1]) + 1
    sb = int(n[0]) // int(n[2]) + 1
vs = list(map(lambda x, y: x+y, na*sa, nb*sb))
lst = vs[:int(n[0])]
print(lst)
a = ['02', '25', '50']
b = ['20', '52', '05']
c = ['00', '22', '55']
for i in lst:
    A = a.count(i)
for i in lst:
    B = b.count(i)
for i in lst:
    C = c.count(i)
if A == B:
    print("draw")
elif A > B:
    print("A")
else:
    print("B")
