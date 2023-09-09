'''
Author: Jonty ljt20030312@Outlook.com
Date: 2023-09-09 15:51
LastEditTime: 2023-09-09 15:57
Description: 
'''
import pandas as pd
import os

# 指定输入文件夹路径（六个Excel文件所在的文件夹）
input_folder = 'D:\\桌面\\CUMCM\\classify_cost'  # 替换为实际的输入文件夹路径

# 指定输出文件夹路径
output_folder = 'D:\\桌面\\CUMCM\\classify_cost\\averageCost_day'  # 替换为实际的输出文件夹路径

# 确保输出文件夹存在，如果不存在则创建它
os.makedirs(output_folder, exist_ok=True)

# 读取并处理每个Excel文件
for filename in os.listdir(input_folder):
    if filename.endswith('.xlsx'):
        file_path = os.path.join(input_folder, filename)
        
        # 读取Excel文件
        data = pd.read_excel(file_path)
        
        # 计算每天的平均批发价格
        daily_avg = data.groupby('日期')['批发价格(元/千克)'].mean().reset_index()
        
        # 创建输出文件的路径
        output_file = os.path.join(output_folder, f'dayAverageCost_{filename}')
        
        # 将结果保存到独立的Excel文件中
        daily_avg.to_excel(output_file, index=False)
        
print("处理完成！")
