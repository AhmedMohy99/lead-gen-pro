import smtplib
from config import EMAIL_SENDER, EMAIL_PASSWORD

def send_email(to_email, name):
    subject = "Grow your business online"
    message = f"""
Hello {name}

I can help you build a professional website and bring more customers.

Let me know if you are interested
"""

    full_message = f"Subject: {subject}\n\n{message}"

    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(EMAIL_SENDER, EMAIL_PASSWORD)
        server.sendmail(EMAIL_SENDER, to_email, full_message)
        server.quit()
    except:
        pass
