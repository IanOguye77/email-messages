import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import schedule
import time

def send_email():
    # Email configuration
    sender_email = "#@gmail.com"  # Your email address
    receiver_email = "#@gmail.com"  # Recipient email address
    subject = "Daily Report"
    
    # Compose the email body
    body = """
    Hello,

    This is your daily report.

    Regards,
    #
    """

    # Setup the MIME
    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = receiver_email
    message['Subject'] = subject

    # Attach the body to the email
    message.attach(MIMEText(body, 'plain'))

    # Connect to the SMTP server (for Gmail)
    smtp_server = "#.gmail.com"
    smtp_port = 587
    smtp_username = "#@gmail.com"  # Your email address
    smtp_password = "#"  # Your email password

    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(smtp_username, smtp_password)

        # Send the email
        server.sendmail(sender_email, receiver_email, message.as_string())

        # Close the connection
        server.quit()

# Schedule the script to run daily
schedule.every().day.at("08:00").do(send_email)  # Adjust the time as needed

# Run the scheduler
while True:
    schedule.run_pending()
    time.sleep(1)
