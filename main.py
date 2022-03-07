import smtplib

my_email = "uditmiishraa@gmail.com"
password = "Ram@1010420"

with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
    connection.starttls()  # This is for encryption of message sent over the protocol
    connection.login(user=my_email, password=password)
    connection.sendmail(
        from_addr=my_email,
        to_addrs="tarangmishraa@yahoo.com",
        msg="Subject:Hello there!\n\nThis is the body of my email."
    )
