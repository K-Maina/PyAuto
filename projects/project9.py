#!usr/bin/env python3
"""
# Author : Khalid Maina.
# Date : 12/12/2020
...............................................................
Script that extracts csv data and writes them in a table in pdf
...............................................................
"""
import csv
import sys
import os
from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import (Table, TableStyle)
from reportlab.lib import colors

pdf_path = os.path.join(os.getcwd(), 'project9.pdf') #you can change the path
csv_path = os.path.join(os.getcwd(), 'projects-resources/project9.csv') # you can change the path
pdf_table_style = [('GRID',(0,0),(-1,-1),2,colors.red),('BACKGROUND',(0,0),(-1,-10),colors.green)]

def extract_csv_data(csv_path):
	"""extracts csv data"""
	row_list = []
	try:
		with open(csv_path, 'r') as csv_file:
			reader = csv.reader(csv_file)
			for row in reader:
				row = tuple(row)
				row_list.append(row)
	except FileNotFoundError:
		print('[-] File not exists.Check your file path.')
		sys.exit()
	return row_list

def generate_pdf_table(csv_data, csv_table_style):
	"""Generates pdf table of the given data"""
	try:
		table_style = TableStyle(pdf_table_style)
		table = Table(csv_data, hAlign = 'LEFT')
	except Exception:
		raise
	table.setStyle(table_style)
	return table

def build_pdf(pdf, table):
	"""build pdf """
	try:
		pdf.build([table])
	except Exception:
		raise
	return True

def main():
	try:
		pdf = SimpleDocTemplate(pdf_path)
	except Exception:
		raise
	csv_data = extract_csv_data(csv_path)
	table = generate_pdf_table(csv_data, pdf_table_style)
	is_built = build_pdf(pdf, table)

	if is_built:
		print('Done.')

if __name__ == '__main__':
	main()
