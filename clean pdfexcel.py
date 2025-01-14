#=================================================不好使=======================================
# import pandas as pd
# from datetime import datetime
# # 读取Excel文件
# df = pd.read_excel('D:/AA econ/research track/articles/goolsbee test/goolsbeev1.1.xlsx')
#
# # 将日期和时间列转换为datetime格式并合并为一列
#
# df['Date'] = datetime.strptime(str(df['Date']), '%d%B%Y')
#
# # 将时间转换为datetime对象
# df['Time'] = datetime.strptime(str(df['Time']), '%H:%M')
#
# df['datetime'] = pd.to_datetime(df['Date'] + ' ' + df['Time'], format='%d%B%Y %H:%M')
#
# # 将datetime列格式化为'YYYY-MM-DD HH:mm:ss'
# df['datetime'] = df['datetime'].dt.strftime('%Y-%m-%d %H:%M:%S')
#
# # 打印处理后的数据
# df.to_excel('D:/AA econ/research track/articles/goolsbee test/goolsbeev1.2.xlsx', index=False)



#==========================================洗爬的时间中有乱码=================================================
# import pandas as pd
#
# # 读取原始excel文件
# df = pd.read_excel('D:/AA econ/research track/articles/goolsbee test/goolsbeev1.xlsx')
#
# # 使用正则表达式匹配第2列中的时间格式
# df['Time'] = df['Time'].str.extract(r'(\d{2}:\d{2})')
#
# # 筛选出包含特定时间格式的行
# filtered_df = df[df['Time'].notnull()]
#
# # 将筛选后的数据保存到新的excel文件
# filtered_df.to_excel('D:/AA econ/research track/articles/goolsbee test/goolsbeev1.1.xlsx', index=False)


#============================================牛逼！！！！！=========================================================
import pandas as pd
from datetime import datetime

# 读取Excel文件
df = pd.read_excel('D:/AA econ/research track/articles/goolsbee test/goolsbeev1.1.xlsx')

# 定义一个函数来转换日期格式
def convert_date(date_str):
    try:
        return datetime.strptime(date_str, '%d%B%Y').strftime('%Y-%m-%d')
    except ValueError:
        return datetime.strptime(date_str.strip(), '%d %B %Y').strftime('%Y-%m-%d')

# 应用函数转换日期格式
df['Date'] = df['Date'].apply(convert_date)

# 格式化时间列
df['Time'] = df['Time'].str.strip().apply(lambda x: x + ':00')

# 合并日期和时间列
df['datetime'] = df['Date'] + ' ' + df['Time']

# 输出结果查看
df.to_excel('D:/AA econ/research track/articles/goolsbee test/goolsbeev1.2.xlsx', index=False)