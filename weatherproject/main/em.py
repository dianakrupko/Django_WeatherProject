import smtplib
from password import password
from email.mime.multipart import MIMEMultipart
from bs4 import BeautifulSoup as bs

# ваши учетные данные
email = "didididididi.kk@gmail.com"
password = password
# электронная почта отправителя
FROM = "didididididi.kk@gmail.com"
# адрес электронной почты получателя
TO = "dnkrupkoo@gmail.com"
# тема письма (тема)
subject = "Report"

# инициализируем сообщение, которое хотим отправить
msg = MIMEMultipart("alternative")
# установить адрес электронной почты отправителя
msg["From"] = FROM
# установить адрес электронной почты получателя
msg["To"] = TO
# задаем тему
msg["Subject"] = subject

# установить тело письма как HTML
html = """
This email is sent using <b>Python</b>!
"""
# делаем текстовую версию HTML
text = bs(html, "html.parser").text


# print(msg.as_string())
def send_mail(email, password, FROM, TO, msg):
    # инициализировать SMTP-сервер
    server = smtplib.SMTP("smtp.gmail.com", 587)
    # подключиться к SMTP-серверу в режиме TLS (безопасный) и отправить EHLO
    server.starttls()
    # войти в учетную запись, используя учетные данные
    server.login(email, password)
    # отправить электронное письмо
    server.sendmail(FROM, TO, msg.as_string())
    # завершить сеанс SMTP
    server.quit()


# отправить почту
send_mail(email, password, FROM, TO, msg)
