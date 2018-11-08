import datetime
starttime = datetime.datetime.now()
#long running
s = input().split()
lst = []
d = []
for i in range(int(s[1])):
    d.append(input().split())
for i in range(int(s[1])):
    for j in range(int(d[i][1]), int(d[i][1]) + 1):
        if j not in lst:
            lst.append(j)
print(int(s[0]) + 1 - len(lst))
endtime = datetime.datetime.now()
print((endtime - starttime).seconds)