# 13강. input() 함수와 자료형 반환

#input() 함수
i = input("입력해주세요: ")
print(i)

# 문자열 -> 숫자
print(type(int("52"))) # 정수
print(type(float("52.1231"))) # 부동소수점

# 숫자 -> 문자열
c = str(20)
print(type(c))