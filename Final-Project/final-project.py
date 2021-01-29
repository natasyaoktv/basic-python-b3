import smtplib, ssl


port = 465  # For SSL
smtp_server = "smtp.gmail.com"

# sender address
sender = "ssipproject12@gmail.com" 

f = open("receiver-list.txt", "r")
x = f.readlines()
receiver = x  
password = input("Masukkan password dan tekan enter: ")

subject = input("Masukkan subject: ")
content = input("Masukkan isi: ")

message = """\
Subject: {}
{}""".format(subject, content)

context = ssl.create_default_context()
with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.login(sender, password)
    server.sendmail(sender, receiver, message)

#https://medium.com/paul-zhao-projects/sending-emails-with-python-c084b55a2857
