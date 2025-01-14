# # ##===================================old version not work=======================================================
# from pytube import YouTube
# from tqdm import tqdm
# import os
#
# url = 'https://www.youtube.com/watch?v=3xHmoAPpSuc'
# yt = YouTube(url)
# print(f'Downloading: {yt.title}')
# # audio_stream = yt.streams.filter(only_audio=True).first()
# audio_stream = yt.streams.filter(only_audio=True)
# title = yt.title
# new_title = title.replace(':','-')
# filename = f'{new_title}.mp3'
# # 定义进度条
# pbar = tqdm(total=audio_stream.filesize, unit='B', unit_scale=True, desc=filename, ncols=80)
# # 定义进度回调函数
# def on_progress(stream, chunk, bytes_remaining):
#     pbar.update(len(chunk))
# # 设置进度回调函数
# yt.register_on_progress_callback(on_progress)
# # 下载音频流
# audio_stream.download(filename=filename)
# pbar.close()
# print('下载完成！')

##=========================================audio========================================================================
from pytubefix import YouTube
from pytubefix.cli import on_progress

import pandas as pd
import glob
import os

path = 'D:/AA econ/research track/data/Youtube CNBC Fed11/*.csv'
xlsx_files = glob.glob(path)
for file in xlsx_files:
    data = pd.read_csv(file,encoding='unicode_escape')#powell
    #data = pd.read_csv(file)#for else
    urls = data.iloc[:, 1]
    output_path1 = file.replace('Youtube CNBC Fed11/', 'audio/')
    print(output_path1)
    output_path = output_path1.replace('.csv','/')
    print(output_path)
    if not os.path.exists(output_path):
        os.makedirs(output_path)
    # output_path = 'D:/AA econ/research track/data/for bert/James Bullard/'
    for url in urls:
        # yt = YouTube(url, use_oauth=True)
        yt = YouTube(url, on_progress_callback = on_progress)
        print(yt.title)
        filetitle = yt.title.replace('?','-')
        ys = yt.streams.get_audio_only()
        ys.download(mp3=True, output_path=output_path,filename=filetitle)  # pass the parameter mp3=True to save in .mp3

# ####==========================================try example==========================================
#
# from pytubefix import YouTube
# from pytubefix.cli import on_progress
#
# url = "https://www.youtube.com/watch?v=IWc5pc5KaUo"
#
# yt = YouTube(url, use_oauth=True)
# print(yt.title)
#
# ys = yt.streams.get_audio_only()
# ys.download(mp3=True)


# ##=========================================audio========================================================================
#
#
# from pytubefix import YouTube
#
# yt = YouTube('https://www.youtube.com/watch?v=3xHmoAPpSuc')
#
# # caption = yt.captions.get_by_language_code('en')
# # caption.save_captions("captions_mark2.txt")
#
# subtitles = yt.captions
#
# print(subtitles)

