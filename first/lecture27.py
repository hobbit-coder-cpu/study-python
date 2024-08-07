# 27강. 수열, 배열, 리스트 기본

# 숫자들이 일렬로 나열된 것: 수열
# a = (1, 2, 3, 4)

# 배열: 길이가 고정 ex) 문자열
# 리스트: 배열에 요소 추가/제거 등의 기능을 추가한 것
arr = [1, "hello", 3.1]
print(type(arr)) # <class 'list'>
print(type(arr[0]))
print(type(arr[1]))
print(type(arr[2]))

# 리스트 연산
print(arr + arr)
print(arr * 5)
print(len(arr))
print(arr[0:2])
print(arr[::-1])

# 중첩 리스트
arr2 = [
    [1, 2, 3], 
    [4, 5, 6], 
    [7, 8, 9]
]

print(arr2)
