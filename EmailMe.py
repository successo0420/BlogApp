import smtplib
import os

password = os.environ.get("PASSWORD")
sender_email = os.environ.get("SENDER_EMAIL")
receiver_email = os.environ.get("RECEIVER_EMAIL")


class EmailMe:
    def send_email(self, message):
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=sender_email, password=password)
            connection.sendmail(from_addr=sender_email, to_addrs=receiver_email, msg=f"Subject: Message from Blogger! "
                                                                                     f"\n\n{message}")
            print(f"Successfully Sent to {receiver_email}")
