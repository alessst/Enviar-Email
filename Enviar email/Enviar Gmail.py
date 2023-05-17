import smtplib
import email.message
from Texto import texto1, texto2

def enviar_email(email_texto):  
    msg = email.message.Message()
    msg['Subject'] = "Assunto"
    msg['From'] = ''
    msg['To'] = ''
    password = '' 
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(email_texto)

    s = smtplib.SMTP('smtp.gmail.com: 587')
    s.starttls()
    # Login Credentials for sending the mail
    s.login(msg['From'], password)
    s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
    print('Email enviado')

enviar_email()