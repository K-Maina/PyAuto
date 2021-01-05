#!usr/bin/env python3
"""
# Author : Khalid Maina
# Date : 11/12/2020
...........................................
Script that sends email message to an email
...........................................
"""
import smtplib
import sys
import socket
from email.message import EmailMessage

#Make sure to change the info below
sender_email = 'sender@domain.com'
receiver_email = 'receiver@domain.com'
email_subject = 'Greating'
email_body = 'Hello,World!'

server ='localhost' #Change to your email server domain
username = 'user' #Change to your username
password = 'userpass' #Change to your password

def generate_message(sender, receiver, subject = '', body = ''):
	"""Generates email message"""
	message = EmailMessage()
	message['From'] = sender
	message['To'] = receiver
	message['Subject'] = subject
	message.set_content(body)
	return message

def send_email(server, username, password, message):
	"""Connects and sends the message to a given emails"""
	try:
		with smtplib.SMTP_SSL(server, timeout =10) as smtp_server:
			smtp_server.login(username, password)
			unreacheable_list = smtp_server.send_message(message)
	except (ConnectionRefusedError, socket.gaierror):
		print('[-] Cant connect to the server.Please check your smtp server')
		sys.exit()
	except socket.timeout:
		print('[-] timeout.Please check your network connections.')
		sys.exit()
	except smtplib.SMTPAuthenticationError:
		print('[-] Bad credentials.Check your password')
		sys.exit()
	return unreacheable_list

def main():
	message = generate_message(sender_email, receiver_email, email_subject, email_body)
	send_email(server, username, password, message)

if __name__ == '__main__':
	main()
