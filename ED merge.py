# #================ED2====================
# import pandas as pd
# import os
#
# # 文件夹路径
# folder_path = 'D:/AA econ/research track/data/futures/3-Month SOFR Futures/'
#
# # 创建一个空的列表来存储数据框
# dataframes = []
# times = ['2017-03-15 10:00:00+00:00', '2017-06-19 10:00:00+00:00', '2017-09-18 10:00:00+00:00',
#          '2017-12-18 11:00:00+00:00', '2018-03-19 11:00:00+00:00', '2018-06-18 10:00:00+00:00',
#          '2018-09-17 10:00:00+00:00', '2018-12-17 11:00:00+00:00', '2019-03-18 11:00:00+00:00',
#          '2019-06-17 10:00:00+00:00', '2019-09-16 10:00:00+00:00', '2019-12-16 11:00:00+00:00',
#          '2020-03-16 11:00:00+00:00', '2020-06-15 10:00:00+00:00', '2020-09-14 10:00:00+00:00',
#          '2020-12-14 11:00:00+00:00', '2021-03-15 11:00:00+00:00', '2021-06-14 10:00:00+00:00',
#          '2021-09-13 10:00:00+00:00', '2021-12-13 11:00:00+00:00', '2022-03-14 11:00:00+00:00',
#          '2022-06-13 10:00:00+00:00', '2022-09-16 10:00:00+00:00', '2022-12-19 11:00:00+00:00']
# # start_time = pd.to_datetime('2017-03-15 10:00:00+00:00')
# # end_time = pd.to_datetime('2017-06-19 10:00:00+00:00')
# j, k = 0, 1
#
# for i in ['7','8','9','0','1','2']:  # 从1到9
#     for prefix in ['GEH', 'GEM', 'GEU', 'GEZ']:
#         if i == '7' and prefix in ['GEH','GEM']: #skip the part overlap with GE
#             continue
#         print(i)
#         file_name = f'{prefix}{i}.csv'  # 生成文件名
#         file_path = os.path.join(folder_path, file_name)  # 生成完整路径
#
#         # 检查文件是否存在
#         if os.path.exists(file_path):
#             df = pd.read_csv(file_path)  # 读取CSV文件
#             df['ts_event'] = pd.to_datetime(df['ts_event'])
#             start_time, end_time = times[j], times[k]
#
#             filtered_df = df[(df['ts_event'] >= start_time) & (df['ts_event'] <= end_time)]
#             dataframes.append(filtered_df)
#             # start_time = end_time
#             # end_time = end_time + pd.DateOffset(days=91)
#             j, k =j+1, k+1
#             print(end_time)
#
# times2 = ['2022-09-16 10:00:00+00:00', '2022-12-20 21:00:00+00:00', '2023-03-14 21:00:00+00:00', '2023-06-20 21:00:00+00:00',
#           '2023-09-19 21:00:00+00:00', '2023-12-19 21:00:00+00:00', '2024-03-19 21:00:00+00:00',
#           '2024-06-18 21:00:00+00:00', '2024-08-16 21:00:00+00:00']
# j, k = 0, 1
#
# for i in ['2','3','4']:
#     for prefix in ['SR3H', 'SR3M', 'SR3U', 'SR3Z']:
#         if i == '2' and prefix in ['SR3H', 'SR3M', 'SR3U']: #skip the part overlap with GE
#             continue
#         if i == '4' and prefix in ['SR3Z']:
#             continue
#         print(i)
#         file_name = f'{prefix}{i}.csv'  # 生成文件名
#         file_path = os.path.join(folder_path, file_name)  # 生成完整路径
#
#         # 检查文件是否存在
#         if os.path.exists(file_path):
#             df = pd.read_csv(file_path)  # 读取CSV文件
#             df['ts_event'] = pd.to_datetime(df['ts_event'])
#             start_time, end_time = times2[j], times2[k]
#             filtered_df = df[(df['ts_event'] >= start_time) & (df['ts_event'] <= end_time)]
#             dataframes.append(filtered_df)
#             # start_time = end_time
#             # end_time = end_time + pd.DateOffset(days=91)
#             j, k = j + 1, k + 1
#             print(end_time)
#
# combined_df = pd.concat(dataframes, ignore_index=True)
# combined_df.to_csv('D:/AA econ/research track/data/futures/3-Month SOFR Futures/ED2.csv', index=False,encoding = 'utf-8-sig')


# ##### ================ED3====================
# import pandas as pd
# import os
#
# # 文件夹路径
# folder_path = '/Users/siyuanfang/Downloads/AA econ/research track/data/futures/3-Month SOFR Futures/'
#
# # 创建一个空的列表来存储数据框
# dataframes = []
# times = ['2017-03-15 10:00:00+00:00', '2017-06-19 10:00:00+00:00', '2017-09-18 10:00:00+00:00',
#          '2017-12-18 11:00:00+00:00', '2018-03-19 11:00:00+00:00', '2018-06-18 10:00:00+00:00',
#          '2018-09-17 10:00:00+00:00', '2018-12-17 11:00:00+00:00', '2019-03-18 11:00:00+00:00',
#          '2019-06-17 10:00:00+00:00', '2019-09-16 10:00:00+00:00', '2019-12-16 11:00:00+00:00',
#          '2020-03-16 11:00:00+00:00', '2020-06-15 10:00:00+00:00', '2020-09-14 10:00:00+00:00',
#          '2020-12-14 11:00:00+00:00', '2021-03-15 11:00:00+00:00', '2021-06-14 10:00:00+00:00',
#          '2021-09-13 10:00:00+00:00', '2021-12-13 11:00:00+00:00', '2022-03-14 11:00:00+00:00',
#          '2022-06-13 10:00:00+00:00', '2022-09-16 10:00:00+00:00', '2022-12-19 11:00:00+00:00']
# # start_time = pd.to_datetime('2017-03-15 10:00:00+00:00')
# # end_time = pd.to_datetime('2017-06-19 10:00:00+00:00')
# j, k = 0, 1
#
# for i in ['7','8','9','0','1','2']:  # 从1到9
#     for prefix in ['GEH', 'GEM', 'GEU', 'GEZ']:
#         if i == '7' and prefix in ['GEH','GEM', 'GEU']: #skip the part overlap with GE
#             continue
#         print(i)
#         file_name = f'{prefix}{i}.csv'  # 生成文件名
#         file_path = os.path.join(folder_path, file_name)  # 生成完整路径
#
#         # 检查文件是否存在
#         if os.path.exists(file_path):
#             df = pd.read_csv(file_path)  # 读取CSV文件
#             df['ts_event'] = pd.to_datetime(df['ts_event'])
#             start_time, end_time = times[j], times[k]
#
#             filtered_df = df[(df['ts_event'] >= start_time) & (df['ts_event'] <= end_time)]
#             dataframes.append(filtered_df)
#             # start_time = end_time
#             # end_time = end_time + pd.DateOffset(days=91)
#             j, k =j+1, k+1
#             print(end_time)
#
# times2 = ['2022-06-13 10:00:00+00:00', '2022-09-16 10:00:00+00:00', '2022-12-20 21:00:00+00:00',
#           '2023-03-14 21:00:00+00:00', '2023-06-20 21:00:00+00:00',
#           '2023-09-19 21:00:00+00:00', '2023-12-19 21:00:00+00:00', '2024-03-19 21:00:00+00:00',
#           '2024-06-18 21:00:00+00:00', '2024-08-16 21:00:00+00:00']
# j, k = 0, 1
#
# for i in ['2','3','4']:
#     for prefix in ['SR3H', 'SR3M', 'SR3U', 'SR3Z']:
#         if i == '2' and prefix in ['SR3H', 'SR3M', 'SR3U']: #skip the part overlap with GE
#             continue
#
#         print(i)
#         file_name = f'{prefix}{i}.csv'  # 生成文件名
#         file_path = os.path.join(folder_path, file_name)  # 生成完整路径
#
#         # 检查文件是否存在
#         if os.path.exists(file_path):
#             df = pd.read_csv(file_path)  # 读取CSV文件
#             df['ts_event'] = pd.to_datetime(df['ts_event'])
#             start_time, end_time = times2[j], times2[k]
#             filtered_df = df[(df['ts_event'] >= start_time) & (df['ts_event'] <= end_time)]
#             dataframes.append(filtered_df)
#             # start_time = end_time
#             # end_time = end_time + pd.DateOffset(days=91)
#             j, k = j + 1, k + 1
#             print(end_time)
#
# combined_df = pd.concat(dataframes, ignore_index=True)
# combined_df.to_csv('/Users/siyuanfang/Downloads/AA econ/research track/data/futures/3-Month SOFR Futures/ED3.csv', index=False)



#
# ######================ED4====================
# import pandas as pd
# import os
#
# # 文件夹路径
# folder_path = '/Users/siyuanfang/Downloads/AA econ/research track/data/futures/3-Month SOFR Futures/'
#
# # 创建一个空的列表来存储数据框
# dataframes = []
# times = ['2017-03-15 10:00:00+00:00', '2017-06-19 10:00:00+00:00', '2017-09-18 10:00:00+00:00',
#          '2017-12-18 11:00:00+00:00', '2018-03-19 11:00:00+00:00', '2018-06-18 10:00:00+00:00',
#          '2018-09-17 10:00:00+00:00', '2018-12-17 11:00:00+00:00', '2019-03-18 11:00:00+00:00',
#          '2019-06-17 10:00:00+00:00', '2019-09-16 10:00:00+00:00', '2019-12-16 11:00:00+00:00',
#          '2020-03-16 11:00:00+00:00', '2020-06-15 10:00:00+00:00', '2020-09-14 10:00:00+00:00',
#          '2020-12-14 11:00:00+00:00', '2021-03-15 11:00:00+00:00', '2021-06-14 10:00:00+00:00',
#          '2021-09-13 10:00:00+00:00', '2021-12-13 11:00:00+00:00', '2022-03-14 11:00:00+00:00',
#          '2022-06-13 10:00:00+00:00', '2022-09-16 10:00:00+00:00', '2022-12-19 11:00:00+00:00']
# # start_time = pd.to_datetime('2017-03-15 10:00:00+00:00')
# # end_time = pd.to_datetime('2017-06-19 10:00:00+00:00')
# j, k = 0, 1
#
# for i in ['7','8','9','0','1','2']:  # 从1到9
#     for prefix in ['GEH', 'GEM', 'GEU', 'GEZ']:
#         if i == '7' and prefix in ['GEH', 'GEM', 'GEU', 'GEZ']: #skip the part overlap with GE
#             continue
#         print(i)
#         file_name = f'{prefix}{i}.csv'  # 生成文件名
#         file_path = os.path.join(folder_path, file_name)  # 生成完整路径
#
#         # 检查文件是否存在
#         if os.path.exists(file_path):
#             df = pd.read_csv(file_path)  # 读取CSV文件
#             df['ts_event'] = pd.to_datetime(df['ts_event'])
#             start_time, end_time = times[j], times[k]
#
#             filtered_df = df[(df['ts_event'] >= start_time) & (df['ts_event'] <= end_time)]
#             dataframes.append(filtered_df)
#             # start_time = end_time
#             # end_time = end_time + pd.DateOffset(days=91)
#             j, k =j+1, k+1
#             print(end_time)
#
# times2 = ['2022-03-14 11:00:00+00:00','2022-06-13 10:00:00+00:00', '2022-09-16 10:00:00+00:00', '2022-12-20 21:00:00+00:00',
#           '2023-03-14 21:00:00+00:00', '2023-06-20 21:00:00+00:00',
#           '2023-09-19 21:00:00+00:00', '2023-12-19 21:00:00+00:00', '2024-03-19 21:00:00+00:00',
#           '2024-06-18 21:00:00+00:00', '2024-08-16 21:00:00+00:00']
# j, k = 0, 1
#
# for i in ['2', '3','4','5']:
#     for prefix in ['SR3H', 'SR3M', 'SR3U', 'SR3Z']:
#         if i == '3' and prefix in ['SR3H', 'SR3M', 'SR3U']: #skip the part overlap with GE
#             continue
#         if i == '5' and prefix in ['SR3M', 'SR3U', 'SR3Z']: #skip the part overlap with GE
#             continue
#         print(i)
#         file_name = f'{prefix}{i}.csv'  # 生成文件名
#         file_path = os.path.join(folder_path, file_name)  # 生成完整路径
#
#         # 检查文件是否存在
#         if os.path.exists(file_path):
#             df = pd.read_csv(file_path)  # 读取CSV文件
#             df['ts_event'] = pd.to_datetime(df['ts_event'])
#             start_time, end_time = times2[j], times2[k]
#             filtered_df = df[(df['ts_event'] >= start_time) & (df['ts_event'] <= end_time)]
#             dataframes.append(filtered_df)
#             # start_time = end_time
#             # end_time = end_time + pd.DateOffset(days=91)
#             j, k = j + 1, k + 1
#             print(end_time)
#
# combined_df = pd.concat(dataframes, ignore_index=True)
# combined_df.to_csv('/Users/siyuanfang/Downloads/AA econ/research track/data/futures/3-Month SOFR Futures/ED4.csv', index=False)

# #================SP500====================
# import pandas as pd
# import os
#
# # 文件夹路径
# folder_path = '/Users/siyuanfang/Downloads/AA econ/research track/data/futures/E-mini SP 500 Futures/'
#
# # 创建一个空的列表来存储数据框
# dataframes = []
# times = ['2017-12-18 11:00:00+00:00', '2018-03-16 11:00:00+00:00', '2018-06-15 10:00:00+00:00',
#          '2018-09-21 10:00:00+00:00', '2018-12-21 11:00:00+00:00', '2019-03-15 11:00:00+00:00',
#          '2019-06-21 10:00:00+00:00', '2019-09-20 10:00:00+00:00', '2019-12-20 11:00:00+00:00',
#          '2020-03-20 11:00:00+00:00', '2020-06-19 10:00:00+00:00', '2020-09-18 10:00:00+00:00',
#          '2020-12-18 11:00:00+00:00', '2021-03-19 11:00:00+00:00', '2021-06-18 10:00:00+00:00',
#          '2021-09-17 10:00:00+00:00', '2021-12-17 11:00:00+00:00', '2022-03-18 11:00:00+00:00',
#          '2022-06-17 10:00:00+00:00', '2022-09-16 10:00:00+00:00', '2022-12-16 11:00:00+00:00',
#          '2023-03-17 11:00:00+00:00', '2023-06-16 10:00:00+00:00', '2023-09-15 10:00:00+00:00',
#          '2023-12-15 11:00:00+00:00', '2024-03-15 11:00:00+00:00', '2024-06-21 10:00:00+00:00',
#          '2024-08-16 10:00:00+00:00', '2024-12-17 11:00:00+00:00']
# # start_time = pd.to_datetime('2017-03-15 10:00:00+00:00')
# # end_time = pd.to_datetime('2017-06-19 10:00:00+00:00')
# j, k = 0, 1
#
# for i in ['8','9','0','1','2','3','4']:  # 从1到9
#     for prefix in ['ESH', 'ESM', 'ESU', 'ESZ']:
#         if i == '4' and prefix in ['ESZ']: #skip the part overlap with GE
#             continue
#         print(i)
#         file_name = f'{prefix}{i}.csv'  # 生成文件名
#         file_path = os.path.join(folder_path, file_name)  # 生成完整路径
#
#         # 检查文件是否存在
#         if os.path.exists(file_path):
#             df = pd.read_csv(file_path)  # 读取CSV文件
#             df['ts_event'] = pd.to_datetime(df['ts_event'])
#             start_time, end_time = times[j], times[k]
#
#             filtered_df = df[(df['ts_event'] >= start_time) & (df['ts_event'] <= end_time)]
#             dataframes.append(filtered_df)
#             # start_time = end_time
#             # end_time = end_time + pd.DateOffset(days=91)
#             j, k =j+1, k+1
#             print(end_time)
#
#
# combined_df = pd.concat(dataframes, ignore_index=True)
# combined_df.to_csv('/Users/siyuanfang/Downloads/AA econ/research track/data/futures/E-mini SP 500 Futures/SP500.csv', index=False,encoding = 'utf-8-sig')


# # #============================MP1========================================
# import pandas as pd
# import os
#
# # 文件夹路径
# folder_path = '/Users/siyuanfang/Downloads/AA econ/research track/data/futures/MP1/'
#
# # 创建一个空的列表来存储数据框
# dataframes = []
# times = ['2019-01-01 12:00:00+00:00','2019-02-01 12:00:00+00:00','2019-03-01 12:00:00+00:00','2019-04-01 11:00:00+00:00',
#          '2019-05-01 11:00:00+00:00','2019-06-01 11:00:00+00:00','2019-07-01 11:00:00+00:00','2019-08-01 11:00:00+00:00',
#          '2019-09-01 11:00:00+00:00','2019-10-01 11:00:00+00:00','2019-11-01 12:00:00+00:00','2019-12-01 12:00:00+00:00',
#          '2020-01-01 12:00:00+00:00','2020-02-01 12:00:00+00:00','2020-03-01 12:00:00+00:00','2020-04-01 11:00:00+00:00',
#          '2020-05-01 11:00:00+00:00','2020-06-01 11:00:00+00:00','2020-07-01 11:00:00+00:00','2020-08-01 11:00:00+00:00',
#          '2020-09-01 11:00:00+00:00','2020-10-01 11:00:00+00:00','2020-11-01 12:00:00+00:00','2020-12-01 12:00:00+00:00',
#          '2021-01-01 12:00:00+00:00','2021-02-01 12:00:00+00:00','2021-03-01 12:00:00+00:00','2021-04-01 11:00:00+00:00',
#          '2021-05-01 11:00:00+00:00','2021-06-01 11:00:00+00:00','2021-07-01 11:00:00+00:00','2021-08-01 11:00:00+00:00',
#          '2021-09-01 11:00:00+00:00','2021-10-01 11:00:00+00:00','2021-11-01 12:00:00+00:00','2021-12-01 12:00:00+00:00',
#          '2022-01-01 12:00:00+00:00','2022-02-01 12:00:00+00:00','2022-03-01 12:00:00+00:00','2022-04-01 11:00:00+00:00',
#          '2022-05-01 11:00:00+00:00','2022-06-01 11:00:00+00:00','2022-07-01 11:00:00+00:00','2022-08-01 11:00:00+00:00',
#          '2022-09-01 11:00:00+00:00','2022-10-01 11:00:00+00:00','2022-11-01 12:00:00+00:00','2022-12-01 12:00:00+00:00',
#          '2023-01-01 12:00:00+00:00','2023-02-01 12:00:00+00:00','2023-03-01 12:00:00+00:00','2023-04-01 11:00:00+00:00',
#          '2023-05-01 11:00:00+00:00','2023-06-01 11:00:00+00:00','2023-07-01 11:00:00+00:00','2023-08-01 11:00:00+00:00',
#          '2023-09-01 11:00:00+00:00','2023-10-01 11:00:00+00:00','2023-11-01 12:00:00+00:00','2023-12-01 12:00:00+00:00',
#          '2024-01-01 12:00:00+00:00','2024-02-01 12:00:00+00:00','2024-03-01 12:00:00+00:00','2024-04-01 11:00:00+00:00',
#          '2024-05-01 11:00:00+00:00','2024-06-01 11:00:00+00:00','2024-07-01 11:00:00+00:00','2024-08-01 11:00:00+00:00',
#          '2024-09-01 11:00:00+00:00','2024-10-01 11:00:00+00:00','2024-11-01 12:00:00+00:00','2024-12-01 12:00:00+00:00']
# # start_time = pd.to_datetime('2017-03-15 10:00:00+00:00')
# # end_time = pd.to_datetime('2017-06-19 10:00:00+00:00')
# j, k = 0, 1
#
# for i in ['9','0','1','2','3','4']:  # 从1到9
#     for prefix in ['ZQF', 'ZQG', 'ZQH', 'ZQJ', 'ZQK', 'ZQM', 'ZQN', 'ZQQ', 'ZQU', 'ZQV', 'ZQX', 'ZQZ']:
#         if i == '4' and prefix in ['ZQU', 'ZQV', 'ZQX', 'ZQZ']: #skip the part overlap with GE
#             continue
#         print(i)
#         file_name = f'{prefix}{i}.csv'  # 生成文件名
#         file_path = os.path.join(folder_path, file_name)  # 生成完整路径
#
#         # 检查文件是否存在
#         if os.path.exists(file_path):
#             df = pd.read_csv(file_path)  # 读取CSV文件
#             df['ts_event'] = pd.to_datetime(df['ts_event'])
#             start_time, end_time = times[j], times[k]
#
#             filtered_df = df[(df['ts_event'] >= start_time) & (df['ts_event'] <= end_time)]
#             dataframes.append(filtered_df)
#             # start_time = end_time
#             # end_time = end_time + pd.DateOffset(days=91)
#             j, k =j+1, k+1
#             print(end_time)
#
#
# combined_df = pd.concat(dataframes, ignore_index=True)
# combined_df.to_csv('/Users/siyuanfang/Downloads/AA econ/research track/data/futures/E-mini SP 500 Futures/MP1.csv', index=False,encoding = 'utf-8-sig')


# # #============================MP2========================================
# import pandas as pd
# import os
#
# # 文件夹路径
# folder_path = '/Users/siyuanfang/Downloads/AA econ/research track/data/futures/MP1/'
#
# # 创建一个空的列表来存储数据框
# dataframes = []
# times = ['2019-01-01 12:00:00+00:00','2019-02-01 12:00:00+00:00','2019-03-01 12:00:00+00:00','2019-04-01 11:00:00+00:00',
#          '2019-05-01 11:00:00+00:00','2019-06-01 11:00:00+00:00','2019-07-01 11:00:00+00:00','2019-08-01 11:00:00+00:00',
#          '2019-09-01 11:00:00+00:00','2019-10-01 11:00:00+00:00','2019-11-01 12:00:00+00:00','2019-12-01 12:00:00+00:00',
#          '2020-01-01 12:00:00+00:00','2020-02-01 12:00:00+00:00','2020-03-01 12:00:00+00:00','2020-04-01 11:00:00+00:00',
#          '2020-05-01 11:00:00+00:00','2020-06-01 11:00:00+00:00','2020-07-01 11:00:00+00:00','2020-08-01 11:00:00+00:00',
#          '2020-09-01 11:00:00+00:00','2020-10-01 11:00:00+00:00','2020-11-01 12:00:00+00:00','2020-12-01 12:00:00+00:00',
#          '2021-01-01 12:00:00+00:00','2021-02-01 12:00:00+00:00','2021-03-01 12:00:00+00:00','2021-04-01 11:00:00+00:00',
#          '2021-05-01 11:00:00+00:00','2021-06-01 11:00:00+00:00','2021-07-01 11:00:00+00:00','2021-08-01 11:00:00+00:00',
#          '2021-09-01 11:00:00+00:00','2021-10-01 11:00:00+00:00','2021-11-01 12:00:00+00:00','2021-12-01 12:00:00+00:00',
#          '2022-01-01 12:00:00+00:00','2022-02-01 12:00:00+00:00','2022-03-01 12:00:00+00:00','2022-04-01 11:00:00+00:00',
#          '2022-05-01 11:00:00+00:00','2022-06-01 11:00:00+00:00','2022-07-01 11:00:00+00:00','2022-08-01 11:00:00+00:00',
#          '2022-09-01 11:00:00+00:00','2022-10-01 11:00:00+00:00','2022-11-01 12:00:00+00:00','2022-12-01 12:00:00+00:00',
#          '2023-01-01 12:00:00+00:00','2023-02-01 12:00:00+00:00','2023-03-01 12:00:00+00:00','2023-04-01 11:00:00+00:00',
#          '2023-05-01 11:00:00+00:00','2023-06-01 11:00:00+00:00','2023-07-01 11:00:00+00:00','2023-08-01 11:00:00+00:00',
#          '2023-09-01 11:00:00+00:00','2023-10-01 11:00:00+00:00','2023-11-01 12:00:00+00:00','2023-12-01 12:00:00+00:00',
#          '2024-01-01 12:00:00+00:00','2024-02-01 12:00:00+00:00','2024-03-01 12:00:00+00:00','2024-04-01 11:00:00+00:00',
#          '2024-05-01 11:00:00+00:00','2024-06-01 11:00:00+00:00','2024-07-01 11:00:00+00:00','2024-08-01 11:00:00+00:00',
#          '2024-09-01 11:00:00+00:00','2024-10-01 11:00:00+00:00','2024-11-01 12:00:00+00:00','2024-12-01 12:00:00+00:00']
# # start_time = pd.to_datetime('2017-03-15 10:00:00+00:00')
# # end_time = pd.to_datetime('2017-06-19 10:00:00+00:00')
# j, k = 0, 1
#
# for i in ['9','0','1','2','3','4']:  # 从1到9
#     for prefix in ['ZQF', 'ZQG', 'ZQH', 'ZQJ', 'ZQK', 'ZQM', 'ZQN', 'ZQQ', 'ZQU', 'ZQV', 'ZQX', 'ZQZ']:
#         if i == '9' and prefix == 'ZQF':
#             continue
#         if i == '4' and prefix in ['ZQV', 'ZQX', 'ZQZ']: #skip the part overlap with GE
#             continue
#         print(i)
#         file_name = f'{prefix}{i}.csv'  # 生成文件名
#         file_path = os.path.join(folder_path, file_name)  # 生成完整路径
#
#         # 检查文件是否存在
#         if os.path.exists(file_path):
#             df = pd.read_csv(file_path)  # 读取CSV文件
#             df['ts_event'] = pd.to_datetime(df['ts_event'])
#             start_time, end_time = times[j], times[k]
#
#             filtered_df = df[(df['ts_event'] >= start_time) & (df['ts_event'] <= end_time)]
#             dataframes.append(filtered_df)
#             # start_time = end_time
#             # end_time = end_time + pd.DateOffset(days=91)
#             j, k =j+1, k+1
#             print(end_time)
#
#
# combined_df = pd.concat(dataframes, ignore_index=True)
# combined_df.to_csv('/Users/siyuanfang/Downloads/AA econ/research track/data/futures/E-mini SP 500 Futures/MP2.csv', index=False,encoding = 'utf-8-sig')


# #============================MP3========================================
import pandas as pd
import os

# 文件夹路径
folder_path = '/Users/siyuanfang/Downloads/AA econ/research track/data/futures/MP1/'

# 创建一个空的列表来存储数据框
dataframes = []
times = ['2019-01-01 12:00:00+00:00','2019-02-01 12:00:00+00:00','2019-03-01 12:00:00+00:00','2019-04-01 11:00:00+00:00',
         '2019-05-01 11:00:00+00:00','2019-06-01 11:00:00+00:00','2019-07-01 11:00:00+00:00','2019-08-01 11:00:00+00:00',
         '2019-09-01 11:00:00+00:00','2019-10-01 11:00:00+00:00','2019-11-01 12:00:00+00:00','2019-12-01 12:00:00+00:00',
         '2020-01-01 12:00:00+00:00','2020-02-01 12:00:00+00:00','2020-03-01 12:00:00+00:00','2020-04-01 11:00:00+00:00',
         '2020-05-01 11:00:00+00:00','2020-06-01 11:00:00+00:00','2020-07-01 11:00:00+00:00','2020-08-01 11:00:00+00:00',
         '2020-09-01 11:00:00+00:00','2020-10-01 11:00:00+00:00','2020-11-01 12:00:00+00:00','2020-12-01 12:00:00+00:00',
         '2021-01-01 12:00:00+00:00','2021-02-01 12:00:00+00:00','2021-03-01 12:00:00+00:00','2021-04-01 11:00:00+00:00',
         '2021-05-01 11:00:00+00:00','2021-06-01 11:00:00+00:00','2021-07-01 11:00:00+00:00','2021-08-01 11:00:00+00:00',
         '2021-09-01 11:00:00+00:00','2021-10-01 11:00:00+00:00','2021-11-01 12:00:00+00:00','2021-12-01 12:00:00+00:00',
         '2022-01-01 12:00:00+00:00','2022-02-01 12:00:00+00:00','2022-03-01 12:00:00+00:00','2022-04-01 11:00:00+00:00',
         '2022-05-01 11:00:00+00:00','2022-06-01 11:00:00+00:00','2022-07-01 11:00:00+00:00','2022-08-01 11:00:00+00:00',
         '2022-09-01 11:00:00+00:00','2022-10-01 11:00:00+00:00','2022-11-01 12:00:00+00:00','2022-12-01 12:00:00+00:00',
         '2023-01-01 12:00:00+00:00','2023-02-01 12:00:00+00:00','2023-03-01 12:00:00+00:00','2023-04-01 11:00:00+00:00',
         '2023-05-01 11:00:00+00:00','2023-06-01 11:00:00+00:00','2023-07-01 11:00:00+00:00','2023-08-01 11:00:00+00:00',
         '2023-09-01 11:00:00+00:00','2023-10-01 11:00:00+00:00','2023-11-01 12:00:00+00:00','2023-12-01 12:00:00+00:00',
         '2024-01-01 12:00:00+00:00','2024-02-01 12:00:00+00:00','2024-03-01 12:00:00+00:00','2024-04-01 11:00:00+00:00',
         '2024-05-01 11:00:00+00:00','2024-06-01 11:00:00+00:00','2024-07-01 11:00:00+00:00','2024-08-01 11:00:00+00:00',
         '2024-09-01 11:00:00+00:00','2024-10-01 11:00:00+00:00','2024-11-01 12:00:00+00:00','2024-12-01 12:00:00+00:00']
# start_time = pd.to_datetime('2017-03-15 10:00:00+00:00')
# end_time = pd.to_datetime('2017-06-19 10:00:00+00:00')
j, k = 0, 1

for i in ['9','0','1','2','3','4']:  # 从1到9
    for prefix in ['ZQF', 'ZQG', 'ZQH', 'ZQJ', 'ZQK', 'ZQM', 'ZQN', 'ZQQ', 'ZQU', 'ZQV', 'ZQX', 'ZQZ']:
        if i == '9' and prefix in ['ZQF','ZQG']:
            continue
        if i == '4' and prefix in ['ZQX', 'ZQZ']: #skip the part overlap with GE
            continue
        print(i)
        file_name = f'{prefix}{i}.csv'  # 生成文件名
        file_path = os.path.join(folder_path, file_name)  # 生成完整路径

        # 检查文件是否存在
        if os.path.exists(file_path):
            df = pd.read_csv(file_path)  # 读取CSV文件
            df['ts_event'] = pd.to_datetime(df['ts_event'])
            start_time, end_time = times[j], times[k]

            filtered_df = df[(df['ts_event'] >= start_time) & (df['ts_event'] <= end_time)]
            dataframes.append(filtered_df)
            # start_time = end_time
            # end_time = end_time + pd.DateOffset(days=91)
            j, k =j+1, k+1
            print(end_time)


combined_df = pd.concat(dataframes, ignore_index=True)
combined_df.to_csv('/Users/siyuanfang/Downloads/AA econ/research track/data/futures/E-mini SP 500 Futures/MP3.csv', index=False,encoding = 'utf-8-sig')
