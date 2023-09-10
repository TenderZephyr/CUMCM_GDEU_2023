'''
Author: Jonty ljt20030312@Outlook.com
Date: 2023-09-09 21:48
LastEditTime: 2023-09-10 13:48
Description: 
'''
import os
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import seaborn as sns

#plt.rcParams['font.sans-serif'] = ['SimHei']  # 黑体
plt.rcParams['axes.unicode_minus'] = False    # 解决无法显示符号的问题
 # 解决Seaborn中文显示问题
sns.set(font = 'SimHei', style = "darkgrid", font_scale = 1.6)  

# 指定包含Excel文件的文件夹路径
folder_path = "classify_sales\\sum_category_month"

# 列出文件夹中的所有文件
file_names = os.listdir(folder_path)

# 创建一个新的图表
plt.figure(figsize=(25, 12))

# 定义一组颜色，用于绘制不同的曲线
colors = sns.color_palette("husl", len(file_names))

# 迭代处理每个文件并绘制曲线
for i, file_name in enumerate(file_names):
    if file_name.endswith(".xlsx"):  # 确保文件是Excel文件
        file_path = os.path.join(folder_path, file_name)
        df = pd.read_excel(file_path)
        # 绘制销售数据，使用指定的颜色
        plt.plot(df['月份'], df['销量(千克)'], linestyle='-', markersize=8, label=f'{file_name[ : -20]}', color=colors[i])
        
        plt.gca().xaxis.set_major_locator(ticker.MultipleLocator(6))
        
# 设置标题、标签等
plt.title('全品类月销售数据')
plt.xlabel('销售日期')
plt.ylabel('销量(千克)')

# 添加图例以区分不同的文件
plt.legend()

# 如果需要保存图表到文件，可以使用以下命令
plt.savefig(f'plot\\month_sales_all.png')

# 显示图表
#plt.show()