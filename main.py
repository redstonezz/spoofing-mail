# Tools untuk spoofing email
# Dibuat oleh giovanni victo
# Email victoarayagiovanni231@gmail.com

# modul yang diperlukan
import random
import smtplib
from email.mime.text import MIMEText

# setting pengirim dan penerima
sender = 'pengirim@gmail.com' #isi dengan email asli pengirim
receivers = ['penerima@gmail.com'] #isi dengan email asli penerima

# port smtp server
port = 587 

# Setting alamat smtp server dan menghubungkannya
with smtplib.SMTP('smtp-relay.sendinblue.com', 587) as server: #isi domain smtp server anda, disini saya menggunakan smtp dari sendinblue, dan port yang saya gunakan 587
    for i in range(1):  # value disini menunjukan berapa banyak email yang mau dikirim
        randnum = random.randint(0, 999)
        msg = MIMEText(f'this is phsihingmail')  # pesan email / email body
        msg['Subject'] = 'testphish'  # judul email/ subject email
        msg['From'] = f'pengirim@gmail.com' #from header pengirim
        msg['To'] = 'penerima@gmail.com' # to header email
        server.login('usernameloginsmtpserver', 'smtpkey-password') # SMTP kredensial . Isi sesuai dengan yang ada pada smtp server kalian
        server.sendmail(sender, receivers, msg.as_string()) # Composing the email
        print("Successfully sent email", i+1) # pesan yang tertera apabila email berhasil terkirim
