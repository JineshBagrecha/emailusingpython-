import pymysql
import smtplib

connection = pymysql.connect (host = "localhost", user = "root", passwd = "jinesh123", db = "sample")
cursor = connection.cursor ()


# creates SMTP session
s = smtplib.SMTP('smtp.gmail.com', 587)

# start TLS for security
s.starttls()

# Authentication
s.login("sender_email_id", "password")

cursor.execute("select advisor_id,advisor_name from advisor")
data = cursor.fetchall ()
message = ""
for row in data:

    message = message + str(row[0]) + "," + row[1] + "\n"

# sending the mail
s.sendmail("sender_email_id", "receiver_email_id", message)

# terminating the session
s.quit()

