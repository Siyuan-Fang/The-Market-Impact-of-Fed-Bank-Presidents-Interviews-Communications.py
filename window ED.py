#==================================================match event to time window===============================
import glob
import pandas as pd
import pytz
from datetime import datetime, timedelta
import numpy as np


df_ED = pd.read_csv('D:/AA econ/research track/data/futures/3-Month SOFR Futures/ED2.csv')
path = 'D:/AA econ/research track/data/Youtube CNBC Fed11/*.csv'
xlsx_files = glob.glob(path)
# df_Goolsbee = pd.read_csv('D:/AA econ/research track/data/Youtube CNBC Fed11/Goolsbee.csv')
for file in xlsx_files:
    df = pd.read_csv(file)
    # df['Publish_Times'] = pd.to_datetime(df['Publish_Times'])
    tz_pacific = pytz.timezone('US/Pacific')
    # tz_eastern = pytz.timezone('US/Eastern')
    tz_utc2 = pytz.timezone('UTC')
    tz_utc = pytz.utc
    df['Publish_Times'] = pd.to_datetime(df['Publish_Times'], utc=True, format='%Y-%m-%d %H:%M:%S%z')
    df_ED['Datetime'] = pd.to_datetime(df_ED['ts_event'], utc=True, format='%Y-%m-%d %H:%M:%S%z')

    df['Publish_Times'] = df['Publish_Times'].dt.tz_convert(tz_pacific).dt.tz_convert(tz_utc)
    df_ED['Datetime'] = df_ED['Datetime'].dt.tz_convert(tz_utc2).dt.tz_convert(tz_utc)

    df['15bf'] = df['Publish_Times'] - timedelta(minutes=15)
    df['75aft'] = df['Publish_Times'] + timedelta(minutes=75)

    df_merged_bf = pd.merge_asof(df.sort_values('15bf'), df_ED.sort_values('Datetime'), left_on='15bf',
                                 right_on='Datetime', direction='nearest')
    df_merged_aft = pd.merge_asof(df.sort_values('75aft'), df_ED.sort_values('Datetime'), left_on='75aft',
                                  right_on='Datetime', direction='nearest')
    new_df = pd.DataFrame({
        '15bf': df_merged_bf['15bf'],
        'Datetime': df_merged_bf['Datetime'],
        'CLOSE': df_merged_bf['close'],
        '75aft': df_merged_aft['75aft'],
        'Datetime2': df_merged_aft['Datetime'],
        'CLOSE2': df_merged_aft['close'],
        'view': df['view'],
        'Publish_Times': df['Publish_Times'],
        'URL': df['URL'],
        'title': df['title'],
        'desc': df['desc']
    })
    change = np.log(new_df['CLOSE2']) - np.log(new_df['CLOSE'])
    new_df['change'] = change

    filenew = file[:49] + 'ED2' + file[49:]

    new_df.to_csv(filenew, index=False,encoding = 'utf-8-sig')