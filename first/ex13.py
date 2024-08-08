# Exercise 13. 튜플 레코드 출력하기

PEOPLE = [
    ('Donald', 'Trump', 7.85),
    ('Vladimir', 'Putin', 3.626),
    ('Jinging', 'Xi', 10.603)
]

import operator

def my_format_sort_records():
    print('my_format_sort_records()')
    for record in sorted(PEOPLE, key=operator.itemgetter(1, 0)):
        print(f'{record[1]:10} {record[0]:10} {record[2]:5.2f}')
        
def format_sort_records():
    print('format_sort_records()')
    output = []
    template = '{1:10} {0:10} {2:5.2f}'
    for person in sorted(PEOPLE, key=operator.itemgetter(1,0)):
        output.append(template.format(*person))
        print(template.format(*person))
    
my_format_sort_records()
print()
print()
format_sort_records()

# namedtuple

from collections import namedtuple

Point = namedtuple("poin", ['x', 'y'])

p = Point(10, 100)
print(p.x)
print(p.y)

p1 = Point._make([10, 20])
print(p1.x)
print(p1.y)