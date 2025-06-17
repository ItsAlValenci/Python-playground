import smtplib
import datetime as dt
from dotenv import load_dotenv
import os
import random

file_path = "quotes.txt"


def email_sender(message="test" ):
    load_dotenv()
    EMAIL_PASSWORD = os.getenv("EMAIL_KEY")

    MY_EMAIL = "my_email@gmail.com"

    destinatary = "your_email@gmail.com"

    with smtplib.SMTP("smtp.gmail.com",port=587) as connection:
        connection.starttls() #to make connection secure

        connection.login(user= MY_EMAIL, password=EMAIL_PASSWORD)
        connection.sendmail(
            from_addr= MY_EMAIL,
            to_addrs=destinatary, 
            msg= f"Subject: Monday motivation for a great week\n\n{message}"
        )

today = dt.datetime.now()
current_day = today.weekday()

if current_day == 0:
    with open(file_path, mode= "r") as file:
        quotes_list = file.readlines()
        quote_to_use = random.choice(quotes_list)

email_sender(quote_to_use)