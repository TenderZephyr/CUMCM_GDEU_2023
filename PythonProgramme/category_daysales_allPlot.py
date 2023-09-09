'''
Author: Jonty ljt20030312@Outlook.com
Date: 2023-09-09 16:35
LastEditTime: 2023-09-09 21:19
Description: 绘制所有品类的日销售折线图
'''
import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#plt.rcParams['font.sans-serif'] = ['SimHei']  # 黑体
plt.rcParams['axes.unicode_minus'] = False    # 解决无法显示符号的问题
 # 解决Seaborn中文显示问题
sns.set(font = 'SimHei', style = "darkgrid", font_scale = 5)  

# 指定包含Excel文件的文件夹路径
folder_path = "D:\\桌面\\CUMCM\\classificationFile_sales\\sumSales_day"

# 列出文件夹中的所有文件
file_names = os.listdir(folder_path)

# 设置Seaborn样式
sns.set(style="whitegrid")

# 创建一个新的图表
plt.figure(figsize=(15, 12))

# 定义一组颜色，用于绘制不同的曲线
colors = sns.color_palette("husl", len(file_names))

# 迭代处理每个文件并绘制曲线
for i, file_name in enumerate(file_names):
    if file_name.endswith(".xlsx"):  # 确保文件是Excel文件
        file_path = os.path.join(folder_path, file_name)
        df = pd.read_excel(file_path)
        
        #图例
        k = file_name[8 : -8]
        label_name = k[5 : ]
        
        # 绘制销售数据，使用指定的颜色
        plt.plot(df['销售日期'], df['销量(千克)'], linestyle='-', markersize=8, label=f'{label_name}', color=colors[i])

# 设置标题、标签等
plt.title('销售数据')
plt.xlabel('销售日期')
plt.ylabel('销量(千克)')

# 添加图例以区分不同的文件
plt.legend()

# 如果需要保存图表到文件，可以使用以下命令
#plt.savefig(f'D:\桌面\CUMCM\classificationFile_sales\sumSales_day_plot\\daySalesPlot_all.png')

# 显示图表
plt.show()