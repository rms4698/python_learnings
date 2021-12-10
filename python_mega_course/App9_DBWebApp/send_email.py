from email.mime.text import MIMEText
import smtplib


def send_email(email_id, height, average_height, count):
    from_email = "rms4698@gmail.com"
    from_PW = "Muthuram123"

    to_email = email_id
    subject = "Height Data"
    message = f"Hey there!\n \
               Your height is <strong>{height} cm</strong>.\n\
               Average height is <strong>{average_height} cm</strong>.\
               It is calculated out of {count} people"

    msg = MIMEText(message, 'html')
    msg["Subject"] = subject
    msg["To"] = to_email
    msg["From"] = from_email

    gmail = smtplib.SMTP("smtp.gmail.com", 587)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(from_email, from_PW)
    gmail.send_message(msg)


if __name__ == "__main__":
    send_email("rms4698@gmail.com", 50)
