#========================================download_hist_data===========================================
# from histdata import download_hist_data as dl
# from histdata.api import Platform as P, TimeFrame as TF
# dl(year='2024', month=1, pair='spxusd', platform=P.META_TRADER, time_frame=TF.ONE_MINUTE)

##========================================merge_csv_files=============================================
# import os
# import pandas as pd
#
# def merge_csv_files(folder_path, output_file):
#     all_files = [file for file in os.listdir(folder_path) if file.endswith('.csv')]
#     combined_df = pd.concat([pd.read_csv(os.path.join(folder_path, file), header=None) for file in all_files])
#     combined_df.columns = ['Date', 'time', 'OPEN', 'HIGH ', 'LOW', 'CLOSE', 'Volume']
#     combined_df.to_csv(output_file, index=False)
# # # 使用示例
# merge_csv_files('D:/AA econ/research track/data/sp500-2', 'D:/AA econ/research track/data/intraday data2/sp500_1011-247.csv')

#####=====================================print first 5 rows======================================
import pandas as pd
df = pd.read_csv('D:/AA econ/research track/data/intraday data2/sp500_1011-247-3.csv')
first_5_rows = df.tail(107485)
#
print(first_5_rows)

# #========================emerge 'Date' and 'time' to 'Datetime'===============================
# import pandas as pd
#
# # 读取CSV文件
# df = pd.read_csv('D:/AA econ/research track/data/intraday data2/sp500_1011-247.csv')
#
# # 转换日期和时间格式
# df['Date'] = pd.to_datetime(df['Date'], format='%Y.%m.%d')
# df['time'] = pd.to_datetime(df['time'], format='%H:%M').dt.time
#
# # 合并日期和时间列
# df['Datetime'] = df.apply(lambda row: pd.Timestamp.combine(row['Date'], row['time']), axis=1)
#
# # 将日期时间格式化为所需的格式
# df['Datetime'] = df['Datetime'].dt.strftime('%Y-%m-%d %H:%M:%S')
# # 删除原始的日期和时间列
# df.drop(['Date', 'time'], axis=1, inplace=True)
#
# # 将日期时间设置为第一列
# cols = ['Datetime'] + [col for col in df.columns if col != 'Datetime']
# df = df[cols]
#
# # 输出到新的CSV文件
# df.to_csv('D:/AA econ/research track/data/intraday data2/sp500_1011-247-2.csv', index=False)

# #=======================================时区转换================================================
# import pandas as pd
# import pytz
#
# # 读取CSV文件
# df = pd.read_csv('D:/AA econ/research track/data/intraday data2/sp500_1011-247-2.csv')
#
# # 确保Datetime列是datetime类型
# df['Datetime'] = pd.to_datetime(df['Datetime'])
#
# # 设置时区为Eastern Standard Time
# eastern = pytz.timezone('US/Eastern')
# df['Datetime'] = df['Datetime'].dt.tz_localize(eastern, ambiguous='infer')
#
# # 输出查看结果
# df.to_csv('D:/AA econ/research track/data/intraday data2/sp500_1011-247-3.csv', index=False)