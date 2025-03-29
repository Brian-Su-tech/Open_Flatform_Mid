import requests
from bs4 import BeautifulSoup
import csv

url = 'https://www.truemovie.com'
web = requests.get(url)                        # 取得網頁內容
web.encoding = 'big5'                          # 設定編碼為big5

soup = BeautifulSoup(web.text, "html.parser")  # 轉換成標籤樹
table = soup.find('table', {'id': 'table123'})

rows = table.find_all('tr')                    # 找到所有tr

data = []                                      # 建立一個空list來儲存電影資料

for row in rows:                               #取得每個row的電影資訊
    cols = row.find_all('td')
    # 不要讀到換行符號和'.'
    cols = [col.text.replace('\n', '').replace('.', '').strip() for col in cols]
    data.append(cols)

tadadate = data[10]
data.remove(data[10])

with open('static.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(tadadate)                 # 寫入排行日期
    writer.writerow(['電影排名', '電影名稱', '電影票房'])
    for row in data:
        writer.writerow(row)