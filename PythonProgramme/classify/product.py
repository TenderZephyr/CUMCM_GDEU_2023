'''
Author: Jonty ljt20030312@Outlook.com
Date: 2023-09-07 21:59
LastEditTime: 2023-09-10 11:32
Description: 将销量数据按照单品拆分成不同的excel
'''

import pandas as pd
import os

# 指定原始.xlsx文件的路径（包括文件名）
input_file = 'D:\\桌面\\CUMCM\\question\\附件2.xlsx'

# 读取原始.xlsx文件
df = pd.read_excel(input_file)

# 根据要分类的列名称，这里假设为"分类列名"
column_to_classify = '单品编码'

# 获取分类的唯一值
categories = df[column_to_classify].unique()

# 指定存放分类结果的文件夹路径
output_folder = 'D:\\桌面\\CUMCM\\classify_product'

# 确保输出文件夹存在，如果不存在则创建它
os.makedirs(output_folder, exist_ok=True)

# 遍历每个分类，将数据存储到不同的.xlsx文件
for category in categories:
    # 选择属于当前分类的数据
    category_data = df[df[column_to_classify] == category]
    
    # 构建输出文件名
    output_file = os.path.join(output_folder, f'{category}.xlsx')
    
    # 将数据写入新的.xlsx文件
    category_data.to_excel(output_file, index=False)

print("分类完成，结果存储在指定文件夹中。")
