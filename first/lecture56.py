# 56강. 메모리 구조(3): 복사

# 변수를 변수에 할당하면 [복사하면]
# 스택에 있는 것이 할당[복사]되는 것이다

a = 10
b = a
a = 20

print(a)
print(b)

# 복합자료형 복사 - 주소를 스택에 저장
c = [1, 2, 3, 4]
d = c

c.append(5)

print(c)
print(d)

e = 10
f = [1, 2, 3, 4]

print(e, f)

def function_e(g, h):
    g = 100
    h = [5, 6, 7, 8]
function_e(e, f)

print(e, f)

def function_f(g, h):
    g = 200
    h.extend([9, 10])
function_f(e, f)

print(e, f)
