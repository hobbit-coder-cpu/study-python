# Exercise 08. 문자열 정렬하기

# 문자열도 시퀀스, 시퀀스(리스트 또는 튜플등)를 사용할 수 있는 곳이라면 문자열도 사용 가능

def strsort(text):
    result = sorted(text)
    print(type(result))
    return "".join(result)


print(strsort("cba"))