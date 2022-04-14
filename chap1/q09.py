from typing import List
from q03 import decompose_sentence
import random
import copy

if __name__ == '__main__':
    target: str = 'I couldn’t believe that I could actually understand what I was reading : the phenomenal power of the human mind.'
    word_lis: List[str] = decompose_sentence(target)
    
    shuffled_word_lis: List[str] = copy.deepcopy(word_lis)

    before_shuffle: List[int] = []
    after_shuffle: List[int] = []
    for i in range(len(word_lis)):
        if i == 0 or i == len(word_lis)-1:
            continue
        if len(word_lis[i]) > 4:
            before_shuffle.append(i)
            after_shuffle.append(i)
    random.shuffle(after_shuffle)

    for i in range(len(before_shuffle)):
        shuffled_word_lis[before_shuffle[i]] = word_lis[after_shuffle[i]]

    print(word_lis)
    print(shuffled_word_lis)



