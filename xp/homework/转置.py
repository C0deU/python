s = input().split()
lst = []
lst1 = []
for i in range(int(s[0])):
    lst.append(input().split())
for i in range(int(s[1])):
    lst2 = []
    for j in range(int(s[0])):
        lst2.append(lst[j][i])
    lst1.append(lst2)
for i in range(len(lst1)):
    print(' '.join(lst1[i]))
