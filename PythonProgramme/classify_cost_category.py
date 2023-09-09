'''
Author: Jonty ljt20030312@Outlook.com
Date: 2023-09-09 15:31
LastEditTime: 2023-09-09 15:51
Description: 将附加3按照分类拆分
'''
import os
import pandas as pd

# 读取文件1
file1 = pd.read_excel('D:\\桌面\\CUMCM\\topic\\附件1.xlsx')  # 替换为文件1的实际路径

# 读取文件2
file2 = pd.read_excel('D:\\桌面\\CUMCM\\topic\\附件3.xlsx')  # 替换为文件2的实际路径

# 使用文件1的单品编码和分类名称合并文件2
merged_data = file2.merge(file1, on='单品编码')

# 分组并保存不同分类的数据到不同的Excel文件夹
grouped = merged_data.groupby('分类名称')

# 指定输出文件夹路径
output_folder = 'D:\\桌面\\CUMCM\\classify_cost'  # 替换为实际的输出文件夹路径

# 确保输出文件夹存在，如果不存在则创建它
os.makedirs(output_folder, exist_ok=True)

for group_name, group_data in grouped:
    output_filename = os.path.join(output_folder, f'{group_name}_cost.xlsx')
    group_data.drop(columns=['分类名称']).to_excel(output_filename, index=False)

print("处理完成！")

