import pandas as pd
import pytz
from datetime import datetime, timedelta
import numpy as np

ED_list = ["MP1.csv","MP2.csv","MP3.csv","ED2.csv", "ED3.csv", "ED4.csv", "SP500.csv"]

# ED_list = ["ED3.csv"]
for ED_name in ED_list:
    ED_path = '/Users/siyuanfang/Downloads/AA econ/research track/data/futures/3-Month SOFR Futures/'
    ED_file = ED_path + ED_name

    main_folder = '/Users/siyuanfang/Downloads/AA econ/research track/code/new_data/'

    input_name = 'fomc_announcement'
    csv = '.csv'

    df_file = main_folder + input_name + csv


    df_ED = pd.read_csv(ED_file)
    df = pd.read_csv(df_file)
    df_a = pd.read_csv('/Users/siyuanfang/Downloads/AA econ/research track/table_graph/marco data release_clearn.csv')
    # 假设 datetime 列的名称为 'datetime'
    # 将字符串转换为 datetime 对象，并设置为东八区时区
    df_ED['Datetime'] = pd.to_datetime(df_ED['ts_event'], utc=True, format='%Y-%m-%d %H:%M:%S%z')
    df['Publish_Times'] = pd.to_datetime(df['Time'], format='%Y-%m-%d %H:%M:%S')
    df['Publish_Times'] = pd.to_datetime(df['Publish_Times']).dt.tz_localize('Asia/Shanghai')

    # 转换为 UTC 时区
    df['Publish_Times'] = df['Publish_Times'].dt.tz_convert('UTC')

    df['Publish_Times'] = pd.to_datetime(df['Publish_Times'], utc=True, format='%Y-%m-%d %H:%M:%S%z')

    df_a['Time'] = pd.to_datetime(df_a['Time'], format='%Y-%m-%d %H:%M:%S')
    df_a['Time'] = pd.to_datetime(df_a['Time'].dt.tz_localize('Asia/Shanghai')).dt.tz_convert('UTC')
    marco_release = pd.concat([df_a['Time'].head(300), df_a['Time'].tail(300)])

    aft_values = []
    # tz_pacific = pytz.timezone('US/Pacific')
    # tz_eastern = pytz.timezone('US/Eastern')
    # tz_utc2 = pytz.timezone('UTC')
    # tz_utc = pytz.utc
    for time in df['Publish_Times']:
        end_time = time + timedelta(minutes=20)
        close_release = marco_release[(marco_release >= time) & (marco_release <= end_time)]

        if not close_release.empty:
            # 如果有'marco_release'，保存最近的一个
            aft_values.append(close_release.min())
        else:
            # 如果没有，保存75分钟后的值
            aft_values.append(end_time)

    # df_ED['Datetime'] = df_ED['Datetime'].dt.tz_convert(tz_utc2).dt.tz_convert(tz_utc)

    df['15bf'] = df['Publish_Times'] - timedelta(minutes=10)
    df['75aft'] = aft_values

    df_merged_bf = pd.merge_asof(df.sort_values('15bf'), df_ED.sort_values('Datetime'), left_on='15bf',
                                 right_on='Datetime', direction='nearest')
    df_merged_aft = pd.merge_asof(df.sort_values('75aft'), df_ED.sort_values('Datetime'), left_on='75aft',
                                  right_on='Datetime', direction='nearest')
    new_df = pd.DataFrame({
        '15bf': df_merged_bf['15bf'],
        'Datetime': df_merged_bf['Datetime'],
        'CLOSE': df_merged_bf['open'],
        '75aft': df_merged_aft['75aft'],
        'Datetime2': df_merged_aft['Datetime'],
        'CLOSE2': df_merged_aft['close'],
        'Publish_Times': df['Publish_Times'],
        'title': df['Event']  # 更改过Event
    })
    change = np.log(new_df['CLOSE2']) - np.log(new_df['CLOSE'])
    new_df['change'] = change
    filenew= main_folder + input_name + ED_name

    new_df.to_csv(filenew, index=False, encoding='utf-8-sig')

    change_std = new_df.change.std()  # 标准差
    change_min = new_df.change.min()  # 最小值
    change_max = new_df.change.max()  # 最大值
    change_mean = new_df.change.mean()  # 均值
    print(len(new_df['change']))
    print(f'Standard Deviation: {change_std}')
    print(f'Minimum: {change_min}')
    print(f'Maximum: {change_max}')
    print(f'Mean: {change_mean}')


#下一步，写出求标准差、最小值、最大值、均值的代码
#换着数据来一遍
#ED2，ED4, SP500    fomc_announcement baha_powell baha_main interviews  minutes