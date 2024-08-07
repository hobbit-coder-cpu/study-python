# 58강. 재귀함수(2): 피보나치 수열

def fibonacci(n):
    if n <= 0:
        return 0
    if n == 1 or n == 2:
        return 1
    return fibonacci(n - 2) + fibonacci(n - 1) 
    

print("--fibonacci--")
print(fibonacci(0))
print(fibonacci(1))
print(fibonacci(2))
print(fibonacci(3))
print(fibonacci(4))
print(fibonacci(5))
print(fibonacci(6))
print(fibonacci(7))


memo = {1: 1, 2: 1}
def fibonacci_memo(n):  
    if n <= 0:
        return 0

    if n in memo:
        return memo[n]
    
    tmp = fibonacci_memo(n-1) + fibonacci_memo(n-2)
    memo[n] = tmp
    return tmp

print("--fibonacci_memo--")
print(fibonacci_memo(1))
print(fibonacci_memo(2))
print(fibonacci_memo(3))
print(fibonacci_memo(4))
print(fibonacci_memo(5))
print(fibonacci_memo(6))
print(fibonacci_memo(7))


