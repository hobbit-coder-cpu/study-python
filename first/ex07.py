# Exercise 07. 비밀 언어 우비두비 단어 만들기

def ubbi_dudbbi(word):
    output = []
    for ch in word:
        if ch in "aeiou":
            output.append("ub")
        output.append(ch)
    
    return "".join(output)

print(ubbi_dudbbi("milk"))
print(ubbi_dudbbi("program"))
print(ubbi_dudbbi("octopus"))
print(ubbi_dudbbi("elephant"))

