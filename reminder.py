from email.message import EmailMessage
import ssl

import smtplib
email_sender = 'poojithreddymenthem@gmail.com'
email_password = 'zsfj zfdv eanb elfp'
email_receiver ='giyol15280@irnini.com'

subject = "Reminder! Take the medicine"
body = """
It's time to take the medicine. Please take the medicine on time.
""" 
em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['subject']= subject
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com',465,context=context)as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender,email_receiver,em.as_string())