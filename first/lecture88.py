# 88강. 기본 내장 모듈 

import random
print(random.uniform(10, 20))
print(random.randrange(10, 20))
print(random.choice([1, 2, 3, 4, 5]))

import sys
print(sys.argv)

import os
print(os.name)
print(os.listdir("."))
os.mkdir('hello')
os.rename("hello", 'world')
# os.system("시스템 명령어")
os.system("dir")

import time
time.sleep(5)

from urllib import request
target = request.urlopen('http://google.com')
print(target.read())
