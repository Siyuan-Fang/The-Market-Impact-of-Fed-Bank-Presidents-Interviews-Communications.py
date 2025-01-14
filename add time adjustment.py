import glob
import pandas as pd
import pytz




path = 'D:/AA econ/research track/data/Youtube CNBC Fed1/*.xlsx'
xlsx_files = glob.glob(path)

for file in xlsx_files:
    df = pd.read_excel(file)
    pacific = pytz.timezone('US/Pacific')
    df['Publish_Times'] = df['Publish_Times'].dt.tz_localize(pacific, ambiguous='infer')
    df = df.sort_values(by=df.columns[0], ascending=False)
    filenew = file[:47] + '1' + file[47:]
    filenew = filenew.replace('.xlsx', '.csv')
    df.to_csv(filenew, index=False, encoding='utf-8-sig')
    print('done!!!!!!!')