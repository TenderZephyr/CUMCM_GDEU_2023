'''
Author: Jonty ljt20030312@Outlook.com
Date: 2023-09-07 22:59
LastEditTime: 2023-09-10 13:46
Description: 将销售数据按照品类拆分成不同的excel并且不同单品存放到不同的工作表
'''

import pandas as pd
import os

# 读取第一个Excel文件，包含单品编码、单品名称和分类名称
file1 = 'question\\附件1.xlsx'
df1 = pd.read_excel(file1)

# 读取第二个Excel文件，包含单品编码和其他信息
file2 = 'question\\附件2.xlsx'
df2 = pd.read_excel(file2)

# 获取第一个Excel文件的分类名称列表
categories = df1['分类名称'].unique()

# 指定存放结果的文件夹路径
output_folder = 'classify_category\\category_product_sheet'

# 确保输出文件夹存在，如果不存在则创建它
os.makedirs(output_folder, exist_ok=True)

# 遍历每个分类，将第二个Excel文件的数据按照分类写入不同的Excel文件
for category in categories:
    # 选择属于当前分类的数据
    category_data = df1[df1['分类名称'] == category]
    
    # 创建一个新的Excel写入对象
    writer = pd.ExcelWriter(os.path.join(output_folder, f'{category}.xlsx'), engine='xlsxwriter')
    
    # 遍历当前分类的每个单品
    for index, row in category_data.iterrows():
        # 获取单品编码和单品名称
        item_code = row['单品编码']
        item_name = row['单品名称']
        
        # 选择第二个Excel文件中与当前单品编码匹配的数据
        item_data = df2[df2['单品编码'] == item_code]
        
        # 将数据写入当前工作表，工作表以单品名称命名
        item_data.to_excel(writer, sheet_name=item_name, index=False)
    
    # 保存当前分类的结果文件
    writer._save()
    writer.close()

print("分类完成，结果存储在指定文件夹中。")
