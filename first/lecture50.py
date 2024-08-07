# 50강. 함수 매개변수 기본

# parameter: 함수 정의 때 넣은 변수
def print_3_times(s):
    if type(s) != str:
        print("WARN")

    print(s)
    print(s)
    print(s)
    
# argument: 함수 호출 때 넣은 값
print_3_times("안녕")



