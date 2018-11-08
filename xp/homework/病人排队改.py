n = int(input())
old = []
young = []
for i in range(n):
    _user = input().split()
    if int(_user[1]) >= 60:
        old.append([_user[0], _user[1]])
    else:
        young.append([_user[0], _user[1]])
old = sorted(old, key=lambda x: x[1], reverse=True)
for el in (old+young):
    print(el[0])
