'''
Author: Jonty ljt20030312@Outlook.com
Date: 2023-09-09 13:25
LastEditTime: 2023-09-09 13:33
Description: 
'''
import pandas as pd
from glob import glob
import os
import xlsxwriter

# 获取所有 Excel 文件的文件名
excel_files = glob('D:\\桌面\\CUMCM\\classificationFile_sales\\sumSales_day\\*.xlsx')  # 替换为你的文件路径

# 创建一个目录来存储新的 Excel 文件
output_directory = 'D:\\桌面\CUMCM\\classificationFile_sales\\sumsales_month'  # 替换为你想要保存文件的文件夹路径
os.makedirs(output_directory, exist_ok=True)

# 读取每个 Excel 文件并累计销量并保存到不同的文件
for file in excel_files:
    df = pd.read_excel(file)
    df['销售日期'] = pd.to_datetime(df['销售日期'])  # 将销售日期列转换为日期时间格式
    df['月份'] = df['销售日期'].dt.to_period('M')  # 创建一个新的列，表示销售日期的月份
    monthly_sales = df.groupby('月份')['销量(千克)'].sum().reset_index()  # 按月份累计销量(千克)

    # 获取输出文件名
    k = os.path.splitext(os.path.basename(file))[0]
    file = k[3 : -3]
    file_name = file[10 : ]
    
    output_file = os.path.join(output_directory, f'{file_name}_sumSales_monty.xlsx')

    # 创建一个新的 Excel 文件并将结果保存到其中
    with pd.ExcelWriter(output_file, engine='xlsxwriter') as writer:
        monthly_sales.to_excel(writer, sheet_name='月度销量', index=False)

    print(f'结果已保存到 {output_file}')

