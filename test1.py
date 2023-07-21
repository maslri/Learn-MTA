import smtplib
from email.message import EmailMessage
import ssl

def prompt(prompt):
    return input(prompt).strip()

fromaddr = prompt("From: ")
toaddrs  = prompt("To: ")
password = prompt("Enter your password: ")

subject = prompt("Enter the subject: ")
body = prompt("Enter the body of Email: ")

print("Message: ", body)
print("Message length is", len(body))

em = EmailMessage()
em['From'] = fromaddr
em['To'] = toaddrs
em['Subject'] = subject
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as server :
    server.login(fromaddr, password)
    print("login success")
    server.sendmail(fromaddr, toaddrs, em.as_string())
    print("Email has been sent to" , toaddrs)
