# Exercise 11. 이름을 알파벳 순서로 정렬하기

PEOPLE = [
    {
        "first": "Reuven", "last": "Lerner",
        "email": "reuven@lerner.co.il"
    },
    {
        "first": "Donald", "last": "Trump",
        "email": "president@whitehouse.gov"
    },
    {
        "first": "Aladmir", "last": "Putin",
        "email": "president@kremvax.ru"
    },
    {
        "first": "Vladmir", "last": "Putin",
        "email": "president@kremvax.ru"
    }
    
    
]

import operator

def alphabetize_names():
    for s in sorted(PEOPLE, key=operator.itemgetter("last", "first")):
        print(f"{s["last"]} {s["first"]} {s["email"]}")


alphabetize_names()