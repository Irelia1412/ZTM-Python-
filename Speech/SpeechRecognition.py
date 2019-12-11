import smtplib
from email.message import EmailMessage

email= EmailMessage()
email['from']= 'Irelia'
email['to']='nphamood14@gmail.com'
email['subject']= " Nice "
email.set_content("You are cute !" )
with smtplib.SMTP(host='smtp.gmail.com', port = 587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('nphamood6@gmail.com', '1010-1010M')
    smtp.send_message(email)
    print("All good !")