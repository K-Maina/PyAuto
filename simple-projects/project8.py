#!usr/bin/env python3
"""
# Author : Khalid Maina.
# Date : 12/12/2020
.................................................................
Script that extracts excel data and writes them in a table in pdf
.................................................................
"""
import os
import sys
from openpyxl import load_workbook
from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import (Table, TableStyle)
from reportlab.lib import colors

pdf_path = os.path.join(os.getcwd(), 'project8.pdf') #you can change the path
excel_path = os.path.join(os.getcwd(), 'projects-resources/project8.xlsx') # you can change the path
row_start = 'A1'
row_end = 'E10'
pdf_table_style = [('GRID',(0,0),(-1,-1),2,colors.red),('BACKGROUND',(0,0),(-1,-10),colors.blue)]

def extract_excel_data(sheet, row_start, row_end):
	"""Extracts excel data from a  excel file.Returns list of tuple of the data"""
	excel_data = sheet[row_start : row_end]
	row_list = []
	for row in excel_data:
		row_values = []
		for cell in row:
			row_values.append(cell.value)
		row_list.append(tuple(row_values))

	return row_list

def generate_pdf_table(excel_data, pdf_table_style):
	"""Generates pdf table of the given data"""
	table_style = TableStyle(pdf_table_style)
	table = Table(excel_data, hAlign = 'LEFT')
	table.setStyle(table_style)
	return table

def build_pdf(pdf, table):
	"""Builds pdf """
	pdf.build([table])
	return True

def main():
	try:
		workbook = load_workbook(excel_path)
		pdf = SimpleDocTemplate(pdf_path)
	except FileNotFoundError:
		print('[-] File not exists.Check your file path.')
		sys.exit()
	sheet = workbook.active
	excel_data = extract_excel_data (sheet, row_start, row_end)
	table = generate_pdf_table(excel_data, pdf_table_style)
	is_built = build_pdf(pdf, table)

	if is_built:
		print('Done.')

if __name__ == '__main__':
	main()
