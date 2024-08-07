# 64강. 기본 파일 처리

# 파일 처리
# 읽기 처리 / 쓰기 처리

#  (1) 스트림 연결(stream)
f1= open("test.txt", "r")

# (1-1) with 구문을 이용한 스트림 연결(stream)
with open("test.txt", "r") as f2:
    pass


# (2) 스트림을 통해 데이터 통신
text = f1.read()
print(text)

# (3) 스트림 해제
f1.close()
