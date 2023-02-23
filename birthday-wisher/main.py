import smtplib
import datetime as dt
import random

email = "jeffsong831@gmail.com"
password = "oxtfnidfgwpldmat"
now = dt.datetime.now()
weekday = now.weekday()

if weekday == 1:
    with open("quotes.txt") as quotes:
        quote_list = quotes.readlines()
        quote = random.choice(quote_list)

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=email, password=password)
        connection.sendmail(
            from_addr=email,
            to_addrs="to_email",
            msg="Subject:Happy Tuesday!\n\n" + quote)


