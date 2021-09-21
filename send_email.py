# smtplib: https://docs.python.org/3/library/smtplib.html
# gmail service to send email
# login to gmail and send email with Subject and body to sender Email
# Email and password are saved but can be fetched using input command

import smtplib


SENDER_EMAIL='test@test.com'
SENDER_PASSWORD='password2Long!'

def send_email(receiver_email, subject, body):
    message = 'Subject: {}\n\n{}'.format(subject, body)
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
        server.login(SENDER_EMAIL, SENDER_PASSWORD)
        server.sendmail(SENDER_EMAIL, receiver_email,message)

send_email('senderemail@gmail.com', 'Notification', 'All Done!')
