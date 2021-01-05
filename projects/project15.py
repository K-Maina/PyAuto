#!usr/bin/env python3
"""
# Author : Khalid Maina
# Date : 11/12/2020
......................................
Script that sends pdf file to an email
......................................
"""
import smtplib
import mimetypes
import os
import sys
import socket
from email.message import EmailMessage

file_path = os.path.join(os.getcwd(), 'projects-resources/project15.txt') #change the path
mimetype, __ = mimetypes.guess_type(file_path)
main_type, sub_type = mimetype.split('/',1)
filename = os.path.basename(file_path)

#Make sure to change the info below
sender_email = 'sender@domain.com'
receiver_email = 'receiver@domain.com'
email_subject = 'next year schedule'
email_body = 'This is the pdf'

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

def add_attachment(message, file_path, main_type, sub_type, filename):
	"""Add an attachment to the email message"""
	try:
		with open(file_path, 'rb') as pdf:
			message.add_attachment(pdf.read(), maintype = main_type, subtype = sub_type, filename = filename)
	except FileNotFoundError:
		print("[-] File does'nt exist.Please check your file path")
		sys.exit()
	return True

def send_email(server, username, password, message):
	"""Connects and sends the message to a given emails"""
	try:
		with smtplib.SMTP_SSL(server, timeout = 10) as smtp_server:
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
	add_attachment(message, file_path, main_type, sub_type, filename)
	send_email(server, username, password, message)

if __name__ == '__main__':
	main()
