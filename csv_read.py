import csv
from ast import literal_eval
from pprint import pprint

def read_csv(file_name='data-set.csv'):
	csv_as_tuple = None
	with open(file_name, encoding='utf-8-sig') as file:
		reader = csv.reader(file, skipinitialspace=True)
		csv_as_tuple = [tuple(map(literal_eval, csv_as_tuple)) for csv_as_tuple in map(tuple, reader)]
	return csv_as_tuple
