# 76강. 예외 객체와 예외 구분
 
try:
  dajdkf[1]
except Exception as e:
  if type(e) == ValueError:
    print()
  elif type(e) == ConnectionError:
    print()

try:
  dajdkf[1]
except ValueError as e:
  print()
except ConnectionError as e:
  print()
except Exception as e:
  print()
