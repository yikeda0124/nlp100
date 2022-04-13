from typing import List, Dict
from q03 import decompose_sentence
    

def extract_substring_from_wordlis(word_lis: List['str'], flag_lis: List['bool']) -> Dict[str, int]:
    result: Dict[str, int] = {}
    for i in range(len(word_lis)):
        if flag_lis[i]:
            result[word_lis[i][0]] = i+1
        else:
            result[word_lis[i][:2]] = i+1
    return result

if __name__ == '__main__': 
    sentence: str = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
    index_list: List[int] = [1, 5, 6, 7, 8, 9, 15, 16, 19]
    
    flag_lis: List[bool] = [False for _ in range(len(sentence))]
    for idx in index_list:
        flag_lis[idx-1] = True
    
    word_lis: List['str'] = decompose_sentence(sentence)
    substr_dict:  Dict[str, int] = extract_substring_from_wordlis(word_lis, flag_lis)
    print(substr_dict)