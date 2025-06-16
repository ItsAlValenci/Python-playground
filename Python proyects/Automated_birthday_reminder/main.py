import smtplib
import datetime as dt
from dotenv import load_dotenv
import os
import random
import pandas as pd

letter_paths = [
    "letter_templates/letter_1.txt",
    "letter_templates/letter_2.txt",
    "letter_templates/letter_3.txt"
]

birthdays_path = "birthdays.csv"


def email_sender(message, destinatary ):

    load_dotenv()
    EMAIL_PASSWORD = os.getenv("EMAIL_KEY")

    MY_EMAIL = "my_email@gmail.com"

    try:
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=EMAIL_PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=destinatary,
                msg=f"Subject: Happy Birthday\n\n{message}"
            )
        print(f"Birthday email sent to: {destinatary}")
    except Exception as e:
        print(f"Failed to send email to {destinatary}: {e}")


# Getting real days
today = dt.datetime.now()
current_day = today.day
current_month = today.month

file = pd.read_csv(birthdays_path)
birthdays_df = pd.DataFrame(file)

matched = False

# Check each birthday
for index, row in birthdays_df.iterrows():
    if row["month"] == current_month and row["day"] == current_day:
        matched = True

        # Prepare the letter
        with open(random.choice(letter_paths), "r") as file:
            email_body = file.read()
            message_to_use = email_body.replace("[NAME]", row["name"])

        # Send the email
        email_sender(message_to_use, destinatary= row["email"])

        # Print confirmation to terminal
        print(f"Birthday email sent to: {row['name']} <{row['email']}>")

# If no birthdays matched
if not matched:
    print("No birthdays today.")

