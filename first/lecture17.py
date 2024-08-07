
# 17강. 파괴적 연산과 비파괴적 연산

a = 10
print(a)

b = "a b c"

b.upper()
print(b)
b.lower()
print(b)

c = "   안녕   하세요  \t\n\n   "
print(c)
print(c.strip())

# c.find()

# + 연산자: 피연산자를 바꾸지 않음
# 비파괴적이다
# split, format, upper, lower 함수도 비파괴적이다.


#  = 연산자: 피연산자를 바꿈!
# 파괴적이다.



# find함수, in 연산자
print("안녕하세요".find("안녕"))
print("안녕" in "안녕하세요")

# format 함수 고급
# 정수 - 특정 칸 만큼 출력
print("{:5d}".format(52))
print("{:05d}".format(52))

print("{:5d}".format(-52))
print("{:=5d}".format(-52))

print("{:+5d}".format(52))
print("{:=+5d}".format(52))

# 부동소수점
print("{:5.1f}".format(52.463)) # 반올림이 자동으로 일어남
print("{:.1f}".format(52.463)) # 반올림이 자동으로 일어남

