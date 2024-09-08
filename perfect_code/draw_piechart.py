import csv
import matplotlib.pyplot as plt
plt.rcParams['font.family'] = 'SimHei'

# 读取文件并处理数据
with open('./asset/complete_data.csv', 'r', encoding='utf-8-sig') as f:
    reader = csv.reader(f)
    # header = next(reader)  # 跳过标题行
    data_dict = {}  # 保存数据的字典
    for row in reader:
        label = row[0]
        value = float(row[11])  # 读取第12列数据并转换为浮点数
        if label not in data_dict:
            data_dict[label] = []
        data_dict[label].append(value)

# 画图
labels = data_dict.keys()
values = [sum(data_dict[label]) for label in labels]
plt.pie(values, labels=labels, autopct='%.1f%%')

# 保存图像
plt.savefig('./asset/pie_chart.jpg')
plt.show()