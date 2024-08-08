# Exercise 10. 아무것이나 더하기

def mysum(*param):
    output = param[0]
    
    for i in param[1:]:
        output += i
        
    return output 


print(mysum('abc', 'def'))
print(mysum([1,2,3], [4,5,6,7]))
print(mysum((1,2,3,4), (1,2)))
print(mysum(1, 2, 4, 6, 7))

# | 연산자

d1 = {"spam": 1}
d2 = {"egg": 2}

print("{**d1, **d2}", {**d1, **d2})
print("d1 | d2", d1 | d2)

print("for k in d1 | d2:")
for k in d1 | d2:
    print("key:", k)
    
print()


d2.update(d1)
print("dict.update", d2)

print("for k in d2.update(d1)")
for k in d2:
    print("key:", k)
    
print()



d3 = {"spam": 1, "carrot": 2}
d4 = {"egg": 2, "carrot": 10}

print("{**d3, **d4}", {**d3, **d4})
print("d3 | d4", d3 | d4)
print("{**d4, **d3}", {**d4, **d3})
print("d4 | d3", d4 | d3)
