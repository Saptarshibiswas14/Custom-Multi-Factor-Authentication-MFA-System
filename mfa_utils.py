import random, smtplib
from email.message import EmailMessage
from datetime import datetime

def generate_otp():
    return str(random.randint(100000, 999999))

def send_otp_email(to_email, otp):
    msg = EmailMessage()
    msg.set_content(f"Your OTP is: {otp}")
    msg['Subject'] = "Your Login OTP"
    msg['From'] = "your_email@example.com"
    msg['To'] = to_email

    # Replace with your email provider settings
    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.starttls()
        smtp.login('your_email@example.com', 'your_app_password')
        smtp.send_message(msg)

def is_otp_valid(user, entered_otp):
    return user.otp == entered_otp and datetime.now() <= user.otp_expiry
