import csv
import codecs

with codecs.open('./asset/常驻人口.txt', 'r', 'utf-8-sig') as f:
    lines = f.readlines()

with open('./asset/processed_data.csv', 'w', newline='', encoding='utf-8-sig') as f:
    writer = csv.writer(f)
    for line in lines[3:-2]:
        writer.writerow(line.strip().split(','))