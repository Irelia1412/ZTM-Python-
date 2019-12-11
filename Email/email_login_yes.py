import smtplib
from email.message import EmailMessage

email= EmailMessage()
email['from']= "Andrei"
email['to']="nphamood2@gmail.com"
email['subject']= " Hello "
email.set_content("You are cute !" )
with smtplib.SMTP(host='smtp.gmail.com', port = 587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login("nphamood100@gmail.com" , "********")
    smtp.send_message(email)
    print("All good !")
