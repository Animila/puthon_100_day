import smtplib

# почта для отправки
my_email = "19itypas70@gmail.com"
password = "Tomas_Kirit_Robert"

# Создание объекта SMTP (местоположение провайдеров эл. Почты)
with smtplib.SMTP("smtp.gmail.com") as connection:
    # включаем безопасность по TLS
    connection.starttls()
    # логин и пароль от вашей почты
    connection.login(user=my_email, password=password)
    # отправка письма (от кого, кому)
    connection.sendmail(from_addr=my_email, to_addrs="hristoforovila5@gmail.com",
                        msg="Subject:Hello\n\n This is body mail")