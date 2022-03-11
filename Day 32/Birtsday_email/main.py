import random
import smtplib
import pandas
import datetime as td

PLACEHOLDER = "[NAME]"
my_email = "19itypas70@gmail.com"
password = "Tomas_Kirit_Robert"

date = td.datetime.now()
month = date.month
day = date.day

data = pandas.read_csv("birthdays.csv")
data_birthday = data.to_dict(orient="records")
for num in data_birthday:
    birthday_month = num["month"]
    birthday_day = num["day"]
    birthday_name = num["name"]
    birthday_email = num["email"]

    if month == birthday_month and day == birthday_day:
        letters = ["letter_1", "letter_2", "letter_3"]
        title = random.choice(letters)
        print(title)
        with open(f"letter_templates/{title}.txt") as file:
            letter = file.read()
            result_letter = letter.replace(PLACEHOLDER, birthday_name)

        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(my_email, password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs=birthday_email,
                msg=f"Subject:Happy Birthday\n\n{result_letter}")


# -- Как надо было--
# import random
# import smtplib
# import pandas
# from datetime import datetime
#
# PLACEHOLDER = "[NAME]"
# my_email = "19itypas70@gmail.com"
# password = "Tomas_Kirit_Robert"
#
# today = datetime.now()
# today_day = (today.month, today.day)
#
# data = pandas.read_csv("birthdays.csv")
# birthday_list = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}
# if today_day in birthday_list:
#     birthday_person = birthday_list[today_day]
#     file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
#     with open(file_path) as letter:
#         content = letter.read()
#         content = content.replace("[NAME]", birthday_person["name"])
#
#     with smtplib.SMTP("smtp.gmail.com") as connection:
#         connection.starttls()
#         connection.login(my_email, password)
#         connection.sendmail(
#             from_addr=my_email,
#             to_addrs=birtsday_person["email"],
#             msg=f"Subject:Happy Birthday\n\n{content}")
