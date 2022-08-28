import smtplib


# Данные почтового сервера
USER = 'mail@gmail.com'
PASSWORD = 'password'
SERVER = 'smtp.gmail.com'
PORT = 587

def send_mails(data):
    try:        
        server = smtplib.SMTP(SERVER, PORT)
        server.ehlo()
        server.starttls()
        server.login(USER, PASSWORD)
        for account in data:
            message = f'Привет, {account["name"]}, твой результат: {account["result"]}'
            body = '\r\n'.join(('Subject: Счастливое письмо', '',message))        
            server.sendmail(USER, account['email'], body.encode())
    except Exception as e:
        print(e)
    finally:
        server.close()


