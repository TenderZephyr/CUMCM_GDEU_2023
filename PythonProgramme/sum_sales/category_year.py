'''
Author: Jonty ljt20030312@Outlook.com
Date: 2023-09-08 19:50
LastEditTime: 2023-09-10 12:30
Description: 将每个分类的年销量算出
'''
import pandas as pd
import os

# 定义包含六个Excel文件的文件夹路径和新Excel文件的路径
folder_path = 'D:\\桌面\\CUMCM\\classify_sales\\sum_category_day'
output_file = 'D:\\桌面\\CUMCM\\classify_sales\\sum_year\\category_all.xlsx'

# 创建一个空的DataFrame来存储累加后的数据
result_df = pd.DataFrame(columns=['商品名', '年份', '销量'])

# 循环遍历文件夹中的每个Excel文件
for filename in os.listdir(folder_path):
    if filename.endswith('.xlsx'):  # 确保只处理Excel文件
        file_path = os.path.join(folder_path, filename)
        
        # 从文件名中提取商品名称
        product = filename.split('.')[0]
        product_name = product[13 : ]
        print(product_name)
        
        # 读取当前Excel文件的数据
        df = pd.read_excel(file_path)
        
        # 按年份对销量列进行累加
        df['年份'] = df['销售日期'].dt.year
        yearly_sales = df.groupby(['年份'])['销量(千克)'].sum().reset_index()
        
        # 添加商品名列
        yearly_sales['商品名'] = product_name
        
        # 将当前文件的结果追加到总结果DataFrame中
        result_df = pd.concat([result_df, yearly_sales], ignore_index=True)

# 将累加后的结果保存到新的Excel文件
result_df.to_excel(output_file, index=False)

print("数据已成功叠加并保存到新的Excel文件中：", output_file)
