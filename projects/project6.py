#!/usr/bin/env python3
"""
# Author : Khalid Maina.
# Date : 18/12/2020.
............................................
Script that replaces a given word in a file.
............................................

"""
import os
import sys

text_file = os.path.join(os.getcwd(), 'projects-resources/project6.txt') # you can change the path
new_file = os.path.join(os.getcwd(), 'project6.txt') #you can change the path
old_word = 'hacker'
new_word = 'programmers'

def replace(file, old, new):
	"""replaces word from a given file"""
	try:
		with open(file, 'r') as txt_file:
			content = txt_file.read()
			new_content = content.replace(old, new)
	except FileNotFoundError:
		print('[-] File not exists.Check your file path.')
		sys.exit()
	return new_content

def write_new_file(new_file, content):
	"""writes a file """
	try:
		with open(new_file, 'w') as txt_file:
			content = txt_file.write(content)
	except Exception:
		raise
	return True

def main():
	content = replace(text_file, old_word, new_word)
	is_written = write_new_file(new_file, content)
	if is_written:
		print('Done.')

if __name__ == '__main__':
	main()
