#!/usr/bin/env python
import os
import smtplib
from shutil import rmtree
from subprocess import Popen, PIPE, call
from sys import exit
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

developer_email = 'stewart_lynch@brown.edu'
sender ='lynchs@fitzgeraldautomall.com'
subject = "DO NOT REPLY: " + "Hello"
body = "HOPEFULLY THIS MESSAGE FINDS YOU IN GOOD AUTOMATED HEALTH MY FELLOW COMPUTER"

message = MIMEMultipart()
message['From'] = developer_email
message['To'] = sender
message['Subject'] = subject
message.attach(MIMEText(body,'plain'))


try:
	smtpObj = smtplib.SMTP("smtp.emailsrvr.com", 587)
	smtpObj.set_debuglevel(True)  # show communication with the server
	smtpObj.ehlo_or_helo_if_needed()
	smtpObj.starttls()
	smtpObj.login(sender,"sh0rtt1m3")
	smtpObj.sendmail(sender, developer_email, message.as_string())
	print("Successfully sent email.")
	smtpObj.quit()
except smtplib.SMTPHeloError:
	print("Error: The server didn't reply properly to the HELO greeting.")
except smtplib.SMTPException:
	print("Error: unable to send mail")
	print(smtplib.SMTPException.strerror)




"""
try:
	smtpObj = smtplib.SMTP("secure.emailsrvr.com", 465)
	smtpObj.set_debuglevel(True)  # show communication with the server
	smtp.ehlo_or_helo_if_needed()
	smtpObj.login(sender,"sh0rtt1m3")
	smtpObj.sendmail(sender,receivers, message)
	print("Successfully sent email.")
except smtplib.SMTPException:
	print("Error: unable to send mail")
	print(smtplib.SMTPException.strerror)
except smtplib.SMTPHeloError:
	print("Error: The server didn't reply properly to the HELO greeting.")

"""


