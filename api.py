import requests
import csv

web = requests.get('https://tcgbusfs.blob.core.windows.net/dotapp/news.json')
jdata = web.json()

update_time = jdata['updateTime']

data = []

for item in jdata['News']:
    row = [item['chtmessage'], item['starttime'], item['endtime'], item['content']]
    data.append(row)

with open('api.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['更新時間', update_time])       
    writer.writerow(['交通資訊', '開始時間', '結束時間', '內容'])
    for row in data:
        writer.writerow(row)