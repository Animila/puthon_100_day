import datetime as dt
import smtplib
import random

# почта для отправки
my_email = "19itypas70@gmail.com"
password = "Tomas_Kirit_Robert"


now = dt.datetime.now()
day_of_week = now.weekday()
print(day_of_week)

if day_of_week == 4:
    with open("G:/Data_Program/python_projects/puthon_100/Day 32/lesson_3/quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quote = all_quotes[0]

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(my_email, password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="hristoforovila5@gmail.com",
            msg=f"Subject:Monday Motivation\n\n{quote}")
