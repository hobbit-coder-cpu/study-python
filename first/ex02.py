# Exercise 02. 숫자 더하기

# 함수 매개변수로 숫자 시퀀스* 받는 방법

def mysum(*list, myN=12):
  sum = 0
  for i in list:
    sum += i
  
  return sum

print(mysum(*[1,2,3]))
print(mysum(1, 2, 3))
print(mysum(10, 20, 30, 40, 50, 60))
print(mysum(1,2,3,myN=20))
