import requests
from bs4 import BeautifulSoup

# 네이버 영화 순위 크롤링

req = requests.get('https://movie.naver.com/movie/sdb/rank/rmovie.nhn')
html = req.text
parse = BeautifulSoup(html, 'html.parser')

#print(parse)

tem = parse.find_all("div" , {"class" : "tit3"})
# soup에서 모든 div를 찾되 class는 tit3 인것만 모두 찾기 
#print(tem)

movie = []

for t in tem:
    movie.append(t.find('a').text)
# a 태그로 쌓여있으므로 a 태그 찾아 text(한글)만 추출
#print(movie)


for index, m in enumerate(movie):
    print('%3d위 : %s'%(index+1, m))
