import datetime as dt

now = dt.datetime.now()
year = now.year
moth = now.month
day_of_week = now.weekday()
if year == 2022:
    print("Это маска")
print(now)
print(year)
print(moth)
print(day_of_week)

day_birtsday = dt.datetime(year=2002, month=12, day=27)
print(day_birtsday)