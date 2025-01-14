# import os
#
# folder_path = 'D:/AA econ/research track/data'  # Replace with your folder path
#
# for dirpath, dirnames, filenames in os.walk(folder_path):
#     for filename in filenames:
#         if filename.endswith('.R'):
#             print(os.path.join(dirpath, filename))

"""This module contains all non-cipher related data extraction logic."""

from pytubefix import Playlist, YouTube
import pytubefix
yt = YouTube('https://www.youtube.com/watch?v=4WywwDmY66A')
A = pytubefix.extract.publish_date(yt.watch_html)
