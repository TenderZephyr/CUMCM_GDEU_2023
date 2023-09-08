'''
Author: Jonty ljt20030312@Outlook.com
Date: 2023-09-08 10:26
LastEditTime: 2023-09-08 10:51
Description: 
'''
import pandas as pd
import os

# 指定包含多个Excel文件的文件夹路径
input_folder = 'D:\\桌面\\CUMCM\\classificationFile_kinds\\all'

# 指定存放结果的文件夹的根路径
output_folder = 'D:\\桌面\\CUMCM\\classificationFile_sales\\sumSales_day'

# 获取文件夹中的所有Excel文件
excel_files = [f for f in os.listdir(input_folder) if f.endswith('.xlsx')]

# 循环处理每个Excel文件
for file_name in excel_files:
    # 构建当前文件的完整路径
    input_file_path = os.path.join(input_folder, file_name)

    # 读取当前Excel文件
    df = pd.read_excel(input_file_path)

    # 将销售日期和销量列转换为日期时间类型和浮点数
    df['销售日期'] = pd.to_datetime(df['销售日期'])
    df['销量(千克)'] = df['销量(千克)'].astype(float)

    # 根据销售日期分组并对销量进行叠加
    result_df = df.groupby(['销售日期']).agg({'销量(千克)': 'sum'}).reset_index()

    # 构建输出文件的完整路径
    output_file_path = os.path.join(output_folder, f'sumSales_day_{file_name}')

    # 保存结果到新的Excel文件
    result_df.to_excel(output_file_path, index=False)

    print(f"{file_name} 的销量叠加完成.\n")

print(f"FINISH!")
