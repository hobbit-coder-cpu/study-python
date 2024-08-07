# 39강. while 반복문

# while True:
#   복합구문

i = 0
while i < 10:
    i += 1
    print(f"{i}번째 반복입니다.")
    
a = [1, 2, 1, 2]
value = 2

while value in a:
    a.remove(value)
    print(a)
    
# import time
# print(time.time())

from time import time
print(time())

begin = time()
end = begin + 5

while time() < end:
    print("똑딱")
print("끝")    

     