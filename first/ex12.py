# Exercise 12. 특정 글자를 가장많이 가진 단어 찾기

import collections

def my_most_repeating_word(seq):
    count = 0
    idx = 0
    
    for i, s in enumerate(seq):
        max_count = collections.Counter(s).most_common(1)[0][1]
        if max_count > count:
            count = max_count
            idx = i
        
    return seq[idx]

def most_repeating_word(seq):
    return max(seq, key=lambda s: collections.Counter(s).most_common(1)[0][1])


words =['this', 'is', 'an', 'elementary', 'test', 'example']
print(my_most_repeating_word(words))
print(most_repeating_word(words))



