#!usr/bin/env python3
"""
# Author : Khalid Maina
# Date : 12/12/2020
.........................................................
Script that write a json file from a list of dictionaries
.........................................................
"""
import csv
import os

data = [
	dict(name = 'Ibrahim ali', email = 'Ali@gmail.com'),
	dict(name = 'Idriss ismali', email = 'idris@gmail.com'),
	dict(name = 'joseph moses', email = 'joseph@yahoo.com')
	]

csv_file_path = os.path.join(os.getcwd(), 'project7.json') #you can change the path
headers = data[0].keys()

def write_csv(file_path, data, headers):
	"""Writes csv file of the given data.Returns True if successful"""
	try:
		with open(file_path, 'w') as csv_file:
			writer = csv.DictWriter(csv_file, fieldnames = headers)
			writer.writeheader()
			writer.writerows(data)
	except Exception:
		raise
	return True

def main():
	is_written = write_csv(csv_file_path, data, headers)
	if is_written:
		print('Done.')

if __name__ == '__main__':
	main()
