lst = []
for i in range(5):
    lst.append(list(map(int, input().split())))
for i in range(5):
    p = 0
    n = 0
    for j in range(4):
        if int(lst[i][p]) > int(lst[i][j+1]):
            p = p
        else:
            p = j+1
    for k in range(5):
        if int(lst[k][p]) > int(lst[i][p]):
            n += 1
    if n == 4:
        print(i+1, p+1, lst[i][p])



