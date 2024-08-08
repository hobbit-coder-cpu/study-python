# Exercise 09. 처음과 마지막 요소 찾기

def firstlast(seq):
    step = max(len(seq)-1, 0)
    return seq[:1] + seq[-1:]

print(firstlast([1]))
print(firstlast((1, 2)))
print(firstlast([1, 2, 3]))
print(firstlast("helloworld"))

import operator

