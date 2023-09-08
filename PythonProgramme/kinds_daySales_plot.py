'''
Author: Jonty ljt20030312@Outlook.com
Date: 2023-09-08 11:21
LastEditTime: 2023-09-08 14:50
Description: 将六个品类的日销售量通过六张图表显示
'''
import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib
matplotlib.rcParams['font.sans-serif'] = ['SimSun']     # 显示中文
matplotlib.rcParams['axes.unicode_minus'] = False

# 指定包含Excel文件的文件夹路径
folder_path = "D:\\桌面\\CUMCM\\classificationFile_sales\\sumSales_day"

# 列出文件夹中的所有文件
file_names = os.listdir(folder_path)

# 设置Seaborn样式
sns.set(style="whitegrid")

# 定义一组颜色，用于绘制不同的图表
colors = sns.color_palette("husl", len(file_names))

# 迭代处理每个文件并绘制单独的图表
for i, file_name in enumerate(file_names):
    if file_name.endswith(".xlsx"):  # 确保文件是Excel文件
        file_path = os.path.join(folder_path, file_name)
        df = pd.read_excel(file_path)

        # 创建一个新的图表
        plt.figure(figsize=(50, 18))

        # 绘制销售数据，使用指定的颜色
        plt.plot(df['销售日期'], df['销量(千克)'], linestyle='-', markersize=8, color=colors[i])

        # 设置标题、标签等
        plt.title(f'{file_name}')
        plt.xlabel('sale day')
        plt.ylabel('sale(Kg)')

        # 如果需要保存图表到文件，可以使用以下命令
        plt.savefig(f'D:\\桌面\\CUMCM\\classificationFile_sales\\sumSales_day_plot\\plot_{file_name}.png')

        # 显示图表
        #plt.show()


