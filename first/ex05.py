# Exercise 05. 피그 라틴 단어 만들기
# 문자열 탐색, 반복, 슬라이싱 


def pig_latin(text):
    
    if text[0] in "aeiou":
        return "".join([text, "way"])
    else:
        return "".join([text[1:], text[0], "ay"])
    

print(pig_latin("air"))
print(pig_latin("eat"))
print(pig_latin("python"))
print(pig_latin("computer")) 
