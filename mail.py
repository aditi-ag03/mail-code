#!/usr/bin/python3
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
email_content="hello"
sender_address=''
sender_pass=''
receiver_address=''
message=MIMEMultipart()
message['From']=sender_address
message['To']=receiver_address
message['Subject']='APPLICATION STATUS ALERT!!'
message.attach(MIMEText(email_content,'plain'))
session=smtplib.SMTP('smtp.gmail.com',587)
session.starttls()
session.login(sender_address,sender_pass)
text=message.as_string()
session.sendmail(sender_address,receiver_address,text)
session.quit()
print('Mail sent successfully!!')