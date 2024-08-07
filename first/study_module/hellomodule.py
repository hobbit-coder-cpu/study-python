a = 10

def b():
  return 10

class C:
  pass

class Circle:
  def __init__(self, r) -> None:
    if r < 0:
      raise ValueError()
    self.__PI = 3.14
    self.__radius = r

  @property
  def area(self):
    return self.__PI * self.__radius ** 2
  
  @property
  def circumference(self):
    return 2 * self.__PI * self.__radius
  

print("hellomodule.py")
print(__name__) 


if __name__ == "__main__":
  print("area()를 검증")
  Circle(10).area == 314
  print("circumference()를 검증")
  Circle(10).circumference == 62.8