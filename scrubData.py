from csv_tools import csv_read_to_list_of_dicts, csv_get_column_headers, list_of_dicts_to_csv

# Load known values curated by Ellen
known_values = csv_read_to_list_of_dicts("Retentiontime_mz_peptides.csv")
name_sequence_dict = dict([(row['name'], row['sequence']) for row in known_values])

# Load desired columns from spreadsheet
test_data = csv_read_to_list_of_dicts("test_nick.csv")

found_dict = dict([(row["name"],[]) for row in known_values])

for idx, row in enumerate(test_data):
	for known_row in known_values:
		if known_row["time_low"] <= row["Time"] and row["Time"] <= known_row["time_high"] and known_row["mz_low"] <= row["Obs m/z"] and row["Obs m/z"] <= known_row["mz_high"]:
			found_dict[known_row["name"]].append(idx)

rows_to_write = []
for peptide, ids in found_dict.iteritems():
	for idx in ids:
		test_data[idx]["Reference"] = peptide
		test_data[idx]["Peptide"] = name_sequence_dict[peptide]
		rows_to_write.append(test_data[idx])

list_of_dicts_to_csv("test.csv", rows_to_write, csv_get_column_headers("test_nick.csv"))