def cipher(target: str) -> str:
    result: str = ''
    for i in range(len(target)):
        if 'a' <= target[i] and target[i] <= 'z':
            result += chr(219 - ord(target[i]))
        else:
            result += target[i]
    return result

if __name__ == '__main__':
    target: str = 'Hello World!'
    print(cipher(target))
    print(cipher(cipher(target)))