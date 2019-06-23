import requests
from bs4 import BeautifulSoup


# 멜론 탑 50 크롤링

RANK = 50

header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Trident/7.0; rv:11.0) like Gecko'}
req = requests.get('https://www.melon.com/chart/index.htm', headers = header)
html = req.text
parse = BeautifulSoup(html, 'html.parser')

titles = parse.find_all("div", {"class": "ellipsis rank01"})
# soup에서 모든 div를 찾되 class는 ellipsis rank01 인것만 모두 찾기 (노래 제목)
singers = parse.find_all("div", {"class": "ellipsis rank02"})
# soup에서 모든 div를 찾되 class는 ellipsis rank02 인것만 모두 찾기 (가수)

#print(titles, songs)

title = []
si = []

for t in titles:
    title.append(t.find('a').text)
    # 노래는 a 태그로 쌓여있으므로 a 태그 찾아 text(한글)만 추출
for s in singers:
    si.append(s.find('a').text)
    # 가수는 a 태그로 쌓여있으므로 a 태그 찾아 text(한글)만 추출

for i in range(1,RANK+1):
    print('%3d위: %s - %s'%(i, title[i], si[i]))


