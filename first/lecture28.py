# 28강. 리스트의 함수

a = [1, 2, 3, 4, 5]

# 파괴적
# 요소 추가: append, insert, extend
print(a.append(6))
print(a)
print(a.append([1,2,3]))
print(a)
print(a.insert(7, 7))
print(a)
print(a.extend([8, 9, 10]))
print(a)

# 요소 제거: del, pop, remove, clear
del a[0]
print(a)
a.pop()
print(a)
a.remove(8)
print(a)
a.clear()
print(a)
# 요소 정렬: sort
b = [1, 5, 2, 9, 4, 10, 7]
a.sort()
print(a)
a.sort(reverse=True)
print(a)
# 요소 존재를 확인: 

# 비파괴적
# 요소 추가:
# 요소 제거: 
# 요소 정렬: 
# 요소 존재를 확인: in/not in
c = [1, 2, 3, 4]
print(1 in c)
print(100 in c)
print(2 not in c)
print(100 not in c)



