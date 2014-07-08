#!/usr/bin/python

import smtplib

sender = 'lynchs@fitzgeraldautomall.com'
receivers = ['lynch.s.101@gmail.com']

message = """From: From Person <from@fromdomain.com>
To: Stewart <stewart_lynch@brown.edu.com>
Subject: SMTP e-mail test

This is a test e-mail message.
"""

try:
   smtpObj = smtplib.SMTP('localhost')
   smtpObj.sendmail(sender, receivers, message)         
   print("Successfully sent email")
except smtplib.SMTPException:
   print("Error: unable to send email")