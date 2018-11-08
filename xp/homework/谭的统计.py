import re
a = {}
try:
    while True:
        s = input()
        lst = re.split(' |\r|\t|\n|,|\.|;|\'|\"|:|!|\?|\(|\)', s)
        for i in range(len(lst)):
            if lst[i] != "" and lst[i].isalpha():
                lst[i] = lst[i].lower()
                if lst[i] not in a:
                    a[lst[i]] = 1
                else:
                    a[lst[i]] += 1
except Exception as e:
    pass
k = max([len(x[0]) for x in a.items()])
c = sorted(a.items(), key=lambda x: (x[0], -x[1]))
for el in c:
    j = k//4+1 - len(el[0]) // 4
    print('%s%s%s' % (el[0], '\t' * j, el[1]))
print('----')
c = sorted(a.items(), key=lambda x: (-x[1], x[0]))
for el in c:
    j = k // 4 + 1 - len(el[0]) // 4
    print('%s%s%s' % (el[0], '\t'*j, el[1]))

