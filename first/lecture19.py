
# 19강. 불 자료형


True
False

a = 10
b = 10

if a > 0 and a < 20:
    print(f"a is {a}")
    
if a is b:
    print("eq")
    
# 날짜 / 시간 구하는 방법

import datetime
import pytz
#pip install pytz

seoul = pytz.timezone("Asia/Seoul")
now = datetime.datetime.now(seoul)
print(now)
now2 = datetime.datetime.now()
print(now2)
    
    
