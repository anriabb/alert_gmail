import smtplib
from email.mime.text import MIMEText

SMTP_HOST = "smtp.gmail.com"
SMTP_PORT = 465 
SMTP_USE_SSL = True
SMTP_USER = "example@gmail.com"
SMTP_PASS = "123456789abcdefg"
SENDER = "example@gmail.com"
RECIPIENT = "example@gmail.com"

def send_simple_email(subject: str, body: str):
    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = SENDER
    msg["To"] = RECIPIENT
    
    with smtplib.SMTP_SSL(SMTP_HOST, SMTP_PORT, timeout=10) as smtp:
        smtp.login(SMTP_USER, SMTP_PASS)
        smtp.sendmail(SENDER, [RECIPIENT], msg.as_string())


if __name__ == "__main__":
    send_simple_email("SUBJECT", "BODY")
    print("Email sent")

