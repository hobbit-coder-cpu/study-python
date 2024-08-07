# 85강. 상속과 컴포지션

# 상속
class Student:
  def __init__(self, m) -> None:
    self.__math = m
  
  @property
  def math(self):
    return self.__math

class StudentList1(list):
  def __init__(self) -> None:
    pass
  def append(self, elem):
    if type(elem) != Student:
      raise "Student를 전달해주세요"
    super().append(elem)
  def sum(self):
    output = 0
    for s in self:
      output += s.math
    return output
  def average(self):
    return self.sum() / len(self)


sl = StudentList1()
sl.append(Student(100))
sl.append(Student(80))
sl.append(Student(70))
# sl.append(20) 에러

for s in sl:
  print(s.math)

print(sl.sum())
print(sl.average())

# 컴포지션
class StudentList2:
  def __init__(self) -> None:
    self.__list = []

  @property
  def list(self):
    return self.__list

  def append(self, elem):
    if type(elem) != Student:
      raise "Student를 전달해주세요"
    self.__list.append(elem)
  def sum(self):
    output = 0
    for s in self.__list:
      output += s.math
    return output
  def average(self):
    return self.sum() / len(self.__list)
  

sl2 = StudentList2()
sl2.list.append(Student(300))
print(sl2.sum(), sl2.average())