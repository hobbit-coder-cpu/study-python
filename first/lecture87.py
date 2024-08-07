# 87강. 모듈을 읽어 들이는 기본 문법

# 카테고리로 구분하기 위해서 
## 클래스: "객체"라는 주어로 묶는 방법
## 모듈: "관심사"를 기반으로 묶는 방법

#  3가지 방법


# import 모듈
#  모듈을 식별자로 읽어들임
import math
math.sin(1)

# import 모듈 as 모
# 모 라는 식별자로 읽어들임
import math as m
m.sin(1)

# from 모듈 import 변수, 함수, 클래스
# 변수 함수 클래스를 식별자로 읽어들임
from math import sin, cos, tan
sin(1)
tan(2)




