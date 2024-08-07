# 80강. 클래스 문법 기본

# 클래스: 함수와 변수를 묶어 놓은 것
# -> 객체를 만들어내기 위한 설계도

# class class_name:
#  pass

# 클래스 정의
class Student:        
    # def __xx__ : 특별한 이름의 함수
    def __init__(self, name, kor, eng, math, sci): # 생성자
        self.name = name
        self.kor = kor
        self.eng = eng
        self.math = math
        self.sci = sci    
    
    def init(self, name, kor, eng, math, sci):
        self.name = name
        self.kor = kor
        self.eng = eng
        self.math = math
        self.sci = sci
        
    def sum(self):
        return self.kor + self.eng + self.math + self.sci
    
    def average(self):
        return self.sum() / 4
    
    def print(self):
        print(f"{self.name}\t{self.sum()}\t{self.average()}")


# 클래스 초기화 방법 #1
# s1 = student()
# student.init(s1, "jungwon",88, 87, 90, 84)


# # 클래스 초기화 방법 #2 - 선호
# s1.init("jungwon",88, 87, 90, 84)
# s1.sum()
# s1.average()

# 클래스 초기화 방법 (초기화 함수(__init__) 사용)
s2 = Student("jungwon",88, 87, 90, 84)
s2.print()


students = [
    Student("인성", 87, 88, 98, 95),
    Student("구름", 92, 98, 97, 98),
    Student("별이", 76, 96, 95, 90)
]

print("이름", "총점", "평균", sep='\t')
for s in students:
    s.print()
    
# 클래스 이름 짓기: 대문자 캐멀케이스
