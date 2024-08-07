# 33강. 딕셔너리의 요소 변경/추가/제거

product = {
    "name": "7D 건조 망고",
    "type": "당절임" 
}



# 요소의 값을 변경하는 방법
product["name"] = "8D 건조 망고"

# 요소를 추가하는 방법
product["price"] = 4000

# 요소를 제거하는 방법 
del product["type"]

# 키의 존재 확인하는 방법
print("price" in product)

# get()
print(product.get("name"))
print(type(product.get("country"))) # <class NoneType>


print(product)

dict_a = {}
dict_a["name"] = "구름"
print(dict_a)

del dict_a["name"]
print(dict_a)

pets = [
    {"name": "구룸", "age": 5},
    {"name": "초코", "age": 3},
    {"name": "아지", "age": 1},
    {"name": "호랑이", "age": 1},
]

print("# 우리 동네 애완 동물들")
for pet in pets:
    print(f"{pet["name"]} {pet["age"]}살")