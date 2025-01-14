import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# 1. 读取CSV文件
data = pd.read_csv('/Users/siyuanfang/Downloads/AA econ/research track/data/summary/summary_v2.3.csv', encoding='utf-8-sig')  # 根据需要调整编码

# 2. 选择两列（假设列名为col1和col2），并取绝对值
# x = data['negative_index'].str.replace(',', '').astype(float)  # 转换为浮点数并取绝对值
x = data['RoBERTa_total'].astype(float)
y = (data['change'].astype(float))  # 转换为浮点数并取绝对值

# 3. 绘制散点图
plt.scatter(x, y)
plt.title("散点图")
plt.xlabel("RoBERTa_total")
plt.ylabel("change")
plt.show()

# 4. 计算相关度
correlation = np.corrcoef(x, y)[0, 1]  # 计算相关系数
print(f"correlation: {correlation}")