import pandas as pd


ED_list = ["MP1.csv","ED2.csv", "ED3.csv", "ED4.csv", "SP500.csv"]
input_name_list = ['baha_powell_79']
main_folder = '/Users/siyuanfang/Downloads/AA econ/research track/code/new_data/'

# ED_list = ["ED3.csv"]
for input_name in input_name_list:
    result_df = pd.DataFrame()
    output_file = main_folder + 'reg_'+ input_name + '.csv'
    for ED_name in ED_list:


        # df_file = main_folder + input_name + csv
        file = main_folder + input_name + ED_name
        df = pd.read_csv(file)
        result_df[ED_name.split('.')[0]] = df['change']
    result_df.to_csv(output_file, index=False)