
#####==========================================all the folder=====================================
# import glob
# import pandas as pd
# from datetime import datetime
# from pytube.exceptions import RegexMatchError
# from pytube.helpers import regex_search
# from pytube import YouTube
#
# def add_element(lst):
#     return ['https://www.youtube.com/watch?v=' + str(item) for item in VideoID]
#
# def publish_date1(watch_html: str):
#     try:
#         result = regex_search(
#             r"(?<=itemprop=\"datePublished\" content=\")\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}",
#             watch_html, group=0
#         )
#
#     except RegexMatchError:
#         return None
#     return result
# path = 'D:/AA econ/research track/data/Youtube CNBC Fed/*.xlsx'
# xlsx_files = glob.glob(path)
#
# for file in xlsx_files:
#     df = pd.read_excel(file)
#
#     VideoID = df['URL'].tolist()
#
#     URLs = add_element(VideoID)
#     Publish_times = []
#     for URL in URLs:
#         yt = YouTube(URL)
#         Publish_time = datetime.strptime(publish_date1(yt.watch_html), "%Y-%m-%dT%H:%M:%S")
#         Publish_times.append(Publish_time)
#
#     df['URL'] = URLs
#     df['Publish_Times'] = Publish_times
#     filenew = file[:47] + '1' + file[47:]
#     df.to_excel(filenew, index=False)
#     print('done!!!!!!!')


#####======================================Jerome Powell===============================================================
from pytubefix import Playlist, YouTube
import pytubefix
import pandas as pd
from datetime import datetime
def add_element(lst):
    return ['https://www.youtube.com/watch?v=' + str(item) for item in VideoID]

# yt = YouTube('https://www.youtube.com/watch?v=4WywwDmY66A')
# A = pytubefix.extract.publish_date(yt.watch_html)

df = pd.read_excel('D:/AA econ/research track/data/Youtube CNBC Fed/Jerome Powell.xlsx')

VideoID = df['URL'].tolist()

URLs = add_element(VideoID)
Publish_times = []
for URL in URLs:
    yt = YouTube(URL)
    try:
        Publish_time = pytubefix.extract.publish_date(yt.watch_html)
    except:
        Publish_time = 'NA'

    Publish_times.append(Publish_time)
    print(Publish_time)

df['URL'] = URLs

df['Publish_Times'] = Publish_times
filenew = 'D:/AA econ/research track/data/Youtube CNBC Fed1/Jerome Powell.xlsx'
df.to_excel(filenew, index=False)
print('done!!!!!!!')
##===============================================加太平洋时区=============================================
# import glob
# import pandas as pd
# import pytz
# path = 'D:/AA econ/research track/data/Youtube CNBC Fed1/*.xlsx'
# xlsx_files = glob.glob(path)
#
# for file in xlsx_files:
#     df = pd.read_excel(file)
#     df['Publish_Times'] = pd.to_datetime(df['Publish_Times'])
#     pacific = pytz.timezone('US/Pacific')
#     # df['Publish_Times'] = df['Publish_Times'].dt.tz_localize('UTC').dt.tz_convert(pacific)
#     df['Publish_Times'] = df['Publish_Times'].dt.tz_localize(pacific, ambiguous='infer')
#     filenew = file[:48] + '1' + file[48:]
#     filenew2 = filenew.replace('.xlsx','.csv')
#     df.to_csv(filenew2, index=False)
#     print('done!!!!!!!')
