import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import datetime

def send_email(receiving_email, username):
    # Email details setup
    now_date = datetime.datetime.now().date()
    sending_email = "ENTER YOUR EMAIL HERE"
    sending_password = "ENTER YOUR EMAIL APP PASSWORD HERE"
    receiver_email = receiving_email
    subject = f"{username} Follower Report - {now_date}"
    file_path = "final_list.txt"

    with open(file_path, "r") as file:
        file_content = file.read()

    # Create message
    message = MIMEMultipart()
    message["From"] = sending_email
    message["To"] = receiver_email
    message["Subject"] = subject

    # Attach file to the message
    attachment = MIMEText(file_content)
    attachment.add_header("Content-Disposition", "attachment", filename=f"{username}_{now_date}.txt")
    message.attach(attachment)

    # Send email
    with smtplib.SMTP("ENTER YOUR EMAIL SMTP SERVER ADDRESS HERE", 587) as connection:
        connection.starttls()
        connection.login(user=sending_email, password=sending_password)

        connection.sendmail(from_addr=sending_email, to_addrs=receiver_email, msg=message.as_string())
