# 57강. 재귀함수(1): 기본

# 팩토리얼 연산
# n! = n * (n - 1) * (n - 2) * ... 1

def factorial(n):
    output = 1
    for i in range(1, n+1):
        output *= i
    return output

print(factorial(2))
print(factorial(3))
print(factorial(4))

# 팩토리얼 점화식
# 1! = 1
# (n이 2이상의 수일 때) n!  = n * (n-1)!

def factorial_recursive(n):
    if n == 1:
        return 1
    return n * factorial_recursive(n -1)

print(factorial_recursive(2))
print(factorial_recursive(3))
print(factorial_recursive(4))
print(factorial_recursive(5))
    