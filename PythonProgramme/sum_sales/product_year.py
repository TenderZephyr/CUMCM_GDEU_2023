'''
Author: Jonty ljt20030312@Outlook.com
Date: 2023-09-08 20:18
LastEditTime: 2023-09-10 12:31
Description: 将附件2的每个单品计算年销量并且按分类分excel文件
'''
import pandas as pd
import os

# 定义第一个Excel文件的路径和第二个Excel文件的路径
file1_path = 'question\\附件1.xlsx'
file2_path = 'question\\附件2.xlsx'
output_folder = 'classify_sales\\sum_year'

# 读取第一个Excel文件以建立单品编码到单品名称和分类名称的映射
df1 = pd.read_excel(file1_path)
product_mapping = df1[['单品编码', '单品名称', '分类名称']]

# 读取第二个Excel文件
df2 = pd.read_excel(file2_path)

# 将销售日期列转换为年份
df2['年份'] = df2['销售日期'].dt.year

# 合并第二个Excel文件和映射关系文件以获取单品名称和分类名称
merged_df = pd.merge(df2, product_mapping, on='单品编码', how='left')

# 按分类名称、年份和单品名称对销量列进行叠加
result_df = merged_df.groupby(['单品名称', '分类名称','年份'])['销量(千克)'].sum().reset_index()

# 按分类名称分别保存结果到不同的Excel文件
for category_name, category_data in result_df.groupby('分类名称'):
    category_output_file = os.path.join(output_folder, f'{category_name}.xlsx')
    category_data.to_excel(category_output_file, index=False)

print("FINISH!!!")