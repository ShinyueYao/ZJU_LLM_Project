import csv
import sys

file_in = open('./asset/processed_data.csv', 'r', encoding='utf-8-sig')
file_out = open('./asset/complete_data.csv', 'w', newline='', encoding='utf-8-sig')
reader = csv.reader(file_in)
writer = csv.writer(file_out)

rows = list(reader)[1:33]  # skip header and read rows 2 to 32

for row in rows:
    data = [float(x) for x in row[1:12]]  # convert columns 2 to 11 to float
    avg = sum(data) / len(data)
    max_val = max(data)
    min_val = min(data)
    row.extend([avg, max_val, min_val])  # add avg, max, min to the row

    writer.writerow(row)

file_in.close()
file_out.close()