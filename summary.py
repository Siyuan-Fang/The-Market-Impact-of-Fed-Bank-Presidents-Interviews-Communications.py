#####==============================================match stance_index========================================
import pandas as pd
import re
import glob
import os

# Function to clean text by removing punctuation
def clean_text(text):
    return re.sub(r'[^\w\s]', '', text).lower().replace('_', '').lower()

path1 = '/Users/siyuanfang/Downloads/AA econ/research track/data/Youtube CNBC Fed11ED2S/*.csv'
path2 = '/Users/siyuanfang/Downloads/AA econ/research track/data/negative score/output/*.csv'
xlsx_files1 = glob.glob(path1)
xlsx_files2 = glob.glob(path2)
# df_Goolsbee = pd.read_csv('D:/AA econ/research track/data/Youtube CNBC Fed11/Goolsbee.csv')
for file1 in xlsx_files1:
    for file2 in xlsx_files2:
        file_name2 = os.path.basename(file2)
        # file_name2 = file_name2.replace('-1','')
        if file_name2 == os.path.basename(file1):
            # Read Excel files
            df1 = pd.read_csv(file1)
            df2 = pd.read_csv(file2)

            # Assuming the sentences are in a column named 'sentence'
            # df1['cleaned'] = df1['title'].apply(clean_text)
            df2['cleaned'] = df2['file'].apply(clean_text)
            print(df1['cleaned'])
            print(df2['cleaned'])

            # Create a new column 'match' in df1
            df1['negative_index'] = df1['cleaned'].apply(lambda x: df2.score[df2['cleaned'] == x].tolist()[0] if x in df2['cleaned'].values else None)
            filenew = file1[:77] + 'S' + file1[77:]
            df1.to_csv(filenew, index=False, encoding='utf-8-sig')

######==========================================merge excels=========================
