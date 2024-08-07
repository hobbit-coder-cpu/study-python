# 66강. 이터러블, 이터레이터, 제너레이터 함수 제너레이터 표현식
 
# "이터러블": 반복할 수 있는것 (반복문 뒤에 넣은 것)
#  Iterate + able
#  리스트, 튜플, 딕셔너리

# "이터레이터": 반복하는 녀석
# 이터러블을 만드는 방법중 하나
#  next(이터레이터): 내부 요소를 꺼낼수 있음
# Iterate + or

# 제너레이터
# 이터레이터를 만드는 방법 중 하나.
# 
# 제너레이터 표현식
r = range(1, 100 + 1)
gen = (
  i * i
  for i in r
)

print(gen)
print(type(gen)) # <class generator>


# 제너레이터 함수
def genFunc():
  for i in range(1, 100 + 1):
    yield i * i

# 제너레이터 = 제너레이터함수()
# next(제너레이터)


# 리스트 내포 vs 제너레이터 표현식 = 메모리 사용량의 차이 


# 이터레이터 클래스 
