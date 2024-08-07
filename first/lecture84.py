# 84강. 오버라이드

class 부모:
  def 함수(self):
    print("부모함수")

class 자식(부모):
  def 함수(self):
    # 자식 함수에서 부모함수 호출하는 방법 #1
    부모.함수(self)
    # 자식 함수에서 부모함수 호출하는 방법 #2
    super().함수()
    print("자식함수")


자 = 자식()
자.함수()

# 자신의 클래스에 그 함수가 있는가?
# -> 없다면 부모 클래스에 그 함수가 있는가?
class 버튼:
  def __init__(self) -> None:
    print("버튼을 초기화합니다.")
    print("버튼을 만듭니다.")
    print("버튼을 화면에 출력합니다.")

class 빨간버튼(버튼):
  def __init__(self) -> None:
    super().__init__()
    print("버튼을 빨간색으로 칠합니다.")

class 파랑버튼(버튼):
  def __init__(self) -> None:
    super().__init__()
    print("버튼을 파란색으로 칠합니다.")

class 노랑버튼(버튼):
  def __init__(self) -> None:
    super().__init__()
    print("버튼을 노란색으로 칠합니다.")

빨간버튼()
파랑버튼()
노랑버튼()


