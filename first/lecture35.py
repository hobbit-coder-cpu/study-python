# 35강. 범위와 반복문

print(list(range(3)))
# (0, 3] 0, 1, 2
print(list(range(3, 5)))
#(3, 5] -> 3, 4
print(list(range(1, 10, 2)))
# 1, 3, 5, 7, 9

# range는 반복 가능한 자료형
for i in range(10):
    print(i)
    
for i in range(10, 0-1, -1):
    print(i)
    