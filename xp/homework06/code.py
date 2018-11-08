s = input()
s1 = ''
for el in s:
    if el.isalpha():
        if el == 'z' or el == 'Z':
            el = chr(ord(el)-25)
        else:
            el = chr(ord(el)+1)
    s1 += el
print(s1)

#字符串编码