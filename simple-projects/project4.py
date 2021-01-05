#!/usr/bin/env python3
"""
# Author : Khalid Maina.
# Date : 20/12/2020
.....................................
Script that converts html body to pdf.
.....................................
"""
import os
import sys
from bs4 import BeautifulSoup
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet

html_file = os.path.join(os.getcwd(), 'projects-resources/project4.html') # you can change the path
pdf_file = os.path.join(os.getcwd(), 'project4.pdf') #you can change the path
styles = getSampleStyleSheet()

def extract_html_body(file):
	"""Extracts html body"""
	try:
		with open(file, 'rb') as html_file:
			html_content = BeautifulSoup(html_file)
	except FileNotFoundError:
		print('[-] File not exists.Check your file path.')
		sys.exit()
	html_body = html_content.body.string
	return html_body

def write_paragraph(html_body):
	"""Writes paragraph of a given html body """
	paragraph = Paragraph(html_body, styles['h1'])
	return paragraph

def main():
	try:
		pdf = SimpleDocTemplate(pdf_file)
	except Exception:
		raise
	html_body = extract_html_body(html_file)
	paragraph = write_paragraph(html_body)
	pdf.build([paragraph])
	print('Done.')
if __name__ == '__main__':
	main()
