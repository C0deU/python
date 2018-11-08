n = int(input())
information = []
old = []
young = []
new_information = []
for i in range(n):
    s = input().split()
    information.append([s[0], i, s[1]])
for el in information:
    if int(el[2]) >= 60:
        old.append(el)
    else:
        young.append(el)
new_information = sorted(old, key=lambda x: (-int(x[2]), int(x[1])))
new_information += sorted(young, key=lambda x: int(x[1]))
for i in range(n):
    print(new_information[i][0])

