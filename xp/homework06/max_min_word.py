import re
s = re.split(' |,|', input())
max_word = s[0]
min_word = s[0]
for el in s:
    if el.isalpha():
        if len(el) > len(max_word):
            max_word = el
        if len(el) < len(min_word):
            min_word = el
print(max_word)
print(min_word)

#冒泡排序
