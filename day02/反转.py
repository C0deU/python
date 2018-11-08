n = input()
if n[0] == "-":
    x = -int(n[1:][::-1])
else:
    x = int(n[::-1])
print(x)
