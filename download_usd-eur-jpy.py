# sentence = "FED COMMUNICATION ON FINANCIAL STABILITY CONCERNS AND MONETARY POLICY DECISIONS: REVELATIONS FROM SPEECHES"
# lowercase_sentence = sentence.lower()
# print(lowercase_sentence)

# #========================================download_hist_data===========================================
# from histdata import download_hist_data as dl
# from histdata.api import Platform as P, TimeFrame as TF
# dl(year='2024', month=1, pair='spxusd', platform=P.META_TRADER, time_frame=TF.ONE_MINUTE)

# # #========================================merge_csv_files=============================================
# import os
# import pandas as pd
#
# def merge_csv_files(folder_path, output_file):
#     all_files = [file for file in os.listdir(folder_path) if file.endswith('.csv')]
#     combined_df = pd.concat([pd.read_csv(os.path.join(folder_path, file)) for file in all_files])
#     combined_df.columns = ['Datetime', 'OPEN', 'HIGH ', 'LOW', 'CLOSE', 'Volume']
#     combined_df.to_csv(output_file, index=False)
#     # # 使用示例
# merge_csv_files('D:/AA econ/research track/data/EURUSD', 'D:/AA econ/research track/data/intraday data2/EURUSD_1101-2407.csv')

# # # # ####=====================================print first 5 rows======================================
import pandas as pd
df = pd.read_csv('D:/AA econ/research track/data/intraday data2/EURUSD_1101-2407-3.csv')
#first_5_rows = df.tail(107485)#冬令时转夏令时
first_5_rows = df.head(191414)
#
print(first_5_rows)

# # #========================emerge 'Date' and 'time' to 'Datetime'===============================
# import pandas as pd
#
# # 读取CSV文件
# df = pd.read_csv('D:/AA econ/research track/data/intraday data2/USDJPY_1101-2407.csv')
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
# df.to_csv('D:/AA econ/research track/data/intraday data2/USDJPY_1101-2407-2.csv', index=False)

# #=======================================时区转换================================================
import pandas as pd
import pytz

# 读取CSV文件
df = pd.read_csv('D:/AA econ/research track/data/intraday data2/EURUSD_1101-2407.csv')

# 确保Datetime列是datetime类型
df['Datetime'] = pd.to_datetime(df['Datetime'])

# 设置时区为Eastern Standard Time
eastern = pytz.timezone('US/Eastern')
df['Datetime'] = df['Datetime'].dt.tz_localize(eastern, ambiguous='infer')



# 输出查看结果
df.to_csv('D:/AA econ/research track/data/intraday data2/EURUSD_1101-2407-3.csv', index=False)

# #===============================all xlsx to csv=============================================
# import pandas as pd
# import os
#
# # 设置文件夹路径
# folder_path = 'D:/AA econ/research track/data/EURUSD/'
#
# # 遍历文件夹中的所有文件
# for file_name in os.listdir(folder_path):
#     if file_name.endswith('.xlsx'):
#         # 构建完整的文件路径
#         file_path = os.path.join(folder_path, file_name)
#         # 读取Excel文件
#         df = pd.read_excel(file_path, header=None)
#         decimals = {1: 6, 2: 6, 3: 6, 4: 6, 5: 0}
#         for col, dec in decimals.items():
#             df.iloc[:, col] = df.iloc[:, col].round(dec)
#         # 构建CSV文件的路径
#         csv_file_path = os.path.join(folder_path, file_name.replace('.xlsx', '.csv'))
#         # 将DataFrame保存为CSV文件
#         df.to_csv(csv_file_path, index=False)
#         print(f'转换文件：{file_path} 到 {csv_file_path}')