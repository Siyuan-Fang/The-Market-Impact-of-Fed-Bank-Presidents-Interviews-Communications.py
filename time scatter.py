import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

# 读取数据
df = pd.read_excel('D:/AA econ/research track/articles/goolsbee test/goolsbeev1.2.xlsx')

# 将时间字符串转换为datetime对象
df['timestamp'] = pd.to_datetime(df['datetime'])

# 绘制散点图
plt.figure(figsize=(10, 2))
plt.scatter(df['timestamp'], [1] * len(df), alpha=0.5, s = 2)

# 设置时间格式
# plt.gca().xaxis.set_major_locator(mdates.DayLocator())
# plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
# plt.gcf().autofmt_xdate()  # 自动旋转日期标记

plt.xlabel('Time')
plt.yticks([])
plt.title('Event Density Over Time')
plt.show()