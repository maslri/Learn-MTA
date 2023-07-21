import smtplib

def prompt(prompt):
    return input(prompt).strip()

fromaddr = prompt("From: ")
toaddrs  = prompt("To: ").split()
password = prompt("Enter your password: ")

subject = prompt("Enter the subject: ").split()

print("Enter message, end with ^D (Unix) or ^Z (Windows):")
msg = ("From: %s\r\nTo: %s\r\nSubject: %s\r\n\r\n"
       % (fromaddr, ", ".join(toaddrs), ", ".join(subject)))
while True:
    try:
        line = input()
    except EOFError:
        break
    if not line:
        break
    msg = msg + line

print("Message: ", msg)
print("Message length is", len(msg))

server = smtplib.SMTP('smtp.gmail.com', 587)
server.set_debuglevel(1)
print(server.docmd(cmd="Return code status"))
server.starttls()
server.login(fromaddr, password)
print("login success")
server.sendmail(fromaddr, toaddrs, msg)
print("Email has been sent to" , toaddrs)
server.quit()