from typing import List, Union

from pkg_resources import parse_requirements
from q03 import decompose_sentence

def get_ngram(n: int, target: Union[str, List[str]]) -> Union[List[str], List[List[str]]]:
    result = []
    assert n <= len(target)
    for i in range(len(target)-n+1):
        result.append(target[i:i+n])
    return result


if __name__ == '__main__':
    sentence: str = 'I am an NLPer'
    word_lis = decompose_sentence(sentence)
    result1 = get_ngram(2, word_lis)
    result2 = get_ngram(2, sentence)
    print(result1)
    print(result2)