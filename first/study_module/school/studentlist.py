class StudentList:
  def __init__(self) -> None:
    self.__list = []

  def append(self, s):
    self.__list.append(s)
  def print(self):
    print("student list")
    for s in self.__list:
      print(s.sum())
