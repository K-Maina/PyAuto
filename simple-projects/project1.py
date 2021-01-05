#!/usr/bin/env python3
"""
# Author : Khalid Maina.
# Date : 12/12/2020

.............................................................................................................
Script that copies first and last columns of the data in an excel file and writes them in a table in pdf file.
.............................................................................................................

"""
import os
from openpyxl import load_workbook
from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import (Table, TableStyle)
from reportlab.lib import colors

pdf_path = os.path.join(os.getcwd(), 'project1.pdf') # You can change the path
excel_path = os.path.join(os.getcwd(), 'projects-resources/project1.xlsx') # You can change the path
pdf_table_style = [('GRID',(0,0),(-1,-1),2,colors.pink)]
first_cols = 'A'
last_cols = 'E'

def copy_first_last_cols(sheet, first_col, last_col):
	"""Copies first and last columns of the excel file"""
	cols_list = []
	first_cols = [cell.value for cell in sheet[first_col]]
	last_cols = [cell.value for cell in sheet[last_col]]
	cols_list.append(first_cols)
	cols_list.append(last_cols)

	return cols_list

def generate_pdf_table(excel_data, pdf_table_style):
	"""Generates pdf table of the given data"""
	try:
		table_style = TableStyle(pdf_table_style)
		table = Table(excel_data)
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
		workbook = load_workbook(excel_path)
		pdf = SimpleDocTemplate(pdf_path)
	except Exception:
		raise
	sheet = workbook.active
	excel_data = copy_first_last_cols(sheet, first_cols, last_cols)
	table = generate_pdf_table(excel_data, pdf_table_style)
	is_built = build_pdf(pdf, table)

	if is_built:
		print('Done.')

if __name__ == '__main__':
	main()
