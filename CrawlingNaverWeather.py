import requests
from bs4 import BeautifulSoup

# 네이버 날씨 크롤링

url = "https://weather.naver.com/rgn/cityWetrCity.nhn?naverRgnCd=09140104"

response = requests.get(url)
html = response.text
soup = BeautifulSoup(html, 'html.parser')

tem = soup.find_all("div", {"class" : "cell"})
# soup에서 모든 div를 찾되 class는 cell 인것만 모두 찾기 
#print(tem)

# 기온 파싱

print("오늘 오전 기온은 ", tem[0].find('span' , {"class" : "temp"}).text, "도입니다")
# tem은 리스트이지만 원소가 하나짜리로 처리되어있으므로 인덱싱 0 으로 접근
## tem[0]에서 span을 찾되 class는 temp인것만 모두 찾기
# .text로 한글만 추출


# 강수량 파싱

weather = tem[0].find('li' , {"class" : "info"}).text
# tem[0]에서 모든 li를 찾되 class는 info 인것만 모두 찾기
#print(weather)
weather = weather.split("강수확률")

print("날씨는" , weather[0], "이고 강수 확률은", weather[1], "입니다\n")

#===============================================================================================



print("오늘 오후 기온은 ", tem[1].find('span' , {"class" : "temp"}).text, "도입니다")

weather = tem[1].find('li' , {"class" : "info"}).text
#print(weather)
weather = weather.split("강수확률")     # '강수확률'이라는 키워드를 기준으로 문자열 자르기

print("날씨는" , weather[0], "이고 강수 확률은", weather[1] , "입니다")

