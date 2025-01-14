import pandas as pd
import matplotlib.pyplot as plt

# read three CSV documents
# df1 = pd.read_csv('/Users/siyuanfang/Downloads/AA econ/research track/data/futures/E-mini SP 500 Futures/ESH2.csv')
# df2 = pd.read_csv('/Users/siyuanfang/Downloads/AA econ/research track/data/futures/E-mini SP 500 Futures/ESM2.csv')
# df3 = pd.read_csv('/Users/siyuanfang/Downloads/AA econ/research track/data/futures/E-mini SP 500 Futures/ESU2.csv')
# df4 = pd.read_csv('/Users/siyuanfang/Downloads/AA econ/research track/data/futures/E-mini SP 500 Futures/ESZ2.csv')
# df5 = pd.read_csv('/Users/siyuanfang/Downloads/AA econ/research track/data/futures/E-mini SP 500 Futures/ESH3.csv')
# df6 = pd.read_csv('/Users/siyuanfang/Downloads/AA econ/research track/data/futures/E-mini SP 500 Futures/ESM3.csv')
# df7 = pd.read_csv('/Users/siyuanfang/Downloads/AA econ/research track/data/futures/E-mini SP 500 Futures/ESU3.csv')
# df8 = pd.read_csv('/Users/siyuanfang/Downloads/AA econ/research track/data/futures/E-mini SP 500 Futures/ESZ3.csv')
df1 = pd.read_csv('/Users/siyuanfang/Downloads/AA econ/research track/data/futures/3-Month SOFR Futures/GEH0.csv')
df2 = pd.read_csv('/Users/siyuanfang/Downloads/AA econ/research track/data/futures/3-Month SOFR Futures/GEM0.csv')
df3 = pd.read_csv('/Users/siyuanfang/Downloads/AA econ/research track/data/futures/3-Month SOFR Futures/GEU0.csv')
df4 = pd.read_csv('/Users/siyuanfang/Downloads/AA econ/research track/data/futures/3-Month SOFR Futures/GEZ0.csv')
df5 = pd.read_csv('/Users/siyuanfang/Downloads/AA econ/research track/data/futures/3-Month SOFR Futures/GEH1.csv')
df6 = pd.read_csv('/Users/siyuanfang/Downloads/AA econ/research track/data/futures/3-Month SOFR Futures/GEM1.csv')
df7 = pd.read_csv('/Users/siyuanfang/Downloads/AA econ/research track/data/futures/3-Month SOFR Futures/GEU1.csv')
df8 = pd.read_csv('/Users/siyuanfang/Downloads/AA econ/research track/data/futures/3-Month SOFR Futures/GEZ1.csv')
##### df4 = pd.read_csv('D:/AA econ/research track/data/intraday data/Treasury Yield 5 Years (^FVX).csv')
#
# select first three cols
df1 = df1.iloc[:, [0, 7]]
df2 = df2.iloc[:, [0, 7]]
df3 = df3.iloc[:, [0, 7]]
df4 = df4.iloc[:, [0, 7]]
df5 = df5.iloc[:, [0, 7]]
df6 = df6.iloc[:, [0, 7]]
df7 = df7.iloc[:, [0, 7]]
df8 = df8.iloc[:, [0, 7]]

# df4 = df4.iloc[:, [0, 5]]

# translate into datetime format
df1['Datetime'] = pd.to_datetime(df1['ts_event'])
df2['Datetime'] = pd.to_datetime(df2['ts_event'])
df3['Datetime'] = pd.to_datetime(df3['ts_event'])
df4['Datetime'] = pd.to_datetime(df4['ts_event'])
df5['Datetime'] = pd.to_datetime(df5['ts_event'])
df6['Datetime'] = pd.to_datetime(df6['ts_event'])
df7['Datetime'] = pd.to_datetime(df7['ts_event'])
df8['Datetime'] = pd.to_datetime(df8['ts_event'])
# df4['Datetime'] = pd.to_datetime(df4['Datetime'])
# df1['Adj Close'] = (df1['Adj Close'] - 100)/2

# Draw line chart
plt.figure(figsize=(100, 36))

# plt.scatter(df1['Datetime'], df1['close'], label='SR3H2', color='pink', alpha=0.7, s=0.5)
# plt.scatter(df2['Datetime'], df2['close'], label='SR3M2', color='r', alpha=0.7, s=0.5)
# plt.scatter(df3['Datetime'], df3['close'], label='SR3U2', color='b', alpha=0.7, s=0.5)
# plt.scatter(df4['Datetime'], df4['close'], label='SR3Z2', color='slateblue', alpha=0.7, s=0.5)
# plt.scatter(df5['Datetime'], df5['close'], label='SR3H3', color='springgreen', alpha=0.7, s=0.5)
# plt.scatter(df6['Datetime'], df6['close'], label='SR3M3', color='turquoise', alpha=0.7, s=0.5)
# plt.scatter(df7['Datetime'], df7['close'], label='SR3U3', color='wheat', alpha=0.7, s=0.5)
# plt.scatter(df8['Datetime'], df8['close'], label='SR3Z3', color='yellow', alpha=0.7, s=0.5)

plt.scatter(df1['Datetime'], df1['close'], label='GEH2', color='pink', alpha=0.7, s=0.5)
plt.scatter(df2['Datetime'], df2['close'], label='GEM2', color='r', alpha=0.7, s=0.5)
plt.scatter(df3['Datetime'], df3['close'], label='GEU2', color='b', alpha=0.7, s=0.5)
plt.scatter(df4['Datetime'], df4['close'], label='GEZ2', color='slateblue', alpha=0.7, s=0.5)
plt.scatter(df5['Datetime'], df5['close'], label='GEH3', color='springgreen', alpha=0.7, s=0.5)
plt.scatter(df6['Datetime'], df6['close'], label='GEM3', color='turquoise', alpha=0.7, s=0.5)
plt.scatter(df7['Datetime'], df7['close'], label='GEU3', color='wheat', alpha=0.7, s=0.5)
plt.scatter(df8['Datetime'], df8['close'], label='GEZ3', color='yellow', alpha=0.7, s=0.5)


# plt.plot(df4['Datetime'], df4['Adj Close'], label='Treasury Yield 5 Years')

# # Powell: Inflation is still too high
# specific_time1 = pd.Timestamp('2023-10-19 12:00:00-04:00')
# plt.axvline(x=specific_time1, color='b', linestyle='--', label='Powell: Inflation is still too high')
#
# # Powell: Although inflation has moved down from its peak — a welcome development — it remains too high
# specific_time2 = pd.Timestamp('2023-08-25 10:05:00-04:00')
# plt.axvline(x=specific_time2, color='r', linestyle='--', label='Powell: Although inflation has moved down from its peak — a welcome development — it remains too high')


plt.xlabel('Datetime')
plt.ylabel('price')
plt.title('Treasury')
plt.legend()
# plt.tight_layout()
#
# figManager = plt.get_current_fig_manager()
# figManager.full_screen_toggle()
plt.show()

#hong kong 7/14 12:10am