#!/usr/bin/env python3
"""
# Author : Khalid Maina.
# Date : 12/12/2020
.....................................
Script that converts csv to json
.....................................

"""
import csv
import json
import os
import sys

csv_file= os.path.join(os.getcwd(), 'projects-resources/project2.csv') # You can change the path
json_file = os.path.join(os.getcwd(), 'project2.json')  # You can change the path

def read_csv(csv_path):
	"""Reads csv data"""
	row_dict_list = []
	try:
		with open(csv_path, 'r') as csv_file:
			reader = csv.DictReader(csv_file)
			for row in reader:
				row_dict_list.append(row)
	except FileNotFoundError:
		print('[-] File not exists.Check your file path.')
		sys.exit()
	return row_dict_list

def write_json(json_path, csv_data):
	"""Writes csv data into json file """
	try:
		with open(json_path, 'w') as json_file:
			json.dump(csv_data, json_file, indent = 3)
	except Exception:
		raise
	return True

def main():
	csv_data = read_csv(csv_file)
	is_written = write_json(json_file, csv_data)
	if is_written:
		print('Done.')

if __name__ == '__main__':
	main()
