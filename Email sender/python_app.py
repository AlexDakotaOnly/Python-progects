from email.message import EmailMessage
from pw import password    #for 2-factor authentication only
import ssl
import smtplib

 email_sender = 'nataly.tyler@gmail.com'
 email_password = password

 email_receiver = 'polomow529@kuvasin.com'

subject = "Don't forget"
body = """
When you watch video
"""
em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['subject'] = subject
em.set_content(body)

context = ssl.create_default_context()
with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
 smtp.login(email_sender, email_password)
 smtp.sendmail(email_sender, email_receiver, em.as_string())