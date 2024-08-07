# Exercise 03. 달린 시간 계산하기

# 입력을 적절한 자료형으로 변환하는 방법

import math

def run_timing():
  record = []
  while True:
    t = input("Enter 10 km run time:")
    if t.isdigit():
      record.append(int(t))
    elif not t :
      break;
  
  if not record:
    return 
  
  print(record)
  print(f"Average of { sum(record) / len(record)}, over {len(record)} runs")


run_timing()

# Decimal 사용하기.
from decimal import *

getcontext().prec = 1
print(f"{Decimal(0.1) + Decimal(0.2)}")
print(f"{0.1 + 0.2}")