#teams = ["Packers", "49ers", "Ravens", "Patriots"]
#print({key: value for value, key in enumerate(teams)})
# print(','.join(teams))
# data = {'user': 1, 'name': 'Max', 'three': 4}
# is_admin = data.get('user', False)
# print(is_admin)
#
# for x in range(1,101):
#     print("fizz"[x % 3*4::]+"buzz"[x % 5*4::]or x)
# from collections import Counter
# print(Counter("hello"))
# lst = []
# for i in range(1, 31):
#     lst.append('*'[i % 3::] or i)
# print(lst)

# print([(x, y) for x in range(10) if x % 2 if x > 3 for y in range(10) if y > 7 if y != 8])
# for x in range(10):
#     if x % 2:
#         print(x)

# lst = [1, 5, 6, 5, 7, 2, 9]
# for el in range(len(lst)):
#         lst.pop()
# print(lst)

# lst = ['周星驰', '周杰伦', '周润发', '马云', '周树人']
# dele = []
# for el in lst:
#     if "周" in el:
#         dele.append(el)
# for el in dele:
#     lst.remove(el)
# print(lst)
i = 0
a = [12, 2, 5, 23, 56, 1, 52, 24]
for j in range(len(a)-1, 0, -1):
    i = 0
    while i < j:
        if a[i] > a[i+1]:
            a[i], a[i+1] = a[i+1], a[i]
        i += 1
print(a)
