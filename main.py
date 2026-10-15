# To run and test the code you need to update 4 places:
# 1. Change MY_EMAIL/MY_PASSWORD to your own details.
# 2. Go to your email provider and make it allow less secure apps.
# 3. Update the SMTP ADDRESS to match your email provider.
# 4. Update birthdays.csv to contain today's month and day.
# See the solution video in the 100 Days of Python Course for explainations.

# import os and use it to get the Github repository secrets
MY_EMAIL = os.environ.get("MY_EMAIL")
MY_PASSWORD = os.environ.get("MY_PASSWORD")

import datetime as dt
import pandas
import smtplib
import random
import os

##################### Extra Hard Starting Project ######################

MY_EMAIL = os.environ.get("my_email")
MY_PASSWORD = os.environ.get("password")

data = pandas.read_csv("birthdays.csv")
picking = data.to_dict(orient="records")

now = dt.datetime.now()
month = now.month
day = now.day
ran_number = random.randint(1, 3)
for item in picking:
    if item["month"] == month and item["day"] == day:
        with open(f"letter_templates/letter_{ran_number}.txt") as file:
            content = file.read()
            message = content.replace("[NAME]", item["name"])
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email,
                                to_addrs="inopepaul13@gmail.com",
                                msg=f"Subject:Birthday wisher\n\n{message}")
