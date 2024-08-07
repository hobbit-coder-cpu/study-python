# 40강. break/continue


i = 0
while True:
    print(f"{i}번째 반복입니다.")
    i += 1
    
    a = input("> 종료하시겠습니까?(y/n): ")
    if a in ['y', 'Y']:
        print("반복문을 종료합니다.")
        break
