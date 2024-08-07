# 20강. if 조건문


# if 조건:
#     문장
#     문장
#     문장
#     문장

raw_input = int(input("정수를 입력해주세요: "))

if raw_input > 0:
    print("양수입니다.")
    
from pytz import timezone
from datetime import datetime

today = datetime.now(timezone("Asia/Seoul"))

m = today.month
    
