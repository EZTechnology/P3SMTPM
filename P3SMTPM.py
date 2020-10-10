#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys, traceback

sys.path.insert(0, '../')
import re
import smtplib
import time


from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

try:

	fileopen = open('maillist.txt', 'r')
	for line in fileopen:

		From = "sendingemail@domain.net"
		match = re.search(r'[\w\.-]+@[\w\.-]+', line)
		if match is None:
			email = str(None)
			print(email)
		elif match:
			To = match.group(0)

			msg = MIMEMultipart()
			msg['From']    = From
			msg['To']      = To
			msg['Subject'] = 'THE SUBJECT'

			handle = open("mail.html", "r")
			html = handle.read()
			handle.close()

			msg.attach(MIMEText(html, 'html', 'utf-8'))          # check your email encoding
			server = smtplib.SMTP('smtp.domain.net', 587)
			server.set_debuglevel(False)                         # 4 Debug
			server.starttls()
			server.login("sendingemail@domain.net", "P@ssw0rD")                         # If Auth Needed
			server.send_message(msg)
			server.quit()
			print("Sent: " + str(To))
			# time.sleep(1)               #un-comma if sleep needed (Quota 4 example)

except smtplib.SMTPRecipientsRefused as e:
	print(e)

except smtplib.SMTPException as e:
	print(e)

except smtplib.SMTPServerDisconnected as e:
	print(e)

except KeyboardInterrupt:
	print("Program Stop")

except UnicodeEncodeError:
	print("Check email for encoding (possibly win1251, need utf-8)")

except:
	print('-' * 50)
	print("All Else Errors")
	traceback.print_exc(limit=2, file=sys.stdout)
	print('-' * 50)