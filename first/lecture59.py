# 59강. 조기 리턴과 리스트 평탄화

def flatten(data):
    output = []
    
    for item in data:
        if type(item) == list:
            output.extend(flatten(item))
        else:
            output.append(item)
    
    return output
            


a = [1, 2, [3, [4, 5, 6, 7, [8, 9, 10]]]]
b = [[1, 2], [3], 4, 5, [6, 7, [8, 9], 10]]

a = flatten(a)
b = flatten(b)

print(a)
print(b)