# 43강. 리스트 내포 - list comprehension


# 반복가능한 거을 기반으로
# 새로운 리스트를 만들어내는 문법

A = []
for i in range(0, 10):
    A.append(i)
    print(A)

# A = [2 * i + 1 for i in range(0, 10)]

dollor = [155.43, 302.71, 77.46, 131.28]
print(dollor)

won = [
    i * 1350 
    for i in dollor
]

print(won)
