# 32강. 딕셔너리와 반복문 

# 딕셔너리
# {
#     key: value
# }
#  key로 사용 가능: 숫자 문자열 불 튜플
#  value로 사용 가능: 모든 값

products = [
    {
        "name": "건망고 슬라이스",
        "price": 4000,
        "type": "식품"
    },
    {
        "name": "건망고",
        "price": 4500,
        "type": "과일"
    },
]

for product in products:
    for key in product:
        print(key)
        print(product[key])
    print("-"*20)
    
    

# 
# 
# 
# 
# 
# 
# 
