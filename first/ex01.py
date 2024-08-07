# Exercise 01. 숫자 맞추기
# 
# 사용자에게 입력을 요청하는 방법
# 입력을 원하는 자료현으로 변환하는 방법
# 반복문과 함께 사용하면 좋은 자료
#   -> 데이터베이스 레코드, xml 파일의 요소, 정규 표현식으로 텍스트를 탐색한 결과 

import random

def guessing_game():
    rand_min_number = 0
    rand_max_number = 100
        
    rand_number = random.randint(rand_min_number, rand_max_number + 1)
    
    while True:
        input_number = int(input(">숫자를 맞춰보세요:"))

        if rand_number > input_number:
            print("Too high")
        elif rand_number == input_number:
            print("Just right")
            return
        else:
            print("Too low")


guessing_game()

    