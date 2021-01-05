#!/usr/bin/env python3
"""
# Author : Khalid Maina.
# Date : 16/12/2020
..........................................................................
Scripts that extracts emails from json file and sends email message to each email.
...........................................................................
"""
import mimetypes
import smtplib
import os
import sys
import socket
import json
from email.message import EmailMessage

json_path = os.path.join(os.getcwd(), 'projects-resources/project12.json') #you can change the path
text_path = os.path.join(os.getcwd(), 'projects-resources/project10.txt') #you can change the path
mimetype, __ = mimetypes.guess_type(text_path)
main_type, sub_type= mimetype.split('/',1)
filename = os.path.basename(json_path)

sender_email = 'sender@domain.com' #Change the sender_email
email_subject = 'About Python'
email_body = 'New update open the file'

server ='your smtp server' #Change to your email server domain
username = 'username' #Change to your username
password = 'password' #Change to your password

def extract_email_addresses(file_path):
	"""Extracts emails from json file """
	try:
		with open(file_path, 'r') as json_file:
			data = json.load(json_file)
	except FileNotFoundError:
		print("[-] File does'nt exist.Please check your file path")
		sys.exit()
	email_list = [row['email'] for row in data]
	return email_list

def craft_email_message(message, sender, receiver_emails, subject, body):
	"""Crafts emails message """
	message['From'] = sender
	message['To'] = receiver_emails
	message['Subject'] = subject
	message.set_content(body)
	return message

def add_attachment(message, file_path, main_type, sub_type, filename):
	"""Adds an attachment to the email message"""
	try:
		with open(file_path, 'rb') as excel:
			message.add_attachment(excel.read(), maintype = main_type, subtype = sub_type, filename = filename)
	except FileNotFoundError:
		print("[-] File does'nt exist.Please check your file path")
		sys.exit()
	return True

def main():
	try:
		with smtplib.SMTP_SSL(server, timeout = 10) as smtp_server:
			smtp_server.login(username, password)
			message = EmailMessage()
			receiver_emails = extract_email_addresses(json_path)
			email_message = craft_email_message(message, sender_email, receiver_emails, email_subject, email_body)
			add_attachment(message, text_path, main_type, sub_type, filename)
			unreacheable = smtp_server.send_mesage(email_message)
			if not unreacheable:
				print('{} are unreacheable'.format(unreacheable))
	except (ConnectionRefusedError, socket.gaierror):
		print('[-] Cant connect to the server.Please check your smtp server')
		sys.exit()
	except socket.timeout:
		print('[-] timeout.Please check your network connections.')
		sys.exit()
	except smtplib.SMTPAuthenticationError:
		print('[-] Bad credentials.Check your password')
		sys.exit()
	return True

if __name__ == '__main__':
	main()
