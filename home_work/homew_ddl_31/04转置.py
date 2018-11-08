x = input().split()
lst = []
for i in range(int(x[0])):
    lst.append(input().split())
lst1 = [[lst[n][m] for n in range(int(x[0]))]for m in range(int(x[1]))]
for j in range(int(int(x[1]))):
    print()
    for i in range(int(int(x[0]))):
        print(lst[i][j], end=" ")
