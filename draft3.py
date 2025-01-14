# import pandas as pd
# import os
#
# # 指定文件夹路径
# folder_path = '/Users/siyuanfang/Downloads/AA econ/research track/data/Youtube CNBC Fed11ED2SS'
#
# # 创建一个空的DataFrame
# combined_df = pd.DataFrame()
#
# # 遍历文件夹中的所有CSV文件
# for filename in os.listdir(folder_path):
#     if filename.endswith('.csv'):
#         # 读取CSV文件
#         file_path = os.path.join(folder_path, filename)
#         df = pd.read_csv(file_path)
#         filename = os.path.splitext(filename)[0]
#         # 添加文件名作为新列
#         df['regional fed president'] = filename
#
#         # 合并到总的DataFrame
#         combined_df = pd.concat([combined_df, df], ignore_index=True)
# # 保存合并后的DataFrame到新的CSV文件
# combined_df.to_csv('/Users/siyuanfang/Downloads/AA econ/research track/data/summary/summary_v2.csv', index=False)


# import pandas as pd
#
# df = pd.read_csv('/Users/siyuanfang/Downloads/AA econ/research track/data/futures/3-Month SOFR Futures/ED4.csv')
# print(df)
# #=========================================分割ZQ数据=======================================================
# import pandas as pd
# import itertools
#
# # 读取CSV文件
# input_file = '/Users/siyuanfang/Downloads/zzz exe download/glbx-mdp3-20181229-20240901.ohlcv-1m.csv'  # 替换为你的CSV文件名
# df = pd.read_csv(input_file)
# df['ts_event'] = pd.to_datetime(df['ts_event'], errors='coerce')
# print(df['ts_event'].dtype)
#
# # 定义symbol_list
# symbol_list = ['ZQ'+f'{letter}{number}' for letter, number in itertools.product(['F', 'G', 'H', 'J', 'K', 'M', 'N', 'Q', 'U', 'V', 'X', 'Z'], ['9', '0', '1', '2', '3', '4'])]
# output_path = '/Users/siyuanfang/Downloads/AA econ/research track/data/futures/3-Month SOFR Futures/'
# # 依次读取symbol为symbol_list中的值对应的行，并保存为新的CSV文件
# df['ts_event'] = df['ts_event'].dt.strftime('%Y-%m-%d %H:%M:%S+00:00')
# for symbol in symbol_list:
#     print(symbol)
#     filtered_df = df[df['symbol'] == symbol]  # 假设CSV中有一列名为'symbol'
#     if not filtered_df.empty:
#         # print(symbol)
#         output_file = output_path + f'{symbol}.csv'
#         filtered_df.to_csv(output_file, index=False)
#         print(f'Saved {output_file}')


import pandas as pd
import os

from astropy.units import cd

# 读取CSV文件
# cd '/Users/siyuanfang/Downloads/AA econ/research track/code/new_data'
csv_file = '/Users/siyuanfang/Downloads/AA econ/research track/code/new_data/reg_fomc_announcement.csv'  # 替换为你的CSV文件名
df = pd.read_csv(csv_file)

# 将DataFrame保存为DTA文件
dta_file = '/Users/siyuanfang/Downloads/AA econ/research track/code/new_data/reg_fomc_announcement.dta'  # 替换为你想要的DTA文件名
df.to_stata(dta_file, write_index=False)