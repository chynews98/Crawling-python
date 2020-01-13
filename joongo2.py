#중고나라 매물 (최종본)

import requests
from bs4 import BeautifulSoup
import time
from apscheduler.schedulers.blocking import BlockingScheduler
from my_email import email

idd = '네이버 이메일'
pw = '네이버 비번'

user_input = '책'

URL = 'https://m.cafe.naver.com/joonggonara'



def crawling_joongo():
    item = []
    
    result = requests.get(URL)
    result = result.text
    soup = BeautifulSoup(result, 'html.parser')
    
    result = soup.find_all('li', {'class' :'board_box'})  
    # 글 목록만 블록잡음. 한페이지에 매물 20개 뜨니까 20개 블록있음
    
    for block in result:
        title = block.find('strong',{'class':'tit'}).text.strip()  # 매물 제목 파싱
        if user_input in title:   # 찾는 매물이 올라왔다면
            link = 'https://m.cafe.naver.com/' + block.find('a').get('href')  # 링크 파싱
            content = title + ' ' + link
            print(content)
            item.append(content)   # 매물 제목이랑 링크 합쳐서 한줄로 이어줌
    
    if len(item) > 0 :   # 찾는 매물이 1개 이상 있다면
        complete = ''
        for i in item:   # 보기 좋게 아래로 내려줌
            complete += i
            complete += '\n'
    
        email(idd, pw, '새 매물이 올라왔습니다', complete)
        
    
    print(str(time.localtime().tm_hour) + ":" + str(time.localtime().tm_min) + ":" + str(time.localtime().tm_sec))
        


  

# 스케줄링 설정

sched = BlockingScheduler()
# 예약방식 interval로 설정, 10초마다 한번 실행
sched.add_job(crawling_joongo, 'interval', seconds=3)
# 예약방식 cron으로 설정, 각 5배수 분의 10, 30초마다 실행
# ex) (5분 10, 30초), (10분 10, 30초), (15분 10, 30초)
#sched.add_job(exec_cron, 'cron', minute='*/5', second='10, 30')
# 스케줄링 시작
sched.start()