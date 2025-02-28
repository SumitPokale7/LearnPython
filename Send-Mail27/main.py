import smtplib 
from datetime import datetime
import random
import pandas


########################### CONSTANT VALUES ################################
TEST_EMAIL = "Masti@gmail.com"
PASSWORD = "qwertyuiop"
PLACE_HOLDER = "[NAME]"
RANDOM_NUMBER = random.randint(1, 3)


########################### TODAY & BIRTHDAY ################################
today = (datetime.now().month, datetime.now().day)
data = pandas.read_csv("letter_templates/birthdays.csv")
birthday_dict = {(data_row.month, data_row.day): data_row for (index, data_row) in data.iterrows()}


############################## SEND MAIL ####################################
if today in birthday_dict:
    file_path = f"letter_templates/letter_{RANDOM_NUMBER}.txt"

    birthday_person = birthday_dict[today]

    with open(file_path) as letter_file:
        content = letter_file.read()
        content = content.replace(PLACE_HOLDER, birthday_person["name"])

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=TEST_EMAIL, password=PASSWORD)

        connection.sendmail(
                from_addr=TEST_EMAIL, 
                to_addrs=birthday_person.email,
                msg=f"Subject:Happy Birthday!\n\n{content}"
        )
