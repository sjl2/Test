#!/usr/bin/env python
import smtplib
from getpass import getpass
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
#from google.appengine.api import oauth

def BombsAway(bomber, password, targets, body):
	try:
		smtpObj = smtplib.SMTP("smtp.gmail.com", 587)
		smtpObj.ehlo_or_helo_if_needed()
		smtpObj.starttls()
		smtpObj.login(bomber, password)
		for i in range(1,21):
			print("Count: " + str(i))
			message = MIMEMultipart()
			message['From'] = bomber
			message['To'] = ",".join(targets)
			message['Subject'] = ("Hell" + ("o"*i)) 
			message.attach(MIMEText(body,'plain'))
			smtpObj.sendmail(bomber, targets, message.as_string())


		smtpObj.quit()
	#except oauth.OAuthRequestError as ex:
	#	print("OAuthRequestError ({0}): {1}".format(ex.errno, ex.strerror))
	except smtplib.SMTPHeloError as ex:
		print("Error: The server didn't reply properly to the HELO greeting.")
	except smtplib.SMTPException as ex:
		print("Error: unable to send mail")
		print("SMTPException ({0}): {1}".format(ex.errno, ex.strerror))

def Body():
	return "Hi Annmarie! \nSorry for all the emails. I felt the need to say \"hi\", and this is the best way to do so."

bomber = input('Bomber\'s Gmail: ')
password = getpass()
targets = ['stewart_lynch@brown.edu','awiehen1@binghamton.edu']

BombsAway(bomber, password, targets, Body())
