# 82강. 캡슐화

# 객체를 사용하는 사람이 허튼짓 못하게 변수와 함수를 숨기는 작업
# 인스턴스 변수와 인스턴스 함수 앞에 __(언더바 2개)를 붙이면

class Circle:
    def __init__(self, 반지름):
        if 반지름 < 0:
            raise TypeError("반지름은 0 이상이어야 합니다.")
        self.__반지름 = 반지름
        self.__파이 = 3.14
        
    @property
    def 빤지름(self):
        return self.__반지름
    
    @빤지름.setter
    def 빤지름(self, value):
        self.__반지름 = value
        
    @property
    def 뚤레(self):
        return 2 * self.__파이 * self.__반지름
    
    @property
    def 넓삐(self):
        return self.__파이 *(self.__반지름 ** 2)
    
    def get_반지름(self):
        return self.__반지름
    def set_반지름(self, 반지름):
        self.__반지름 = 반지름
    def 둘레(self):
        return 2 * self.__파이 * self.__반지름
    def 넓이(self):
        return self.__파이 *(self.__반지름 ** 2)


circle = Circle(10)
# print(circle.__반지름) # 에러
circle.__반지름 = -10 # 다름 변수
print(circle.둘레())
print(circle.넓이())

# 프로퍼티 만들기
circle.빤지름 = 20
print(circle.빤지름)
print(circle.뚤레)
print(circle.넓삐)
