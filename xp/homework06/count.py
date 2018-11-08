s = input()
word = ''
for el in s:
    if s.count(el) == 1:
        word = el
        break
if word:
    print(word)
else:
    print('no')

# count()函数的应用
