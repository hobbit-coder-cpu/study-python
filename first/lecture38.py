# 38강. reversed() 함수와 별 피라미드

# 매개변수: 반복 가능한 것 
# 결과: 그것을 뒤집은 것
# 결과 자료형: 이터레이터 -> list()를 사용해 리스트로 변호나해서 결과 보기

# 리스트
print(list(reversed([1, 2, 3, 4])))

print(list(reversed(range(0, 10))))

height = int(input("층을 입력하기:"))
for i in range(1, height + 1):
    for j in range(i):
        print("*", end="")
    print()
    
for i in range(1, height + 1):
    for j in range(height - i):
        print(" ", end="")
    for j in range(2 * i - 1):
        print("*", end="")
    print()