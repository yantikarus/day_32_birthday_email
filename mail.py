import random
import smtplib
import datetime as dt
import random

my_email = ""
passw = " "



now = dt.datetime.now()
year = now.year
month = now.month
date = now.day
day_of_the_week = now.weekday()
print(day_of_the_week)


with open("quotes.txt") as file:
    content = [line.rstrip("\n") for line in file]
    print(len(content))
    today_quote = random.choice(content)
    print(today_quote)

# if day_of_the_week == 4:
#     with smtplib.SMTP("smtp.gmail.com", 587) as connection:
#         connection.starttls()
#         connection.login(user=my_email, password=passw)
#         connection.sendmail(from_addr=my_email,
#                             to_addrs="",
#                             msg=f"Subject: Friday Motivation\n\n{today_quote}")

# # dob = dt.datetime(year=1995, month=12, day=15)
# current_day_of_week = now.weekday()
# print(current_day_of_week)

