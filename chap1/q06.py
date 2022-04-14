from typing import Set
from q05 import get_ngram

if __name__ == '__main__':
    target1: str = 'paraparaparadise'
    target2: str = 'paragraph'
    
    result1: Set[str] = set(get_ngram(2, target1))
    result2: Set[str] = set(get_ngram(2, target2))
    print('和集合', result1 | result2)
    print('積集合', result1 & result2)
    print('差集合', result1 - result2)