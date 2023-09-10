'''
Author: Jonty ljt20030312@Outlook.com
Date: 2023-09-08 10:18
LastEditTime: 2023-09-10 11:44
Description: 将销售数据按品类拆分成不同的excel文件
'''
import pandas as pd
import os

# 读取第一个Excel文件，包含单品编码、单品名称和分类名称
inputFile1 = 'D:\\桌面\\CUMCM\\question\\附件1.xlsx'
df1 = pd.read_excel(inputFile1)

# 读取第二个Excel文件，包含单品编码和其他信息
inputFile2 = 'D:\\桌面\\CUMCM\\question\\附件2.xlsx'
df2 = pd.read_excel(inputFile2)

# 获取第一个Excel文件的分类名称列表
categories = df1['分类名称'].unique()

# 指定存放结果的文件夹路径
output_folder = 'D:\\桌面\\CUMCM\\classify_category\\all_in_one_sheet'

# 确保输出文件夹存在，如果不存在则创建它
os.makedirs(output_folder, exist_ok=True)

# 遍历每个分类，将第二个Excel文件的数据按照分类写入不同的Excel文件
for category in categories:
    # 选择属于当前分类的数据
    category_data = df1[df1['分类名称'] == category]
    
    # 获取当前分类的所有单品编码
    item_codes = category_data['单品编码'].tolist()
    
    # 选择第二个Excel文件中与当前分类的单品编码匹配的数据
    filtered_data = df2[df2['单品编码'].isin(item_codes)]
    
    # 创建一个新的Excel写入对象
    writer = pd.ExcelWriter(os.path.join(output_folder, f'{category}.xlsx'), engine='xlsxwriter')
    
    # 将数据写入当前工作表
    filtered_data.to_excel(writer, index=False)
    
    # 保存当前分类的结果文件
    writer._save()
    writer.close()

print("分类完成，结果存储在指定文件夹中。")
