lst = []
lst_change = []
data = input().split()
for i in range(int(data[0])):
    lst.append([int(x) for x in input().split()])
for i in range(int(data[0])):
    c = []
    for j in range(int(data[1])):
        if j == 0 or j == (int(data[1]) - 1) or i == 0 or i == (int(data[0]) - 1):
            c.append(str(lst[i][j]))
        else:
            c.append(str(round((lst[i - 1][j] + lst[i][j - 1] + lst[i][j + 1] + lst[i + 1][j] + lst[i][j]) / 5)))
    lst_change.append(c)
for el in lst_change:
    print(' '.join(el))
