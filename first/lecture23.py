
# 23강. elif else 구문

number = int(input("정수 입력: "))

if number % 2 == 0:
    print("짝수")
if number % 2 != 0:
    print("홀수")

if number % 2 == 0:
    print("짝수")
else:
    print("홀수")

from pytz import timezone
from datetime import datetime

today = datetime.now(timezone('Asia/Seoul'))

if today.hour < 12:
    print("오전")
else:
    print("오후")
    
number2 = int(input("정수 입력:"))
if number > 0:
    print("양수")
elif number == 0:
    print("0")
else:
    print("음수")

