from datetime import date

k = int(input())
total_days = 0

for i in range(k):
    # year a until year b
    a, b = map(int, input().split())

    for year in range(a, b+1):
        for month in range(1, 13):
            d = date(day=13, month=month, year=year)
            if d.weekday() == 4:
                total_days+=1

print(total_days)