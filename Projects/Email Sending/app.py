# import required libraries
from smtplib import SMTP
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from dotenv import load_dotenv
import os

load_dotenv()
# Server Configuration
smtp_server = os.getenv("SMTP_SERVER")
smtp_port = int(os.getenv("SMTP_PORT"))
sender_email = os.getenv("SENDER_EMAIL")
passkey = os.getenv("PASSKEY")

def singleEmailSend(to_email:str,subject:str,body:str):
    msg = MIMEMultipart()
    msg['To'] = to_email
    msg['From'] = sender_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body,'plain'))

    try:
        # Start Server
        server = SMTP(smtp_server,smtp_port)
        # Start Server
        server.starttls()
        # login to server
        server.login(sender_email,passkey)
        # send email
        server.sendmail(from_addr=sender_email,to_addrs=to_email,msg = msg.as_string())
        server.quit()
        return f"Successfully email sent to {to_email}"
    except Exception as e:
        return f"Failed to send email because: {e}"
    
to_email  = input("Enter Email address: ")
subject = input("Enter Email Subject: ")
body = input("Enter Email Body: ")
print(singleEmailSend(to_email=to_email,subject=subject,body=body))