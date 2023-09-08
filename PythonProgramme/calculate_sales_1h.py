'''
Author: Jonty ljt20030312@Outlook.com
Date: 2023-09-08 07:55
LastEditTime: 2023-09-08 09:07
Description: 对同一个单品在一个小时内的销量进行合并
'''
import pandas as pd

# 读取原始Excel文件
inputFile = 'D:\\桌面\\CUMCM\\topic\\附件2.xlsx'
df = pd.read_excel(inputFile)

# 提取销售时间的小时作为新的列
df['销售小时'] = pd.to_datetime(df['扫码销售时间']).dt.hour

# 将数据按销售日期、销售小时、单品编码分组，并计算销量的总和
result_df = df.groupby(['销售日期', '销售小时', '单品编码'])['销量(千克)'].sum().reset_index()

# 创建一个新的Excel文件来存储结果
outputFile = 'D:\桌面\CUMCM\sales\\oneHour_sumSales.xlsx'
with pd.ExcelWriter(outputFile, engine='xlsxwriter') as writer:
    result_df.to_excel(writer, sheet_name='一小时总销量结果', index=False)
