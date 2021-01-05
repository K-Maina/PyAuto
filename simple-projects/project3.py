#!/usr/bin/env python3
"""
# Author : Khalid Maina.
# Date : 12/12/2020
................................
Script that converts json to csv
................................
"""
import csv
import json
import os
import sys

json_path = os.path.join(os.getcwd(), 'projects-resources/project3.json') # you can change the path
csv_path = os.path.join(os.getcwd(), 'project3.csv') # you can change the path

def read_json(json_path):
	"""Reads json data"""
	try:
		with open(json_path, 'r') as json_file:
			json_data = json.load(json_file)
	except FileNotFoundError:
		print('[-] File not exists.Check your file path.')
		sys.exit()
	return json_data

def write_csv(csv_path, json_data):
	"""Writes json data into csv file """
	headers = json_data[0].keys()
	try:
		with open(csv_path, 'w') as csv_file:
			writer = csv.DictWriter(csv_file, fieldnames = headers)
			writer.writeheader()
			writer.writerows(json_data)
	except Exception:
		raise
	return True

def main():
	json_data = read_json(json_path)
	is_written = write_csv(csv_path, json_data)
	if is_written:
		print('Done.')

if __name__ == '__main__':
	main()
