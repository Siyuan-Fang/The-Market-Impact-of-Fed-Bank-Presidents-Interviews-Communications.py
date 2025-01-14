import pandas as pd
import os

folder_path = 'D:/AA econ/research track/data/bert/C/'
folder_path2 = 'D:/AA econ/research track/data/bert/CNBC Fed/'
subfolders = [f for f in os.listdir(folder_path) if os.path.isdir(os.path.join(folder_path, f))]
# Step 5: Save subfolder names as variables (if needed)
for i, subfolder in enumerate(subfolders):
    input_folder = os.path.join(folder_path, subfolder)
    output_folder = os.path.join(folder_path2, subfolder)
    csv_files = [f for f in os.listdir(input_folder) if f.endswith('.csv')]
    titles, stance_indexs = [], []
    for file in csv_files:
        input_file = os.path.join(input_folder, file)
        df = pd.read_csv(input_file)
        stance_index = df.iloc[:, 2].mean()
        title = file.replace('.csv', '')
        titles.append(title)
        stance_indexs.append(stance_index)
    new_df = pd.DataFrame({'title':titles,'stance_index':stance_indexs})
    # print(new_df)
    # new_df.to_xlsx(output_folder, index=False)
    output_file = output_folder + '.csv'
    print(output_file)
    new_df.to_csv(output_file, index=False,encoding = 'utf-8-sig')