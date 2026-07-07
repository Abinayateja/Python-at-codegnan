# import required modules
from smtplib import SMTP
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


# SERVER CONFIGARATION
smtp_server = "smtp.gmail.com"
smtp_port = 587
sender_email="irshadshaik5656@gmail.com"
passkey = "imnofbgwtemiwfwi"
def singleEmailSend(to_email:str,subject:str,body:str):
    msg = MIMEMultipart()
    msg['TO']= to_email
    msg['from']=sender_email
    msg['subject']=subject
    msg.attach(MIMEText(body,'plain'))


    try:
        # start server
        server = SMTP(smtp_server,smtp_port)
        # start server
        server.starttls()
        #login to server
        server.login(sender_email,passkey)
        # send email
        server.sendmail(from_addr=sender_email,to_addrs=to_email,msg=msg.as_string())
        server.quit()
        return f"successfully email send to{to_email}"
    except  Exception as e:
        return f"faild to send email because: {e}"


to_email=input("enter Email address: ")
subject=input("Enter Email Subject: ")
body= input("Enter Email Body: ")
print(singleEmailSend(to_email,subject,body))