monthDays = [-1, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
days = 0
n = int(input())
lst = []
q = 0
p = 0
for i in range(n):
    lst.append(input().split())     # lst里存储日期的格式是[[XXXX,XX,XX],[XXXX,XX,XX],[XXXX,XX,XX]]
for i in range(n):
    year, month, date = int(lst[i][0]), int(lst[i][1]), int(lst[i][2])
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        monthDays[2] = 29
    if month < 1 or month > 12:
        print("illegal")
        continue
    if date < 1 or date > int(monthDays[month]):
        print("illegal")
        continue
    if year >= 2018:
        q = 1
        p = 1
        for y in range(2018, year, q):
            if y % 4 == 0 and y % 100 != 0 or y % 400 == 0:
                days += 366
            else:
                days += 365
        for j in range(p, month, q):
            days += monthDays[j]
        days += date
        days -= 1
        print(week[days % 7])
    elif year < 2018:
        q = -1
        p = 12
        for y in range(2018, year, q):
            if y % 4 == 0 and y % 100 != 0 or y % 400 == 0:
                days += 366
            else:
                days += 365
        for j in range(p, month, q):
            days += monthDays[j]
        days += (monthDays[month] - date + 1)
        print(week[(8 - days % 7) % 7])
