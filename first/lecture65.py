# 65강. 간단한 CSV(Comma Separated Values) 파일 읽고 쓰기

import random
hangul = list("가나다라마바사아자차카타파하")

with open("human.txt", "w") as f:
    f.write("이름,몸무게,키\n")
    for i in range(1000):
        name = random.choice(hangul) + random.choice(hangul)
        weight = random.randrange(40, 120)
        height = random.randrange(140, 200)
        f.write(f"{name},{weight},{height}\n")
        # print("{},{},{}".format(name, weight, height))
        
with open("human.txt", "r") as f:
    for n, line in enumerate(f):
        name, weight, height = line.strip().split(",")
        if n == 0:
            continue
            
        weight = int(weight)
        height = int(height)
        bmi = weight / (height / 100) ** 2
        print(f"{name} {weight} {height} {bmi}")