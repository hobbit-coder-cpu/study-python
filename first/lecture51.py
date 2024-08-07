# 51강. 가변 매개변수

def print_n_times(times, lst):
    for i in range(times):
        for elm in lst:
            print(elm)

print_n_times(2, ["안녕", "하세요"])


# 전개 연산자 적용시, <class 'tuple'>
def print_n_times2(times, *lst):
    
    print(type(lst))
    
    for i in range(times):
        for elm in lst:
            print(elm)

a = ["안녕", "하세요", "정원씨"]
print_n_times2(2, *a)


# 키워드 매개변수
def print_n_times3(*lst, times):
        
    print(type(lst))
    
    for i in range(times):
        for elm in lst:
            print(elm)

b = ["안녕", "반가워", "정원씨"]
print_n_times3(*b, times=2)    