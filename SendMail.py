
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from datetime import datetime

def send_email():
    # Set up email and password
    sender_email = "qualityteam231@gmail.com"  # Your email
    app_password = "uojo tjfs dluw molk"  # Your app password

    # Set up the recipient email addresses
    recipients = [ "sabatali@devaxon.com", "35918.it4@gmail.com"]

    # Create a message
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = ", ".join(recipients)
    message["Subject"] = "nextdoor Post Data"

    # Add body to email csv files
    body = "The script creates a file named nextdaoor_data.csv containing the scraped data."
    message.attach(MIMEText(body, "plain"))

    # Attach CSV files
    filenames = ["complete_merged_file.csv", "last_hour_data.csv"]  # Path to CSV files
    for filename in filenames:
        attachment = open(filename, "rb")
        part = MIMEBase("application", "octet-stream")
        part.set_payload((attachment).read())
        encoders.encode_base64(part)
        part.add_header("Content-Disposition", f"attachment; filename= {filename}")
        message.attach(part)
        attachment.close()

    # Connect to the SMTP server
    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()  # Secure the connection
        # Log in to Gmail account
        server.login(sender_email, app_password)
        # Send the email
        server.send_message(message)
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print("Email sent successfully!", current_time)

# Call the send_email function directly
send_email()
