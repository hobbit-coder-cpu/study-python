# 42강. 리스트, 딕셔너리와 관련된 기본 함수.

a = [52, 273, 32, 103, 57]

print(max(a))
print(max(52, 273, 32, 103, 57))
print(max(*a))
print(min(a))
print(min(52, 273, 32, 103, 57))
print(min(*a))

print(sum(a))


for i in reversed(range(0, 10)):
    print(i)

print(type(reversed(range(0, 10)))) # <class range_iterator>

print("-"* 20)

# enumerate() 함수
fruits = ['banana', 'apple', 'grape']

for f in fruits:
    print(f)
    
for f in enumerate(fruits):
    print(f)
    
for (i, v) in enumerate(fruits):
    print(i, v)   

for [i, v] in enumerate(fruits):
    print(i, v)   

for i, f in enumerate(fruits):
    print(i, f)        
    
product = {
    "name": "아이폰16",
    "price": 6000,
    "made in": "china"
}

print("-"*10)
print("key in product")
for key in product:
    print(key, product[key])

print("-"*10)
print("i in product.keys()")
for i in product.keys():
    print(i)

print("-"*10)
print("i in product.values()")
for i in product.values():
    print(i)

print("-"*10)
print("k, v in product.items()")  
for k, v in product.items():
    print(k, v)

