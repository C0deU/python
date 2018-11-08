# import re
# b = {}
# try:
#     while 1:
#         s = input()
#         a = re.split(' |,|\.|;|\'|\"|:|!|\?|\(|\)', s)
#         for el in a:
#             if el.isalpha() and el:
#                 el = el.lower()
#                 if el in b:
#                     b[el] += 1
#                 else:
#                     b[el] = 1
# except Exception as e:
#     pass
# c = sorted(b.items(), key=lambda x: (-x[1], x[0]))
# for el in c:
#     print('%s\t%s' % (el[0], el[1]))
#     # # print(el[0], end='')
#     # # print('\t', end='')
#     # # print(el[1])
#     # print(el[0], '\t', el[1])
# print('----')
# c = sorted(b.items(), key=lambda x: (x[0], -x[1]))
# for el in c:
#     print('%s\t%s' % (el[0], el[1]))

import re
a = {}
b = []
try:
    while True:
        s = input()
        lst = re.split(":|,|\.|\?|!|;|\"|\'| |\r|\t|\n|\(|\)", s)
        for i in range(len(lst)):
            if lst[i] != "" and lst[i].isalpha():
                lst[i] = lst[i].lower()
                if lst[i] not in a:
                    a[lst[i]] = 1
                else:
                    a[lst[i]] += 1
except Exception as e:
    pass
for i in a.items():
    b.append([i[0], i[1]])
k = max([len(x[0]) for x in b])
d = sorted(b, key=lambda x: x[0])
for i in range(len(d)):
    x = k//4 + 1 - len(d[i][0])//4
    print("%s%s%s" % (d[i][0], '\t'*x, d[i][1]))
print("----")
c = sorted(b, key = lambda x: int(x[1]), reverse=True)
for i in range(len(c)):
    x = k//4 + 1 - len(c[i][0])//4
    print("%s%s%s" % (c[i][0], '\t'*x, c[i][1]))
