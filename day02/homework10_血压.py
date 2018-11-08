# n = int(input())
# count = 0
# time = []
# for i in range(0, n):
#     a, b = input().split()
#     if 60 <= int(b) <= 90 <= int(a) <= 140:
#         count += 1
#     else:
#         time.append(count)
#         count = 0
# for i in range(0, len(time)-1):
#     if time[i] > time[i+1]:
#         time[i], time[i+1] = time[i+1], time[i]
# print(time[len(time)-1])
n = int(input())
i = 0
a = 0
for j in range(n):
    s = input().split()
    if 60 <= int(s[1]) <= 90 <= int(s[0]) <= 140:
        i += 1
    else:
        i = 0
    if a < i:
        a = i
print(a)
