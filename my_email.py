

import smtplib
from email.mime.text import MIMEText


def email(idd, pw, title, contents):
    
    msg = MIMEText(contents, _charset = 'euc-kr')
    msg['Subject'] = title
    msg['From'] = idd
    msg['To'] = idd
    
    naver_server = smtplib.SMTP_SSL('smtp.naver.com',465)
    naver_server.login(idd,pw)
    naver_server.sendmail(idd,[idd], msg.as_string()) # 보내는 사람, [받는 사람]
    naver_server.quit()
