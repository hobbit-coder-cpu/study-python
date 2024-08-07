# 81강. 특수한 이름의 함수, 값 객체

# 클래스 정의
class Student:        
    def __init__(self, name, kor, eng, math, sci): # 생성자
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
        
    def __eq__(self, rhs): # ==
        if type(rhs) == Student:
            return self.sum() == rhs.sum()
        else:
            raise "같은 자료형을 비교해주세요"
        
    def __ne__(self, rhs): # !=
        return not self.__eq__(rhs)
    
    def __ge__(self, rhs): # >=
        return self.sum() >= rhs.sum() 
    
    def __str__(self):
        return f"{self.name}\t{self.sum()}\t{self.average()}"
    

class StudentList:
    def __init__(self):
        self.students = []
        
    def __add__(self, rhs):
        self.students.append(rhs)
        return self       
    
    def print(self):
        print("이름", "총점", "평균", sep='\t')
        for s in self.students:
            s.print()
            
    def __str__(self) -> str:
        output = "이름\t총점\t평균\n"
        for s in self.students:
            output += f"{str(s)}\n"
        return output


# 요구사항1. 클래스 인스턴트에 대한  비교 연산자를 사용하게 해달라: __eq__, __ge__ ... 구현
s1 = Student("a", 10, 20, 30, 40)
s2 = Student("b", 10, 20, 25, 40)
s3 = Student("c", 1, 2, 3, 4)

print(s1 == s2)
# print(s1 == 10)
print(s1 != s2)
print(s1 >= s2)

# 요구사항2. + 연산자를 사용하게 해달라: __add__ 구현
sl = StudentList()
sl += s1
sl += s2
sl += s3
sl.print()
print()

# 요구사항3. print() 에 객체를 넣어 사용할수 있도록 해달라: __str__ 구현
print("print(s1)")
print(s1)
print("print(sl)")
print(sl)


# 값 객체
class CmLength:
    def __init__(self, cm) -> None:
        if cm < 0:
            raise "길이는 0이상으로 지정해야하 합니다."
        self.length = cm
    
    def __add__(self, value):
        pass
