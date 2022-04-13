from typing import List
import re

def decompose_sentence(target: str) -> List[str]:
    cleaned_target = re.subn('[.|,]', '', target)[0]
    return list(cleaned_target.split())

if __name__ == '__main__': 
    sentence: str = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."

    word_lis: List[str] = decompose_sentence(sentence)
    len_lis: List[int] = list(map(len, word_lis))
    print(len_lis)