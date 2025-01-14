# import pandas as pd
# import numpy as np
# from sklearn.decomposition import PCA
# from sklearn.linear_model import LinearRegression
# from sklearn.preprocessing import StandardScaler
# import statsmodels.api as sm
# import os
#
# # 加载数据
# # 假设数据文件是 CSV 格式（需要根据具体情况调整文件格式）
# os.chdir('/Users/siyuanfang/Downloads/AA econ/research track/code/new_data/')
# data = pd.read_csv("reg_fomc_announcement.csv")
#
# # 提取用于 PCA 的变量
# pca_vars = ["MP1","MP2","MP3", "ED2", "ED3", "ED4"]
# data_pca = data[pca_vars].dropna()  # 去掉缺失值
#
# scaler = StandardScaler()
# data_pca = scaler.fit_transform(data_pca)
# # 执行主成分分析
# pca = PCA(n_components=2)  # 提取前两个主成分
# # pca_scores = pca.fit_transform(data_pca)
# pca.fit(data_pca)
# # 将主成分结果添加到数据框
# pca_scores = pca.transform(data_pca)
# data["f1"] = pca_scores[:, 0]  # 第一主成分
# data["f2"] = pca_scores[:, 1]  # 第二主成分
#
# # 提取特征向量（旋转矩阵）
# evec = pca.components_.T  # 转置以匹配 Stata 的输出格式
#
# # 计算旋转权重
# a1 = evec[0, 0] / (evec[0, 0] + evec[0, 1])
# a2 = evec[0, 1] / (evec[0, 0] + evec[0, 1])
#
# # 计算主成分的方差
# vf1 = np.var(data["f1"], ddof=1)  # 样本方差
# vf2 = np.var(data["f2"], ddof=1)
#
# # 计算旋转后的权重 b1 和 b2
# b1 = -1 * a2 * vf2 / (a1 * vf1 - a2 * vf2)
# b2 = a1 * vf1 / (a1 * vf1 - a2 * vf2)
#
# # 打印权重
# print(f"a1: {a1}, a2: {a2}, b1: {b1}, b2: {b2}")
#
# # 生成旋转后的因子
# data["transfact1"] = a1 * data["f1"] + a2 * data["f2"]
# data["transfact2"] = b1 * data["f1"] + b2 * data["f2"]
#
# # 标准化 transfact1，使其回归系数对 mp1tight 为 1
# # 回归 transfact1 对 mp1tight
# mask = data["ED2"].notna()  # 筛选非缺失值
# reg1 = LinearRegression().fit(data.loc[mask, ['transfact1']], data.loc[mask, 'MP1'])
#
# # 调整 transfact1
# data["transfact1"] *= reg1.coef_[0]
#
# # 标准化 transfact2，使其对 ed4tightchange 的影响与 transfact1 一致
# # 回归 transfact1 和 transfact2 对 ed4tightchange
# reg2 = LinearRegression().fit(data.loc[mask, ['transfact1', 'transfact2']], data.loc[mask, 'ED4'])
# # 调整 transfact2
# data["transfact2"] *= reg2.coef_[1] / reg2.coef_[0]
#
# # 打印最终因子
# print(data[["transfact1", "transfact2"]].head())
#
# import pandas as pd
# import statsmodels.api as sm
# from statsmodels.iolib.summary2 import summary_col
#
# # 1. 提供变量标签（为变量创建字典标签）
# # variable_labels = {
# #     "mp1tight": "MP1T",
# #     "mp2tight": "MP2T",
# #     "ed1tightchange": "ED1T",
# #     "ed2tightchange": "ED2T",
# #     "ed3tightchange": "ED3T",
# #     "ed4tightchange": "ED4T",
# #     "change3mtight": "3MthT",
# #     "change6mtight": "6MthT",
# #     "change2ytight": "2yrT",
# #     "change5ytight": "5yrT",
# #     "change10ytight": "10yrT",
# #     "change30ytight": "30yrT",
# #     "changefwdt": "5FWD5T",
# #     "spchangetight": "S&P500T",
# # }
#
# # 将标签映射到数据框（可选）
# # data.rename(columns=variable_labels, inplace=True)
#
# # 2. 回归分析函数
# def run_regression(data, y_var, x_vars, robust=True):
#     """
#     运行回归并返回结果
#     :param data: 数据框
#     :param y_var: 因变量
#     :param x_vars: 自变量列表
#     :param robust: 是否使用稳健标准误
#     :return: 回归结果对象
#     """
#     X = sm.add_constant(data[x_vars])  # 添加常数项
#     y = data[y_var]
#     model = sm.OLS(y, X, missing="drop").fit(
#         cov_type="HC3" if robust else "nonrobust"
#     )  # 使用稳健标准误
#     return model
#
# # 3. 创建一个列表存储回归结果，便于后续输出
# results = []
#
# # 3.3 对变量列表中的每个变量进行回归
# variables = [
#     "MP1",
#     "MP2",
#     "MP3",
#     "ED2",
#     "ED3",
#     "ED4",
#     "SP500"
# ]
# variables2 = [item for item in variables for _ in range(2)]
# for var in variables:
#     # 回归 1: `var` ~ `transfact1`
#     model_single = run_regression(data, var, ["transfact1"], robust=True)
#     results.append(model_single)
#
#     # 回归 2: `var` ~ `transfact1 + transfact2`
#     model_double = run_regression(data, var, ["transfact1", "transfact2"], robust=True)
#     results.append(model_double)
#
# # # 3.4 回归 `spchangetight` ~ `transfact1` 和 `transfact1 + transfact2`
# # model_sp1 = run_regression(data, "spchangetight", ["transfact1"], robust=True)
# # results.append(model_sp1)
# #
# # model_sp2 = run_regression(data, "spchangetight", ["transfact1", "transfact2"], robust=True)
# # results.append(model_sp2)
#
# # 4. 格式化输出结果
# # 使用 summary_col 将多个回归结果合并成表格格式
# output = summary_col(
#     results,
#     stars=True,  # 添加显著性星号
#     float_format="%0.4f",  # 控制小数点格式
#     model_names=[
#         f"Model {i}" for i in variables2
#     ],  # 为每个回归模型命名
#     info_dict={"N": lambda x: f"{int(x.nobs)}"},  # 显示样本量
#     regressor_order=["const", "transfact1", "transfact2"],  # 控制变量顺序
# )
#
# # 打印输出结果
# print(output)
#
# # 5. 保存结果到文件
# with open("output_test.csv", "w") as f:
#     f.write(output.as_text())


# #######============================the chair speeches=======================================
import pandas as pd
import numpy as np
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
import statsmodels.api as sm
import os

# 加载数据
# 假设数据文件是 CSV 格式（需要根据具体情况调整文件格式）
os.chdir('/Users/siyuanfang/Downloads/AA econ/research track/code/new_data/')
data = pd.read_csv("reg_baha_powell_79.csv")

# 提取用于 PCA 的变量
pca_vars = ["ED2", "ED3", "ED4"]
data_pca = data[pca_vars].dropna()  # 去掉缺失值
scaler = StandardScaler()
data_pca = scaler.fit_transform(data_pca)

# 执行主成分分析
pca = PCA(n_components=1)  # 提取前两个主成分
# pca_scores = pca.fit_transform(data_pca)
pca.fit(data_pca)
# 将主成分结果添加到数据框
pca_scores = pca.transform(data_pca)
data["f1"] = pca_scores[:, 0]  # 第一主成分
# data["f2"] = pca_scores[:, 1]  # 第二主成分
#
# # 提取特征向量（旋转矩阵）
# evec = pca.components_.T  # 转置以匹配 Stata 的输出格式
#
# # 计算旋转权重
# a1 = evec[0, 0] / (evec[0, 0] + evec[0, 1])
# a2 = evec[0, 1] / (evec[0, 0] + evec[0, 1])
#
# # 计算主成分的方差
# vf1 = np.var(data["f1"], ddof=1)  # 样本方差
# vf2 = np.var(data["f2"], ddof=1)
#
# # 计算旋转后的权重 b1 和 b2
# b1 = -1 * a2 * vf2 / (a1 * vf1 - a2 * vf2)
# b2 = a1 * vf1 / (a1 * vf1 - a2 * vf2)
#
# # 打印权重
# print(f"a1: {a1}, a2: {a2}, b1: {b1}, b2: {b2}")

# 生成旋转后的因子
data["transfact1"] = data["f1"]
std_dev = data['transfact1'].std()
print(std_dev)
data["transfact1"] = data["transfact1"]/std_dev
# data["transfact2"] = b1 * data["f1"] + b2 * data["f2"]

# 标准化 transfact1，使其回归系数对 mp1tight 为 1
# 回归 transfact1 对 mp1tight
# mask = data["ED2"].notna()  # 筛选非缺失值
# reg1 = LinearRegression().fit(data.loc[mask, ['transfact1']], data.loc[mask, 'MP1'])
#
# # 调整 transfact1
# data["transfact1"] *= reg1.coef_[0]
#
# # 标准化 transfact2，使其对 ed4tightchange 的影响与 transfact1 一致
# # 回归 transfact1 和 transfact2 对 ed4tightchange
# reg2 = LinearRegression().fit(data.loc[mask, ['transfact1', 'transfact2']], data.loc[mask, 'ED4'])
# # 调整 transfact2
# data["transfact2"] *= reg2.coef_[1] / reg2.coef_[0]

# 打印最终因子
# print(data[["transfact1", "transfact2"]].head())

import pandas as pd
import statsmodels.api as sm
from statsmodels.iolib.summary2 import summary_col

# 1. 提供变量标签（为变量创建字典标签）
# variable_labels = {
#     "mp1tight": "MP1T",
#     "mp2tight": "MP2T",
#     "ed1tightchange": "ED1T",
#     "ed2tightchange": "ED2T",
#     "ed3tightchange": "ED3T",
#     "ed4tightchange": "ED4T",
#     "change3mtight": "3MthT",
#     "change6mtight": "6MthT",
#     "change2ytight": "2yrT",
#     "change5ytight": "5yrT",
#     "change10ytight": "10yrT",
#     "change30ytight": "30yrT",
#     "changefwdt": "5FWD5T",
#     "spchangetight": "S&P500T",
# }

# 将标签映射到数据框（可选）
# data.rename(columns=variable_labels, inplace=True)

# 2. 回归分析函数
def run_regression(data, y_var, x_vars, robust=True):
    """
    运行回归并返回结果
    :param data: 数据框
    :param y_var: 因变量
    :param x_vars: 自变量列表
    :param robust: 是否使用稳健标准误
    :return: 回归结果对象
    """
    X = sm.add_constant(data[x_vars])  # 添加常数项
    y = data[y_var]
    model = sm.OLS(y, X, missing="drop").fit(
        cov_type="HC3" if robust else "nonrobust"
    )  # 使用稳健标准误
    return model

# 3. 创建一个列表存储回归结果，便于后续输出
results = []

# 3.3 对变量列表中的每个变量进行回归
variables = [
    "ED2",
    "ED3",
    "ED4",
    "SP500"
]
# variables2 = [item for item in variables for _ in range(2)]
for var in variables:
    # 回归 1: `var` ~ `transfact1`
    model_single = run_regression(data, var, ["transfact1"], robust=True)
    results.append(model_single)

    # 回归 2: `var` ~ `transfact1 + transfact2`
    # model_double = run_regression(data, var, ["transfact1", "transfact2"], robust=True)
    # results.append(model_double)

# # 3.4 回归 `spchangetight` ~ `transfact1` 和 `transfact1 + transfact2`
# model_sp1 = run_regression(data, "spchangetight", ["transfact1"], robust=True)
# results.append(model_sp1)
#
# model_sp2 = run_regression(data, "spchangetight", ["transfact1", "transfact2"], robust=True)
# results.append(model_sp2)

# 4. 格式化输出结果
# 使用 summary_col 将多个回归结果合并成表格格式
output = summary_col(
    results,
    stars=True,  # 添加显著性星号
    float_format="%0.4f",  # 控制小数点格式
    model_names=[
        f"Model {i}" for i in variables
    ],  # 为每个回归模型命名
    info_dict={"N": lambda x: f"{int(x.nobs)}"},  # 显示样本量
    regressor_order=["const", "transfact1", "transfact2"],  # 控制变量顺序
)

# 打印输出结果
print(output)

# 5. 保存结果到文件
with open("output_test2.csv", "w") as f:
    f.write(output.as_text())