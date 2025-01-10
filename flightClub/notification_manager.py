import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

sender_email = os.environ["SENDER_EMAIL"]
sender_password = os.environ["SENDER_PASSWORD"]


def send_flights_email(email, mail_content):
    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = email
    message['Subject'] = "We've got deals for you!"
    message.attach(MIMEText(mail_content, 'plain'))
    session = smtplib.SMTP('smtp.office365.com', 587)
    session.starttls()
    session.login(sender_email, sender_password)  # login with mail_id and password
    text = message.as_string()
    session.sendmail(sender_email, email, text)
    session.quit()
    print('Mail Sent')
