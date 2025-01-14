import scrapetube
import pandas as pd
#videos = scrapetube.get_channel("UCCezIgC97PvUuR4_gbFUs5g")
#videos = scrapetube.get_channel("UCiaba-DmYJacphj7r7Knrwg")
#循环间断
'''for index, video in enumerate(videos):
    if index >=2:
        break
    print(video)
    print(type(video))'''

videos = scrapetube.get_channel("UCrp_UI8XtuYfpiqluWLD7Lw")
data = {'URL': [],'title':[],'desc':[], 'view':[], 'time':[], 'length':[]}
cycle = 0
for video in videos:
    ID, title, desc, view, length = None, None, None, None, None
    try:
        #ID = 'https://www.youtube.com/watch?v=' + video['videoId']
        ID = video['videoId']
    except:
        pass
    data['URL'].append(ID)
    try:
        title = video["title"]["runs"][0]['text']
    except:
        pass
    data['title'].append(title)
    try:
        desc = video['descriptionSnippet']['runs'][0]["text"]
    except:
        pass
    data['desc'].append(desc)
    try:
        view = video['viewCountText']['simpleText'][:-6]
    except:
        pass
    data['view'].append(view)
    try:
        time = video['publishedTimeText']['simpleText']
    except:
        pass
    data['time'].append(time)
    try:
        length = video['lengthText']['simpleText']
    except:
        pass
    data['length'].append(length)
    cycle = cycle + 1
    print(cycle)
df = pd.DataFrame(data)
df.to_excel('D:/AA econ/research track/data/output1.xlsx', index=False)

#print(type(videos))
print('done!!!!!!!!!!!!!!!!!!!!!!!')