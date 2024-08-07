# 63강. 람다, key 키워드 매개변수

def power1(숫자):
    return 숫자 ** 2

power2 = lambda 숫자: 숫자 ** 2

def is_odd1(숫자):
    return 숫자 % 2 == 1

is_odd2 = lambda 숫자: 숫자 % 2 == 0