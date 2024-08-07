import hellomodule

print(hellomodule.a)
print(hellomodule.b())


from hellomodule import Circle

c = Circle(10)
print(c.area)
print(c.circumference)

# 해당 파일이 모듈로써 실행되는지 메인으로써 실행되는지 확인하는 변수
print("main.py")
print(__name__) 

# 1.폴더를 모듈로 읽어들이는 방법
# -> 폴더 내부에 __init__.py 생성
import school

# print(school.a)
# print(school.b)


# 2. 모듈 파일을 읽어들이는 방법
from school.student import Student
from school.studentlist import StudentList

sl = StudentList()
sl.append(Student(100))
sl.append(Student(90))
sl.append(Student(80))

sl.print()

# 1, 2번 방법 모두를 사용하는 방법
from school import *
print(Student)

# print(a)
