with open("data.txt", "r") as f:
    text = f.read()
    if text != "":
        print(text.strip().split(" "))

with open("data.txt", "a") as f:
    i = input("데이터를 입력해주세요: ")
    f.write(i + " ")
        