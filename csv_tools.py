import csv

def csv_read_to_list_of_dicts(filepath, desiredColumns = None):
	list_of_dict = []
	with open(filepath, 'rU') as csvfile:
		csvreader = csv.DictReader(csvfile)
		if desiredColumns == None:
			desiredColumns = csvreader.fieldnames

		for row in csvreader:
			list_of_dict.append({})
			for key,value in row.iteritems():
				if key in desiredColumns:
					try:
						value = float(value)
					except:
						pass
					finally:
						list_of_dict[-1][key] = value
	return list_of_dict

def csv_get_column_headers(filepath):
	with open(filepath, 'rU') as csvfile:
		csvreader = csv.DictReader(csvfile)
		return csvreader.fieldnames

def list_of_dicts_to_csv(filepath, list_of_dicts, fieldnames = None):
	if fieldnames == None:
		fieldnames = list_of_dicts.keys()
	with open(filepath, 'w') as csvfile:
		csvwriter = csv.DictWriter(csvfile, fieldnames = fieldnames)
		csvwriter.writeheader()
		for row in list_of_dicts:
			csvwriter.writerow(row)