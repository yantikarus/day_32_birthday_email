import datetime as dt
import random
import smtplib
import pandas

my_email = "
passw = ""

##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv
now = dt.datetime.now()
month = now.month
date = now.day
data = pandas.read_csv("birthdays.csv")
bday_list = data.values.tolist()

for i in bday_list:
    if i[3] == month and i[4] == date:
        name = i[0]
        email = i[1]

        with open(f"./letter_templates/letter_{random.randint(1,3)}.txt") as letter:
            content = letter.readlines()
            new_content = "\n".join(content).replace("[NAME]", name)
            print(new_content)

        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=passw)
            connection.sendmail(from_addr=my_email,
                                to_addrs=email,
                                msg=f"Subject: Happy Birthday\n\n{new_content}")
# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.




