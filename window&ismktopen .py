#==================================================match event to time window===============================
import glob
import pandas as pd
import pytz
from datetime import datetime, timedelta
import pandas_market_calendars as mcal
import numpy as np

def is_nyse_open(time_str):
    # Load the NYSE trading calendar
    nyse = mcal.get_calendar('NYSE')

    input_time = datetime.fromisoformat(str(time_str))
    # input_time = pd.to_datetime(time_str)

    # Convert to Eastern Time
    eastern = pytz.timezone('America/New_York')
    input_time = input_time.astimezone(eastern)
    # input_time = input_time.dt.tz_convert(eastern)

    # Get the schedule for the specific day
    schedule = nyse.schedule(start_date=input_time.strftime('%Y-%m-%d'), end_date=input_time.strftime('%Y-%m-%d'))

    # Check if the day is a trading day and within trading hours
    if not schedule.empty:
        market_open = schedule.iloc[0]['market_open'].tz_convert(eastern)
        market_close = schedule.iloc[0]['market_close'].tz_convert(eastern)
        if market_open <= input_time <= market_close:
            return True
    return False


df_sp500 = pd.read_csv('D:/AA econ/research track/data/intraday data2/sp500_1011-247-3.csv')
path = 'D:/AA econ/research track/data/Youtube CNBC Fed11/*.csv'
xlsx_files = glob.glob(path)
# df_Goolsbee = pd.read_csv('D:/AA econ/research track/data/Youtube CNBC Fed11/Goolsbee.csv')
for file in xlsx_files:
    df = pd.read_csv(file)
    # df['Publish_Times'] = pd.to_datetime(df['Publish_Times'])
    tz_pacific = pytz.timezone('US/Pacific')
    tz_eastern = pytz.timezone('US/Eastern')
    tz_utc = pytz.utc
    df['Publish_Times'] = pd.to_datetime(df['Publish_Times'], utc=True, format='%Y-%m-%d %H:%M:%S%z')
    df_sp500['Datetime'] = pd.to_datetime(df_sp500['Datetime'], utc=True, format='%Y-%m-%d %H:%M:%S%z')

    df['Publish_Times'] = df['Publish_Times'].dt.tz_convert(tz_pacific).dt.tz_convert(tz_utc)
    df_sp500['Datetime'] = df_sp500['Datetime'].dt.tz_convert(tz_eastern).dt.tz_convert(tz_utc)

    df['15bf'] = df['Publish_Times'] - timedelta(minutes=15)
    df['75aft'] = df['Publish_Times'] + timedelta(minutes=75)

    df_merged_bf = pd.merge_asof(df.sort_values('15bf'), df_sp500.sort_values('Datetime'), left_on='15bf',
                                 right_on='Datetime', direction='nearest')
    df_merged_aft = pd.merge_asof(df.sort_values('75aft'), df_sp500.sort_values('Datetime'), left_on='75aft',
                                  right_on='Datetime', direction='nearest')
    new_df = pd.DataFrame({
        '15bf': df_merged_bf['15bf'],
        'Datetime': df_merged_bf['Datetime'],
        'CLOSE': df_merged_bf['CLOSE'],
        '75aft': df_merged_aft['75aft'],
        'Datetime2': df_merged_aft['Datetime'],
        'CLOSE2': df_merged_aft['CLOSE'],
        'view': df['view'],
        'Publish_Times': df['Publish_Times'],
        'URL': df['URL'],
        'title': df['title'],
        'desc': df['desc']
    })
    isopen_15bfs, isopen_75afts = [], []
    bf15 = new_df['15bf'].tolist()
    aft75 = new_df['75aft'].tolist()
    for time in bf15:
        isopen_15bf = is_nyse_open(time)
        isopen_15bfs.append(isopen_15bf)
    for time in aft75:
        isopen_75aft = is_nyse_open(time)
        isopen_75afts.append(isopen_75aft)
    new_df['isopen_15bfs'] = isopen_15bfs
    new_df['isopen_75afts'] = isopen_75afts
    change = np.log(new_df['CLOSE2']) - np.log(new_df['CLOSE'])
    new_df['change'] = change

    filenew = file[:48] + '1' + file[48:]

    new_df.to_csv(filenew, index=False,encoding = 'utf-8-sig')





#
# #=========================================================whether the market is open====================================
# import pandas as pd
# import pandas_market_calendars as mcal
# from datetime import datetime
# import pytz
#
# def is_nyse_open(time_str):
#     # Load the NYSE trading calendar
#     nyse = mcal.get_calendar('NYSE')
#
#     input_time = datetime.fromisoformat(time_str)
#     # input_time = pd.to_datetime(time_str)
#
#     # Convert to Eastern Time
#     eastern = pytz.timezone('America/New_York')
#     input_time = input_time.astimezone(eastern)
#     # input_time = input_time.dt.tz_convert(eastern)
#
#     # Get the schedule for the specific day
#     schedule = nyse.schedule(start_date=input_time.strftime('%Y-%m-%d'), end_date=input_time.strftime('%Y-%m-%d'))
#
#     # Check if the day is a trading day and within trading hours
#     if not schedule.empty:
#         market_open = schedule.iloc[0]['market_open'].tz_convert(eastern)
#         market_close = schedule.iloc[0]['market_close'].tz_convert(eastern)
#         if market_open <= input_time <= market_close:
#             return True
#     return False
#
# # Example usage
#
# # time_str = "2024-07-04 09:35:07-04:00"
# df = pd.read_csv('D:/AA econ/research track/data/mkt_changes/sp500_goolsbee.csv')
# # print(df)
# isopen_15bfs, isopen_75afts = [],[]
# bf15 = df['15bf'].tolist()
# aft75 = df['75aft'].tolist()
# for time in bf15:
#     isopen_15bf = is_nyse_open(time)
#     isopen_15bfs.append(isopen_15bf)
# for time in aft75:
#     isopen_75aft = is_nyse_open(time)
#     isopen_75afts.append(isopen_75aft)
# df['isopen_15bfs'] = isopen_15bfs
# df['isopen_75afts'] = isopen_75afts
#
# # print(is_nyse_open(time_str))  # Output will depend on whether it's a trading day and time
# df.to_csv('D:/AA econ/research track/data/mkt_changes/sp500_goolsbee2.csv', index=False)
#
