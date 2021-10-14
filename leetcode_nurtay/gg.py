import itertools
from typing import Protocol

s = "wordgoodgoodgoodbestword"
words = ["word","good","best","word"]

v = list(itertools.permutations(words))

new_words = []
for i in v:
    new_words.append(i[0]+i[1])

print(new_words)

print([s.find(word) for word in new_words if s.find(word) != -1])