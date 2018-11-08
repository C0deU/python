# from collections import OrderedDict
# c = [('b', 222), ('a', 222), ('c', 222), ('e', 111), ('f', 111),('d', 111)]
# c = OrderedDict(c)
# del c['b']
# c.pop(c['a'])
# del c['b']
# print(c)


# print(id(c['b']))
# print(id(c['a']))
# print(id(c['c']))
# print(id(c['e']))
# print(id(c['f']))
# print(id(c['d']))
# # print(c.keys())
# for i in c.keys():
#     print(id(i))
# b = sorted(c.items(), key=lambda x: x[1], reverse=True)
# print(b)

l = []
k = []
while True:
    s = input().split()
    l.append(s)
    if s == ['-1', '-1']:
        k.append(l)
        l = []
    if s[0] == '-1' and len(s) == 1:
        break
for i in range(len(k)):
    n = int(k[i][0][0])
    m = 0
    s = k[i][1::]
    b = []
    for i in range(len(s) - 1):
        c = n
        m = 0
        while True:
            if s[i][0] == "-1":
                break
            c -= int(s[i][1])
            if c >= 0:
                m += int(s[i][0])
                i += 1
                if s[i][0] == "-1":
                    break
            if c < 0:
                break
        b.append(m)
    print(max(b))
