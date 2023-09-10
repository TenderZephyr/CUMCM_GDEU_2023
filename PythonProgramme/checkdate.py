'''
Author: Jonty ljt20030312@Outlook.com
Date: 2023-09-08 17:26
LastEditTime: 2023-09-08 17:26
Description: 检查是否有跳过的天数
'''
import pandas as pd

# 读取Excel文件
excel_file = 'D:\\桌面\\CUMCM\\classify_sales\\sum_category_day\\sum_category_day_花菜类all.xlsx'  # 请将文件路径替换为你的Excel文件路径
df = pd.read_excel(excel_file)

# 将销售日期列转换为日期时间类型
df['销售日期'] = pd.to_datetime(df['销售日期'])

# 对销售日期列进行排序
df = df.sort_values(by='销售日期')

# 计算销售日期之间的差值
date_diff = df['销售日期'].diff()

# 找到中断的销售日期
interrupted_dates = df[date_diff > pd.Timedelta(days=1)]['销售日期']

# 输出中断的销售日期
if not interrupted_dates.empty:
    print("中断的销售日期:")
    for date in interrupted_dates:
        print(date.strftime('%Y-%m-%d'))
else:
    print("没有中断的销售日期")
