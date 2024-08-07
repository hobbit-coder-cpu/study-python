# 25강. 3장 조건문 마무리

# None, 숫자 0, 빈문자열, 빈 컨테이너: False

i = input("입력해주세요: ").strip()

if i != "": # if not i == "": / if i: 
    print("입력한 내용:", i)
else:
    print("프로그램을 다시 실행해주세요")
    

if i:
    pass
else:
    raise NotImplementedError

arr = [1, 2, 3, 4]

if 1 in arr:
    print("IN!")
    
for i in arr:
    print(i)
    

    