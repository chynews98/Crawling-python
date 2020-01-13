# cgv 아이맥스관 유무

# 특정 날짜에 아이맥스관 개봉 유무

import requests
from bs4 import BeautifulSoup
from apscheduler.schedulers.blocking import BlockingScheduler
from my_email import email
import time
import sys
idd = '네이버이메일'
pw = '네이버비번'


date = '20191220'

def crawling_imax():
    
    print(str(time.localtime().tm_hour) + ":" + str(time.localtime().tm_min) + ":" + str(time.localtime().tm_sec))
    
    # 서울 용산
    url = 'http://www.cgv.co.kr/common/showtimes/iframeTheater.aspx?areacode=01&theatercode=0013&date='+date
    
    response = requests.get(url)
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    
    col_times = soup.find_all('div',{'class':'col-times'})   # 영화 블럭별로 분리
    for each_block in col_times:
        if 'IMAX' in each_block.text:            # 영화 블럭 중에 내가 찾는 영화 블럭 선택
            movie_name = each_block.find('strong').text.strip()  # 해당 영화 제목
            print(movie_name , '아이맥스관 개봉') 
            content = movie_name + ' IMAX 개봉했습니다'
            email(idd, pw, 'IMAX 개봉', content)
            sched.shutdown()   # 스케줄러 종료
            sys.exit()
                
        
 # 스케줄링 설정

sched = BlockingScheduler()
# 예약방식 interval로 설정, 10초마다 한번 실행
sched.add_job(crawling_imax, 'interval', seconds=3)
# 예약방식 cron으로 설정, 각 5배수 분의 10, 30초마다 실행
# ex) (5분 10, 30초), (10분 10, 30초), (15분 10, 30초)
#sched.add_job(exec_cron, 'cron', minute='*/5', second='10, 30')
# 스케줄링 시작
sched.start()       