import requests
from bs4 import BeautifulSoup

# 영화 개봉 여부 알아보는 크롤링


# 서버에 cgv 홈페이지 정보 요청

url = "http://www.cgv.co.kr/common/showtimes/iframeTheater.aspx?areacode=01&theatercode=0013&date=20190605"
# areacode => 서울 theatercode =0013 => 용산아이파크몰 data => 날짜

response = requests.get(url)        # 서버에 cgv 홈페이지 정보 요청
html = response.text
soup = BeautifulSoup(html, 'html.parser')



# 파싱

movies_name = []    

movie = soup.find_all('div' , {'class' : "info-movie"})
# soup에서 모든 div를 찾되 class는 info-movie 인것만 모두 찾기

for m in movie:
    movies_name.append(m.find('strong').text.strip())

# 영화 제목은 strong 태그로 쌓여있으므로 strong 태그 찾아 text(한글)만 추출하고 양쪽 여백 제거

#print(movies_name)

for movie in movies_name:           # 내가 찾는 영화인 알라딘이라는 글자가 리스트 안에 있으면 
    if('알라딘' in movie):
        print('개봉했습니다.')
        
    



