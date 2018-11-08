a, b = input().split()
c = ""
count = 0
for i in range(int(a), int(b)+1):
    c = c + str(i)
print(c.count('2'))


# d.extend(c)
# for i in range(0, (len(d))):
#     if d[i] == "2":
#         count += 1
#print(count)
