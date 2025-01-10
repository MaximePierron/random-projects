import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def is_price_under_threshold(threshold, product):
    product_url = product["url"]
    product_title = product["title"]
    product_price = product["price"]
    currency = product["currency"]

    if product["price"] < threshold:
        sender_email = os.environ["SENDER_EMAIL"]
        receiver_email = os.environ["RECEIVER_EMAIL"]
        sender_password = os.environ["SENDER_PASSWORD"]
        smtp_server = os.environ["SMTP_SERVER"]
        mail_content = f"{product_title} just went under {threshold} {currency} for a current price of {product_price} {currency}.\nGo get it!\n{product_url}"
        message = MIMEMultipart()
        message['From'] = sender_email
        message['To'] = receiver_email
        message['Subject'] = f"Price alert! {product_title}"
        message.attach(MIMEText(mail_content, 'plain'))
        session = smtplib.SMTP(smtp_server, 587)
        session.starttls()
        session.login(sender_email, sender_password)  # login with mail_id and password
        text = message.as_string()
        session.sendmail(sender_email, receiver_email, text)
        session.quit()
        print('Mail Sent')
