def get_odd_subsequence(target: str) -> str:
    return target[::2]

if __name__ == '__main__': 
    target: str = 'パタトクカシーー'
    print(get_odd_subsequence(target))