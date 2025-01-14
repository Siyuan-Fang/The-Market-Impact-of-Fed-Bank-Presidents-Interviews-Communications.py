# ######=============================================figure 1======================================
# import matplotlib.pyplot as plt
# import numpy as np
# import pandas as pd
#
# ED_list = ["ED2.csv", "ED4.csv", "SP500.csv"]
# main_folder = '/Users/siyuanfang/Downloads/AA econ/research track/code/new_data/'
# input_name_list = ["fomc_announcement_", "baha_powell_79", "interviews_top100"]
# data_list = []
#
# for ED_name in ED_list:
#     for input_name in input_name_list:
#         file = main_folder + input_name + ED_name
#         df = pd.read_csv(file)
#         data_list.append((df['change']*100).values)
#
#
# titles = ['FOMC Announcement effects, ED2', 'Fed Chair effects, ED2', 'Fed Presidents effects(100), ED2',
#           'FOMC Announcement effects, ED4', 'Fed Chair effects, ED4', 'Fed Presidents effects(100), ED4',
#           'FOMC Announcement effects, SP 500', 'Fed Chair effects, SP 500', 'Fed Presidents effects(100), SP 500']
#
# # 创建绘图
# fig, axes = plt.subplots(3, 3, figsize=(9, 10), tight_layout=True)  # 2 行 3 列子图
#
# # 遍历数据并绘制直方图
# for i, ax in enumerate(axes.flat):  # 展平子图数组以便迭代
#     ax.hist(data_list[i], bins=15, color='skyblue', edgecolor='black')
#     ax.set_title(titles[i])  # 设置标题
#     # ax.set_xlabel('Value')  # 设置X轴标签
#     # # ax.set_ylabel('Frequency')  # 设置Y轴标签
#     if i < 6:  # 前 6 个图
#         ax.set_xlim(-0.2, 0.2)
#     else:  # 后 3 个图
#         ax.set_xlim(-2, 2)
#
# # 优化布局并显示
# plt.tight_layout()
# plt.show()

####===================================================================================================================
##================================================table 2 =============================================================
# import matplotlib.pyplot as plt
# import numpy as np
# import pandas as pd
#
# ED_list = ["ED2.csv", "ED3.csv", "ED4.csv", "SP500.csv"]
# main_folder = '/Users/siyuanfang/Downloads/AA econ/research track/code/new_data/'
# input_name_list = ["fomc_announcement", "baha_powell_79", "interviews_top100","interviews_top200","minutes_"]
# results2,results3 = [],[]
# count = 0
# results3 = pd.DataFrame()
#
# for input_name in input_name_list:
#     for ED_name in ED_list:
#         file = main_folder + input_name + ED_name
#         df = pd.read_csv(file)
#         # data_list.append((df['change']*100).values)
#         df['Publish_Times'] = pd.to_datetime(df['Publish_Times'])
#
#         # 设置datetime为索引
#         df.set_index('Publish_Times', inplace=True)
#         start_date = '2019-01-01'
#         end_date = '2024-07-31'
#         df = df[start_date:end_date]
#         monthly_sum = df['change'].resample('M').sum().fillna(0)
#         # monthly_sum = monthly_sum.reindex(all_months, fill_value=0)
#         monthly_sum = monthly_sum.combine_first(monthly_sum)
#         # 将结果转换为DataFrame  .to_period('M')
#
#
#         monthly_data = pd.DataFrame({
#             'mouth2': monthly_sum.index.to_period('M'),
#             input_name: monthly_sum.values
#         }).reset_index(drop=True)
#         if input_name == 'interviews_top100':
#             top_padding = pd.DataFrame({
#                 'mouth2': [0] * 11,  # 用 0 填充 'mouth2' 列
#                 input_name: [0] * 11  # 用 0 填充 input_name 列
#             })
#             bottom_padding = pd.DataFrame({
#                 'mouth2': [0],  # 用 0 填充 'mouth2' 列
#                 input_name: [0]  # 用 0 填充 input_name 列
#             })
#             monthly_data = pd.concat([top_padding, monthly_data, bottom_padding], ignore_index=True)
#         if input_name == 'interviews_top200':
#             top_padding = pd.DataFrame({
#                 'mouth2': [0] * 4,  # 用 0 填充 'mouth2' 列
#                 input_name: [0] * 4  # 用 0 填充 input_name 列
#             })
#             bottom_padding = pd.DataFrame({
#                 'mouth2': [0],  # 用 0 填充 'mouth2' 列
#                 input_name: [0]  # 用 0 填充 input_name 列
#             })
#             monthly_data = pd.concat([top_padding, monthly_data, bottom_padding], ignore_index=True)
#         results2.append(monthly_data)
#     results4 = pd.concat(results2, ignore_index=True)
#     # results3 = pd.DataFrame({
#     #     'mouth': results4['mouth2'] # 这里填入你想要的初始数据
#     # })
#     results3[f'mouth{input_name}'] = results4['mouth2']
#     results3[input_name] = results4[input_name]
#     results2 = []
#
#
# results = []
# for ED_name in ED_list:
#     ED_path = '/Users/siyuanfang/Downloads/AA econ/research track/data/futures/3-Month SOFR Futures/'
#     ED_file = ED_path + ED_name
#     df_ED = pd.read_csv(ED_file)
#
#     # 确保 datetime 列是 datetime 类型
#     df_ED['datetime'] = pd.to_datetime(df_ED['ts_event'])
#
#     # 设置 datetime 列为索引
#     df_ED.set_index('datetime', inplace=True)
#     start_date = '2019-01-01'
#     end_date = '2024-07-31'
#     df_ED = df_ED[start_date:end_date]
#     # 选择每个月的1日的00:00:00的价格
#
#     monthly_start_prices = df_ED.resample('MS').first()
#
#     # 计算下个月的起始价格
#     next_month_prices = df_ED.resample('MS').last()
#
#     # 合并数据
#     monthly_data = monthly_start_prices[['close']].rename(columns={'close': 'price'})
#     monthly_data['next_price'] = next_month_prices['close']
#
#     # 计算价格变动
#     monthly_data['price_change'] = monthly_data['next_price'] - monthly_data['price']
#     monthly_data['month'] = monthly_data.index.to_period('M')
#     monthly_data['ED'] = ED_name
#     # 选择需要的列
#     result = monthly_data[['ED', 'month', 'price', 'price_change']]
#     results.append(result)
#
# df_new = pd.concat(results, ignore_index=True)
# df_new['mouthfomc_announcement'] = results3['mouthfomc_announcement']
# df_new['mouthbaha_powell_79'] = results3['mouthbaha_powell_79']
# df_new['mouthinterviews_top100'] = results3['mouthinterviews_top100']
# df_new['mouthinterviews_top200'] = results3['mouthinterviews_top200']
# df_new['mouthminutes_'] = results3['mouthminutes_']
#
#
# df_new["fomc_announcement"] = results3["fomc_announcement"]
# df_new["baha_powell_79"] = results3["baha_powell_79"]
# df_new["interviews_top100"] = results3["interviews_top100"]
# df_new["interviews_top200"] = results3["interviews_top200"]
# df_new["minutes_"] = results3["minutes_"]
# df_new.to_csv(main_folder + 'Sum_Variance.csv')
#
#
# ######============================== table C=========================================
# print('='*10+'ED2'+'='*10)
# df_ED2 = df_new[df_new['ED'] == 'ED2.csv']
# print(f"fomc_announcement: {df_ED2['price_change'].corr(df_ED2['fomc_announcement'])}")
# print(f"baha_powell_79: {df_ED2['price_change'].corr(df_ED2['baha_powell_79'])}")
# print(f"interviews_top100: {df_ED2['price_change'].corr(df_ED2['interviews_top100'])}")
# print(f"interviews_top200: {df_ED2['price_change'].corr(df_ED2['interviews_top200'])}")
# print(f"minutes_: {df_ED2['price_change'].corr(df_ED2['minutes_'])}")
# print('='*10+'ED3'+'='*10)
# df_ED2 = df_new[df_new['ED'] == 'ED3.csv']
# print(f"fomc_announcement: {df_ED2['price_change'].corr(df_ED2['fomc_announcement'])}")
# print(f"baha_powell_79: {df_ED2['price_change'].corr(df_ED2['baha_powell_79'])}")
# print(f"interviews_top100: {df_ED2['price_change'].corr(df_ED2['interviews_top100'])}")
# print(f"interviews_top200: {df_ED2['price_change'].corr(df_ED2['interviews_top200'])}")
# print(f"minutes_: {df_ED2['price_change'].corr(df_ED2['minutes_'])}")
# print('='*10+'ED4'+'='*10)
# df_ED2 = df_new[df_new['ED'] == 'ED4.csv']
# print(f"fomc_announcement: {df_ED2['price_change'].corr(df_ED2['fomc_announcement'])}")
# print(f"baha_powell_79: {df_ED2['price_change'].corr(df_ED2['baha_powell_79'])}")
# print(f"interviews_top100: {df_ED2['price_change'].corr(df_ED2['interviews_top100'])}")
# print(f"interviews_top200: {df_ED2['price_change'].corr(df_ED2['interviews_top200'])}")
# print(f"minutes_: {df_ED2['price_change'].corr(df_ED2['minutes_'])}")
# print('='*10+'SP500'+'='*10)
# df_ED2 = df_new[df_new['ED'] == 'SP500.csv']
# print(f"fomc_announcement: {df_ED2['price_change'].corr(df_ED2['fomc_announcement'])}")
# print(f"baha_powell_79: {df_ED2['price_change'].corr(df_ED2['baha_powell_79'])}")
# print(f"interviews_top100: {df_ED2['price_change'].corr(df_ED2['interviews_top100'])}")
# print(f"interviews_top200: {df_ED2['price_change'].corr(df_ED2['interviews_top200'])}")
# print(f"minutes_: {df_ED2['price_change'].corr(df_ED2['minutes_'])}")
#
# ######============================== table A&B=========================================
# for input_name in input_name_list:
#     print('='*10+input_name+'='*10)
#     for ED_name in ED_list:
#         print(f'ED neme: {ED_name}')
#         file = main_folder + input_name + ED_name
#         df = pd.read_csv(file)
#         # data_list.append((df['change']*100).values)
#         df['Publish_Times'] = pd.to_datetime(df['Publish_Times'])
#
#         # set datetime as index
#         df.set_index('Publish_Times', inplace=True)
#         start_date = '2019-01-01'
#         end_date = '2024-07-31'
#         df = df[start_date:end_date]
#
#         sum_abs = df['change'].abs().sum()
#         mean_abs = df['change'].abs().mean()
#
#         print(f"sum_abs: {sum_abs}")
#         print(f"mean_abs: {mean_abs}")


####===================================================================================================================
####================================================Figure 2 ==========================================================
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

ED_list = ["ED2.csv", "ED3.csv", "ED4.csv", "SP500.csv"]
main_folder = '/Users/siyuanfang/Downloads/AA econ/research track/code/new_data/'
input_name_list = ["fomc_announcement", "baha_powell_79", "interviews_top100","interviews_top200","minutes_"]
results2,results3 = [],[]
count = 0
results3 = pd.DataFrame()

for input_name in input_name_list:
    for ED_name in ED_list:
        file = main_folder + input_name + ED_name
        df = pd.read_csv(file)
        # data_list.append((df['change']*100).values)
        df['Publish_Times'] = pd.to_datetime(df['Publish_Times'])

        # 设置datetime为索引
        df.set_index('Publish_Times', inplace=True)
        start_date = '2019-01-01'
        end_date = '2024-07-31'
        df = df[start_date:end_date]
        df['change_abs'] = df['change'].abs()
        monthly_sum = df['change_abs'].resample('M').sum().fillna(0)
        # monthly_sum = monthly_sum.reindex(all_months, fill_value=0)
        monthly_sum = monthly_sum.combine_first(monthly_sum)
        # 将结果转换为DataFrame  .to_period('M')


        monthly_data = pd.DataFrame({
            'mouth2': monthly_sum.index.to_period('M'),
            input_name: monthly_sum.values
        }).reset_index(drop=True)
        if input_name == 'interviews_top100':
            top_padding = pd.DataFrame({
                'mouth2': [0] * 11,  # 用 0 填充 'mouth2' 列
                input_name: [0] * 11  # 用 0 填充 input_name 列
            })
            bottom_padding = pd.DataFrame({
                'mouth2': [0],  # 用 0 填充 'mouth2' 列
                input_name: [0]  # 用 0 填充 input_name 列
            })
            monthly_data = pd.concat([top_padding, monthly_data, bottom_padding], ignore_index=True)
        if input_name == 'interviews_top200':
            top_padding = pd.DataFrame({
                'mouth2': [0] * 4,  # 用 0 填充 'mouth2' 列
                input_name: [0] * 4  # 用 0 填充 input_name 列
            })
            bottom_padding = pd.DataFrame({
                'mouth2': [0],  # 用 0 填充 'mouth2' 列
                input_name: [0]  # 用 0 填充 input_name 列
            })
            monthly_data = pd.concat([top_padding, monthly_data, bottom_padding], ignore_index=True)
        monthly_data['ED'] = ED_name
        results2.append(monthly_data)
    results4 = pd.concat(results2, ignore_index=True)
    # results3 = pd.DataFrame({
    #     'mouth': results4['mouth2'] # 这里填入你想要的初始数据
    # })
    results3[f'mouth{input_name}'] = results4['mouth2']
    results3[input_name] = results4[input_name]
    results3['ED'] = results4['ED']
    results2 = []
# df_new = pd.concat(results3, ignore_index=True)
results3.to_csv(main_folder + 'Overtime_Sum_Variance.csv')

plot_name_list = ["FOMC Announcements", "Fed Chair Speeches", "Interviews(Top100)","Interviews(Top200)","Minutes"]
for k in range(5):
    results3[plot_name_list[k]] = results3[input_name_list[k]]

fig, axes = plt.subplots(2, 2, figsize=(9, 10), tight_layout=True)
for i, ax in enumerate(axes.flat):  # 展平子图数组以便迭代
    print(i)
    # ax.hist(data_list[i], bins=15, color='skyblue', edgecolor='black')
    ed_data = results3[results3['ED'] == ED_list[i]]
    for col in plot_name_list:
        ed_data['Datetime'] = ed_data['mouthfomc_announcement'].dt.to_timestamp()
        ed_data[f'rolling{col}'] = ed_data[[col]].rolling(window=6).sum()
        ax.plot(ed_data['Datetime'], ed_data[f'rolling{col}'], label=col)
    # title = ED_list[i][:-4]
    ax.set_title(ED_list[i][:-4])
    if i == 0:
        ax.legend()

    # ax.set_title(titles[i])  # 设置标题
plt.tight_layout()
plt.show()
# for ed in ED_list:
#     # 筛选出当前 ED 的数据
#     ed_data = results3[results3['ED'] == ed]
#
#     # 设置折线图
#     plt.figure(figsize=(10, 6))  # 设置图形大小
#
#     # 绘制5条折线图，对应 'col1' 到 'col5'
#     for col in input_name_list:
#         ed_data['Datetime'] = ed_data['mouthfomc_announcement'].dt.to_timestamp()
#         ed_data[f'rolling{col}'] = ed_data[[col]].rolling(window=6).sum()
#         plt.plot(ed_data['Datetime'], ed_data[f'rolling{col}'], label=col)  # x轴用 datetime，y轴用列数据
#
#     # 添加图例、标题、坐标轴标签、网格
#     plt.legend()
#     plt.title(f'Rolling-Window Plot for ED: {ed}')
#     plt.xlabel('Datetime')
#     plt.ylabel('Values')
#     plt.grid()
#     plt.show()

# titles = ['FOMC Announcement effects, ED2', 'Fed Chair effects, ED2', 'Fed Presidents effects(100), ED2',
#           'FOMC Announcement effects, ED4', 'Fed Chair effects, ED4', 'Fed Presidents effects(100), ED4',
#           'FOMC Announcement effects, SP 500', 'Fed Chair effects, SP 500', 'Fed Presidents effects(100), SP 500']
#
# # 创建绘图
# fig, axes = plt.subplots(3, 3, figsize=(9, 10), tight_layout=True)  # 2 行 3 列子图
#
# # 遍历数据并绘制直方图
# for i, ax in enumerate(axes.flat):  # 展平子图数组以便迭代
#     ax.hist(data_list[i], bins=15, color='skyblue', edgecolor='black')
#     ax.set_title(titles[i])  # 设置标题
#     # ax.set_xlabel('Value')  # 设置X轴标签
#     # # ax.set_ylabel('Frequency')  # 设置Y轴标签
#
# # 优化布局并显示
# plt.tight_layout()
# plt.show()