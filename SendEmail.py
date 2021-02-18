import email, smtplib, ssl
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from re import search, sub

with open("keywordHits.txt", "r+", encoding='utf-8', errors='ignore') as txt:
    body = txt.read()
    body = sub("["+"\[\],"+"]", "", str(body))

with open("keywordHits.txt", "w") as txt:
    txt.write('')

def sendEmail(body):
    message = MIMEMultipart()
    message["From"] = '[email]'
    message["To"] = '[email]'
    message["Subject"] = 'Reddit Keyword Hit(s)'
    message.attach(MIMEText(body))
    text = message.as_string()

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login('[email]', '[email]' )
        server.sendmail('[FromEmail]', '[ToEmail]', text)
        server.quit()

sendEmail(body)