def concat_str(target1: str, target2: str) -> str:
    assert len(target2)-len(target1) == 0
    
    result = ''
    for t1, t2 in zip(target1, target2):
        result += t1
        result += t2
    return result

if __name__ == '__main__': 
    target1: str = 'パトカー'
    target2: str = 'タクシー'
    print(concat_str(target1, target2))