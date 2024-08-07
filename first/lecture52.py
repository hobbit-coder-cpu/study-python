# 52강. 기본 매개변수

# 기본 매개변수
def test(a = 10, b = 20):
    print(a)

test()
test(20)

# 키워드 매개변수 기본 매개변수
test(a = 30)
test(a = 30, b = 100)


# 딕셔너리 매개변수
def function(*가변, **딕셔너리):
    pass
