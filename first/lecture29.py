# 29강. for 반복문과 리스트, 항등원, 총합과 총곱

# 항등원: 임의의 원소에 특정 연산을 했을 때 재귀시키는 원소
# A + ? = A, 덧셈의 항등원 0
# A * ? = A, 곱셈의 항등원 1

# for 반복변수 in 리스트:

a = [10, 20, 30]

sum = 0
for i in a:
    sum += i

mul = 1
for i in a:
    mul *= i

print(sum, mul)

import functools

def multiply(a, b):
    return a * b

def add(a, b):
    return a + b

print(functools.reduce(add, a, 0))
print(functools.reduce(multiply, a, 1))