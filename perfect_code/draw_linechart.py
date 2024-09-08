import csv
import matplotlib.pyplot as plt
plt.rcParams['font.family'] = 'SimHei'

def find_and_plot():
    with open('./asset/processed_data.csv', newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if row[0] == '浙江省':
                data = row[1:11]
                data = [float(i) for i in data]
                years = list(range(2023, 2013, -1))
                plt.plot(years, data, marker='o', linestyle='-', color='b')
                plt.xlabel('Years')
                plt.ylabel('Values')
                plt.title('Data for 浙江省 (2014-2023)')
                plt.grid(True)
                plt.show()
                break

find_and_plot()