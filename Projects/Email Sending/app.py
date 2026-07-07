# import required libraries
from smtplib import SMTP
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Server Configuration
smtp_sever = "smtp.gmail.com"
smtp_port = 587
sender_email = "gaddamabinayateja@gmail.com"
passkey = "hwjlhwgpnrlqtpab"

def singleEmailSend(to_email:str,subject:str,body:str):
    msg = MIMEMultipart()
    msg['To'] = to_email
    msg['From'] = sender_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body,'plain'))

    try:
        # Start Server
        server = SMTP(smtp_sever,smtp_port)
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