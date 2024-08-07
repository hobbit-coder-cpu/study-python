# 55강. 메모리 구조(2): global 키워드

# 전역 위치에서 a, b 라는 변수 생성
a = 10
b = [1, 2, 3, 4]

def function():
    # 함수 내부에서 a, b라는 변수 생성
    a = 20
    b = [5, 6, 7, 8]
    print(a) # 20
    print(b) # [5, 6, 7, 8]

function()

def function_unbound_local_error():
    # 함수 내부에서 a, b라는 변수 생성
    print(a) # 20
    print(b) # [5, 6, 7, 8]
    a = 20
    b = [5, 6, 7, 8]

function_unbound_local_error()


print(a)
print(b)

def global_function():
    global a, b # 함수 내부에서 변수를 생성하지 않는다. 따라서 아래의 변수는 가장 가까운 위치(전역 위치)의 변수를 의미
    a = 20
    b = [5, 6, 7, 8]
    
global_function()
print(a)
print(b)