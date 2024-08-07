# Excersize 08. 문자열 정렬하기

def strsort(text):
    result = sorted(text)
    print(type(result))
    return "".join(result)


print(strsort("cba"))