# Excersize 06. 피그 라틴 문장 만들기

def pig_latin(text):
    
    if text[0] in "aeiou":
        return "".join([text, "way"])
    else:
        return "".join([text[1:], text[0], "ay"])

def pl_sentence(text):
    output = []
    for w in text.split():
        output.append(pig_latin(w))
    
    return " ".join(output) 
        
print(pl_sentence('this is a test translation'))

s = "abc  def  ghi"
print(s.split())
print(s.split(" "))