# 75강. 예외 처리의 else finally 구문

try: 
  pass
except:
  pass
finally:
  pass

def 함수():
  print("함수에 진입했습니다.")
  try:
    print("try 구문에 진입했습니다.")
    return 
    print("try 구문이 끝났습니다.")
  except:
    print("except 구문에 진입했습니다.")
  finally:
    print("finally 구문에 진입했습니다.") # try구문에서 return을 하더라도 해당 구문을 무조건 실행
  
  print("함수가 끝났습니다.")


함수()

