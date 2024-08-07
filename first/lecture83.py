# 83강. 상속 기본

class Shape: # super class
  def __init__(self):
    raise "생성자를 구현해주세요"
  @property
  def area():
    raise "넓이를 구현해주세요 넓이를 리턴하는 함수를 작성해주세요"
  def 출력보조(self):
    raise "출력 보조 함수를 구현해주세요 출력 전 한마디를 입력해주세요"
  def 출력(self):
      print("=" * 10)
      print("*" * 10)
      print("=" * 10)
      self.출력보조()
      print(f"넓이: {self.area}")
      print("=" * 10)
      print("*" * 10)
      print("=" * 10)


class Circle(Shape): # sub class 
  def __init__(self, r):
    self.__PI = 3.14
    self.__radius = r

  @property
  def radius(self):
    return self.__radius
  
  @property
  def area(self):
    return self.__PI * self.__radius ** 2

  def 출력보조(self):
    print(f"원의 반지름은 {self.radius}")


c = Circle(10)
c.출력()


