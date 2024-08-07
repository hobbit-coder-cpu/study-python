# 67강. 가독성과 유지보수성

PI = 3.141582

def 숫자입력():
  number_input_a = input(">  숫자 입력:")
  return float(number_input_a)


def 둘레구하기(radius):
  return 2 * PI * radius

def 넓이구하기(radius):
  return PI * radius * radius

반지름 = 숫자입력()
print(둘레구하기(반지름))
print(넓이구하기(반지름))


