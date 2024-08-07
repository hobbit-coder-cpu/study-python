# 60강. 튜플 이뮤터블 자료, 뮤터블 자료

# 리스트 []
# 튜플 ()

a = (1, 2, 3)
print(a)
print(a[0])
print(a[1])
print(a[2])

# 요소를 하나 갖는 튜플을 만들고 싶을 때 -> 쉼표
b = (1, )

# 튜플 괄호 생략

a1 = 1, 2, 3
b1 = 1, 
print(type(a1), type(b1))

# 튜플과 리스트의 차이
a2 = [1, 2, 3]
a2[1] = 5

a3 = (1, 2, 3) # 변경 불가
# a3[1] = 10

# 튜플의 장점 
# 1. 외관이 간단
# 다중 할당 구문
[a4, b5] = [10, 20]
(a5, b5) = (10, 20) # a5, b5 = 10, 20

def a():
    return (10, 20, 30)

a6, b6, c6 = a()

a7 = ["바나나", "사과", "고구마"]

for i, v in enumerate(a7):
    print(i, v)
    
b7 = {
    "이름": "별",
    "생일": (2019, 11, 15)
}

for key, value in b7.items():
    print(key, value)
    
# 2. 요소를 변경할 수 없다
# 자료: 뮤터블 자료 + 이뮤터블 자료

p = {
    1: 1
}

print(p)